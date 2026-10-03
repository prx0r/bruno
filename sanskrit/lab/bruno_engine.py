"""Bruno imaginal runtime — LEXICON · WHEEL · SCENE · LOCUS + Caelum.

Operational over triginta-sigilli inventory. Not ceremonial.
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

from pathlib import Path as _P
import sys as _sys
_worlds = _P(__file__).resolve().parent.parent / "worlds"
if str(_worlds) not in _sys.path:
    _sys.path.insert(0, str(_worlds))
from bruno_primitives import Arbor, Catena, Caelum, Locus, build_matrika_caetum, load_inventory

LAB = Path(__file__).resolve().parent
WORLDS = Path(__file__).resolve().parent.parent / "worlds"

MODES = ("encode", "explore")


@dataclass
class ImaginalToken:
    symbol: str
    label: str
    image: str
    meta: dict = field(default_factory=dict)


@dataclass
class Lexicon:
    name: str
    tokens: dict[str, ImaginalToken] = field(default_factory=dict)

    def add(self, symbol: str, label: str, image: str, **meta: Any) -> ImaginalToken:
        t = ImaginalToken(symbol=symbol, label=label, image=image, meta=meta)
        self.tokens[symbol] = t
        return t

    def get(self, symbol: str) -> ImaginalToken | None:
        return self.tokens.get(symbol)

    def ensure_from_varnas(self) -> int:
        """Seed lexicon from lab varnas (phonetic structure first)."""
        varnas = json.loads((LAB / "data" / "varnas.json").read_text())["items"]
        n = 0
        for v in varnas:
            sym = v.get("iast") or v.get("id")
            if not sym or sym in self.tokens:
                continue
            place = v.get("place") or "other"
            manner = v.get("manner") or ""
            # imaginal identity grounded in phonetics, not Apollo mythology
            image = f"{v.get('devanagari','')} {place}/{manner} · {v.get('colorScaffold','')}"
            self.add(sym, f"{v.get('devanagari','')} {sym}", image,
                     place=place, manner=manner, id=v.get("id"))
            n += 1
        return n


@dataclass
class WheelAxis:
    id: str
    values: list[str]


@dataclass
class Wheel:
    """Jagged multi-dimensional combinatorial device (encode | explore)."""

    id: str
    axes: list[WheelAxis]
    mode: str = "encode"
    constraints: list[str] = field(default_factory=list)
    score_fn: Callable[[dict], float] | None = None

    def state_space_size(self) -> int:
        n = 1
        for a in self.axes:
            n *= max(1, len(a.values))
        return n

    def enumerate(self, limit: int = 64) -> list[dict]:
        """Enumerate axis selections (capped). Sparse/jagged constraint later."""
        axes = self.axes
        if not axes:
            return [{}]
        out: list[dict] = [{}]
        for ax in axes:
            nxt = []
            for base in out:
                for val in ax.values:
                    nxt.append({**base, ax.id: val})
                    if len(nxt) >= limit:
                        break
                if len(nxt) >= limit:
                    break
            out = nxt
            if len(out) >= limit:
                break
        return out

    def random_state(self, rng: random.Random | None = None) -> dict:
        rng = rng or random.Random()
        return {ax.id: rng.choice(ax.values) for ax in self.axes if ax.values}


@dataclass
class Scene:
    state: dict
    tokens: list[ImaginalToken]
    text: str
    score: float = 0.0
    mode: str = "encode"

    def to_dict(self) -> dict:
        return {
            "state": self.state,
            "scene_text": self.text,
            "score": self.score,
            "mode": self.mode,
            "tokens": [t.label for t in self.tokens],
        }


@dataclass
class LocusMap:
    """Stable addresses for scenes / knowledge."""

    topology: str = "caelum"
    caelum: Caelum = field(default_factory=lambda: Caelum(name="lab"))
    scenes: dict[str, dict] = field(default_factory=dict)

    def place_scene(self, scene: Scene, parent: str = "oct_+++") -> str:
        lid = self.caelum.place(parent, scene.text[:80], {
            "kind": "scene",
            "mode": scene.mode,
            "score": scene.score,
            "state": scene.state,
        })
        self.scenes[lid] = scene.to_dict()
        return lid


@dataclass
class BrunoEngine:
    lexicon: Lexicon = field(default_factory=lambda: Lexicon(name="sanskrit"))
    wheels: dict[str, Wheel] = field(default_factory=dict)
    loci: LocusMap = field(default_factory=LocusMap)
    seals: list[dict] = field(default_factory=list)
    mode: str = "encode"

    def __post_init__(self) -> None:
        inv = load_inventory()
        self.seals = inv.get("seals", [])
        self.wheels["varna_series"] = self.default_series_wheel()
        self.wheels["faculty_pair"] = Wheel(
            id="faculty_pair",
            axes=[
                WheelAxis("faculty", ["memory", "intellect", "eloquence", "understanding"]),
                WheelAxis("mode", ["install", "absorb", "derive", "speak"]),
            ],
            mode="explore",
        )

    @staticmethod
    def default_series_wheel() -> Wheel:
        series = {
            "gutturals": ["ka", "kha", "ga", "gha", "ṅa"],
            "dentals": ["ta", "tha", "da", "dha", "na"],
            "labials": ["pa", "pha", "ba", "bha", "ma"],
        }
        axes = []
        for name, vals in series.items():
            axes.append(WheelAxis(name, vals))
        return Wheel(id="varna_series", axes=axes, mode="explore")

    def compile_scene(self, state: dict, mode: str | None = None) -> Scene:
        mode = mode or self.mode
        tokens: list[ImaginalToken] = []
        parts = []
        for k, v in state.items():
            tok = self.lexicon.get(str(v)) or self.lexicon.get(str(k)) or ImaginalToken(
                symbol=str(v), label=str(v), image=str(v), meta={"axis": k}
            )
            # if state value is axis value like 'dentals', keep label
            if tok.symbol != str(v):
                tok = ImaginalToken(symbol=str(v), label=str(v), image=str(v), meta={"axis": k})
            tokens.append(tok)
            parts.append(f"{k}={tok.label}")
        text = " · ".join(parts) if parts else "(empty)"
        score = float(len(tokens))
        if mode == "explore":
            score += 0.5 * len(set(t.image for t in tokens))
        return Scene(state=state, tokens=tokens, text=text, score=score, mode=mode)

    def encode_varna_row(self, series: str = "dentals") -> Scene:
        """Encode one matrika series into a scene + caelum locus."""
        rows = {
            "dentals": ["ta", "tha", "da", "dha", "na"],
            "gutturals": ["ka", "kha", "ga", "gha", "ṅa"],
            "labials": ["pa", "pha", "ba", "bha", "ma"],
        }
        vals = rows.get(series, rows["dentals"])
        state = {f"slot{i+1}": v for i, v in enumerate(vals)}
        state["series"] = series
        scene = self.compile_scene(state, mode="encode")
        parent = self.loci.caelum.place("oct_+++", f"matrika/{series}", {"kind": "series"})
        for i, v in enumerate(vals, 1):
            lid = self.loci.caelum.place(parent, f"{series}[{i}] {v}", {
                "kind": "varna_imago",
                "symbol": v,
            })
            tok = self.lexicon.get(v)
            if tok:
                self.loci.caelum.attach_imago(
                    lid,
                    imago={"symbol": v, "image": tok.image, "series": series},
                    vinculum={"series": series, "slot": i},
                )
        return scene

    def explore(self, wheel_id: str = "varna_series", n: int = 3, seed: int | None = 42) -> list[Scene]:
        w = self.wheels[wheel_id]
        rng = random.Random(seed)
        scenes = []
        for _ in range(n):
            st = w.random_state(rng)
            scenes.append(self.compile_scene(st, mode="explore"))
        return scenes

    def caelum_install_matrika(self, series: str = "dentals") -> dict:
        cael = build_matrika_caetum(series)
        # merge into engine loci
        for lid, loc in cael.loci.items():
            if lid not in self.loci.caelum.loci:
                self.loci.caelum.loci[lid] = loc
        return cael.export()

    def seal_of(self, name: str | int) -> dict | None:
        key = str(name).lower()
        for s in self.seals:
            sname = str(s.get("name") or "").lower()
            if sname.startswith(key) or str(s.get("n")) == key:
                return s
        return None

    def choose_operator(self, topology: str) -> str:
        m = {
            "sequential": "catena",
            "hierarchical": "arbor",
            "spatial": "caelum",
            "graded": "scala",
            "combinatorial": "combinans",
            "grid": "campus",
        }
        return m.get(topology, "caelum")

    def status(self) -> dict:
        return {
            "lexicon_size": len(self.lexicon.tokens),
            "wheels": {
                wid: {"axes": len(w.axes), "size": w.state_space_size(), "mode": w.mode}
                for wid, w in self.wheels.items()
            },
            "caelum_loci": len(self.loci.caelum.loci),
            "scenes": len(self.loci.scenes),
            "seals": len(self.seals),
            "mode": self.mode,
        }


def build_default_engine() -> BrunoEngine:
    eng = BrunoEngine()
    n = eng.lexicon.ensure_from_varnas()
    eng.lexicon.add("S", "Spiderman-room (forum example)", "familiar room template", kind="template")
    eng.lexicon.add("memory", "Memory faculty", "Castle memory figure hub", kind="faculty")
    eng.lexicon.add("intellect", "Intellect faculty", "Castle intellect hub", kind="faculty")
    eng.lexicon.add("eloquence", "Eloquence faculty", "Castle eloquence hub", kind="faculty")
    eng.lexicon.add("dentals", "Dental series", "green/heart series", series="dentals")
    eng.lexicon.add("gutturals", "Guttural series", "red/root series", series="gutturals")
    eng.lexicon.add("labials", "Labial series", "blue/throat series", series="labials")
    eng.lexicon.add("install", "Install", "form+color+locus", mode="install")
    eng.lexicon.add("absorb", "Absorb", "Laya silence", mode="absorb")
    eng.lexicon.add("derive", "Derive", "Pāṇini trace", mode="derive")
    eng.lexicon.add("speak", "Speak", "uccāra recoil", mode="speak")
    eng.lexicon.add("ka", "क ka", "velar unvoiced stop", place="velar")
    eng.lexicon.add("ta", "त ta", "dental unvoiced stop", place="dental")
    # ensure varnas filled
    eng.lexicon.ensure_from_varnas()
    _ = n
    return eng


if __name__ == "__main__":
    e = build_default_engine()
    print("Bruno engine", e.status())
    sc = e.encode_varna_row("dentals")
    print("encode dentals:", sc.to_dict()["scene_text"], "loci", e.loci.caelum.loci and len(e.loci.caelum.loci))
    for s in e.explore("varna_series", n=3):
        print(" explore:", s.text)
    print("choose sequential →", e.choose_operator("sequential"))
    print("seal 2", e.seal_of("2"))
