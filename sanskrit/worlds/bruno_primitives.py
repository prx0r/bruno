"""Bruno WorldPrimitive runtimes — Caelum and friends (lab, not ceremony)."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INVENTORY = ROOT / "triginta-sigilli-inventory.json"


def load_inventory() -> dict:
    return json.loads(INVENTORY.read_text())


@dataclass
class Locus:
    id: str
    label: str
    content: dict = field(default_factory=dict)
    children: list[str] = field(default_factory=list)
    relations: dict[str, list[str]] = field(default_factory=dict)

    def add_rel(self, kind: str, other: str) -> None:
        self.relations.setdefault(kind, [])
        if other not in self.relations[kind]:
            self.relations[kind].append(other)


@dataclass
class Caelum:
    """Sphere ∩ 3 orthogonal great circles → 8 octants; recursive subdivision.

    Addressability comes from distinctions, not a precounted slot list.
    """

    name: str
    loci: dict[str, Locus] = field(default_factory=dict)
    _n: int = 0

    def _next_id(self, parent: str | None) -> str:
        self._n += 1
        base = f"loc{self._n:03d}"
        if not parent:
            return base
        p = self.loci[parent]
        return f"{p.id}/q{len(p.children) + 1}"

    def seed(self) -> None:
        """Create the 8 octants of the sphere."""
        if any(i.startswith("root") or i == "octants" for i in self.loci):
            return
        axes = ["+", "-"]
        for x in axes:
            for y in axes:
                for z in axes:
                    lid = f"oct_{x}{y}{z}"
                    label = f"{x}x {y}y {z}z"
                    self.loci[lid] = Locus(
                        id=lid,
                        label=label,
                        content={"kind": "octant", "axes": {"x": x, "y": y, "z": z}},
                    )
        # lateral relations
        ids = list(self.loci)
        for i, a in enumerate(ids):
            for b in ids[i + 1 :]:
                la, lb = a[4:], b[4:]
                diffs = sum(1 for u, v in zip(la, lb) if u != v)
                if diffs == 1:
                    self.loci[a].add_rel("adjacent", b)
                    self.loci[b].add_rel("adjacent", a)
                elif diffs == 3:
                    self.loci[a].add_rel("opposite", b)
                    self.loci[b].add_rel("opposite", a)

    def place(self, parent: str, label: str, content: dict | None = None) -> str:
        self.seed()
        if parent not in self.loci:
            raise KeyError(f"unknown locus parent: {parent}")
        lid = self._next_id(parent)
        self.loci[lid] = Locus(id=lid, label=label, content=content or {})
        self.loci[parent].children.append(lid)
        return lid

    def subdivide(self, parent: str, labels: list[str]) -> list[str]:
        return [self.place(parent, lab, {"kind": "subregion"}) for lab in labels]

    def navigate(self, locus_id: str) -> dict:
        self.seed()
        if locus_id not in self.loci:
            raise KeyError(locus_id)
        loc = self.loci[locus_id]
        return {
            "id": loc.id,
            "label": loc.label,
            "content": loc.content,
            "children": loc.children,
            "relations": loc.relations,
        }

    def retrieve(self, query: str) -> list[dict]:
        q = query.lower()
        hits = []
        for loc in self.loci.values():
            blob = (loc.label + " " + json.dumps(loc.content)).lower()
            if q in blob:
                hits.append(self.navigate(loc.id))
        return hits

    def attach_imago(self, locus_id: str, imago: dict, vinculum: dict | None = None) -> None:
        """Bruno install: bind IMAGO + VINCULUM onto a LOCUS."""
        loc = self.loci[locus_id]
        loc.content["imago"] = imago
        if vinculum:
            loc.content["vinculum"] = vinculum
        # cross-links by shared keys in vinculum
        if vinculum:
            for kind, target in vinculum.items():
                if isinstance(target, str) and target in self.loci:
                    loc.add_rel(str(kind), target)
                    self.loci[target].add_rel(str(kind), locus_id)

    def export(self) -> dict:
        return {
            "name": self.name,
            "n_loci": len(self.loci),
            "loci": [
                {
                    "id": l.id,
                    "label": l.label,
                    "content": l.content,
                    "children": l.children,
                    "relations": l.relations,
                }
                for l in self.loci.values()
            ],
        }


@dataclass
class Catena:
    """Sequence primitive: A → B → C."""

    name: str
    steps: list[str] = field(default_factory=list)

    def push(self, item: str) -> None:
        self.steps.append(item)

    def walk(self) -> list[dict]:
        out = []
        for i, s in enumerate(self.steps):
            out.append(
                {
                    "i": i,
                    "item": s,
                    "precedes": self.steps[i + 1] if i + 1 < len(self.steps) else None,
                    "follows": self.steps[i - 1] if i > 0 else None,
                }
            )
        return out


@dataclass
class Arbor:
    name: str
    nodes: dict[str, dict] = field(default_factory=dict)

    def attach(self, node: str, parent: str | None, meta: dict | None = None) -> None:
        self.nodes[node] = {"parent": parent, "meta": meta or {}, "children": []}
        if parent:
            self.nodes[parent]["children"].append(node)

    def walk(self, root: str, depth: int = 0) -> list[dict]:
        out = [{"id": root, "depth": depth}]
        for c in self.nodes.get(root, {}).get("children", []):
            out.extend(self.walk(c, depth + 1))
        return out


def build_matrika_caetum(row: str = "dentals") -> Caelum:
    """Install one phoneme series as IMAGOes in a Caelum."""
    rows = {
        "dentals": [
            ("ta", "त", "ta", "#1a4a2a"),
            ("tha", "थ", "tha", "#1a4a2a"),
            ("da", "द", "da", "#1a4a2a"),
            ("dha", "ध", "dha", "#1a4a2a"),
            ("na", "न", "na", "#1a4a2a"),
        ],
        "gutturals": [
            ("ka", "क", "ka", "#5c1a1a"),
            ("kha", "ख", "kha", "#5c1a1a"),
            ("ga", "ग", "ga", "#5c1a1a"),
            ("gha", "घ", "gha", "#5c1a1a"),
            ("ṅa", "ङ", "ṅa", "#5c1a1a"),
        ],
    }
    items = rows.get(row, rows["dentals"])
    cael = Caelum(name=f"matrika-{row}")
    cael.seed()
    region = cael.place("oct_+++", f"matrika/{row}", {"kind": "series_region", "series": row})
    for key, deva, iast, color in items:
        lid = cael.place(
            region,
            f"{key} {deva}",
            {
                "kind": "varna_imago",
                "id": key,
                "devanagari": deva,
                "iast": iast,
                "color": color,
            },
        )
        cael.attach_imago(
            lid,
            imago={
                "devanagari": deva,
                "iast": iast,
                "articulation": key,
                "color": color,
                "locus": lid,
            },
            vinculum={
                "color": color,
                "series": row,
                "practices": "chant-then-contractio",
            },
        )
    # catena for drill order
    cat = Catena(name=f"drill-{row}")
    for key, _, _, _ in items:
        cat.push(key)
    cael.loci["__catena"] = Locus(
        id="__catena",
        label="drill order",
        content={"kind": "catena", "steps": cat.steps},
    )
    return cael


def _demo() -> dict:
    inv = load_inventory()
    cael = build_matrika_caetum("dentals")
    dentals = [i for i in inv["seals"] if i["n"] in (1, 2, 3, 4, 6)]
    print("Bruno stack v2 — Caelum + primitives")
    print(f"Inventory seals: {len(inv['seals'])}")
    print(f"WorldPrimitive types: {len(inv['worldPrimitives'])}")
    print("Core seals:", ", ".join(f"{s['n']}:{s['name']}" for s in dentals))
    print(f"Caelum loci: {cael.loci and len(cael.loci)}")
    # navigate a dental
    target = next(l for l in cael.loci.values() if "त" in l.label or l.content.get("id") == "ta")
    print("Navigate ta:", json.dumps(cael.navigate(target.id), ensure_ascii=False)[:200])
    print("Retrieve heart/green:", len(cael.retrieve("green")), "hits")
    return cael.export()


if __name__ == "__main__":
    _demo()
