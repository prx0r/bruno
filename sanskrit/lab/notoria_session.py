"""Castle Notoria faculty session shell — operational method, not full medieval regime.

Faculty engine: memory · intellect · eloquence · understanding
Method of places ↔ Bruno LOCUS/IMAGO
Abbreviata ethic: extract what you need
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from pathlib import Path

from bruno_engine import BrunoEngine, build_default_engine
from panini_runtime import PaniniRuntime

LAB = Path(__file__).resolve().parent

FACULTIES = {
    "memory": {
        "castle": "Prayer/figure for memory; method of places",
        "lab_goal": "Retain phoneme stacks + loci",
        "notoria_hub": "memory",
    },
    "intellect": {
        "castle": "Prayer/figure for intellect/understanding",
        "lab_goal": "Pāṇini rule insight + derivation",
        "notoria_hub": "intellect",
    },
    "eloquence": {
        "castle": "Prayer/figure for eloquence",
        "lab_goal": "Spoken Sanskrit / uccāra recoil",
        "notoria_hub": "eloquence",
    },
    "understanding": {
        "castle": "Related to intellect in tradition",
        "lab_goal": "Conceptual Trika/Tantrāloka grasp",
        "notoria_hub": "understanding",
    },
}


@dataclass
class NotoriaSession:
    faculty: str = "memory"
    series: str = "dentals"
    duration_min: int = 25
    purification: bool = False  # optional
    use_liturgical_text: bool = False  # optional historical layer
    notes: str = ""
    engine: BrunoEngine = field(default_factory=build_default_engine)
    panini: PaniniRuntime = field(default_factory=PaniniRuntime)
    steps: list[dict] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.faculty not in FACULTIES:
            raise ValueError(f"unknown faculty: {self.faculty}")

    def step(self, name: str, detail: dict | None = None) -> None:
        self.steps.append({"name": name, "t": time.time(), **(detail or {})})

    def run(self) -> dict:
        eng = self.engine
        pan = self.panini
        faculty_meta = FACULTIES[self.faculty]

        self.step("intention", {
            "faculty": self.faculty,
            "series": self.series,
            "castle": faculty_meta["castle"],
            "lab_goal": faculty_meta["lab_goal"],
        })
        if self.purification:
            self.step("purification_optional", {
                "note": "quiet body, clear intention — not costume magic (Castle Abbreviata ethic)"
            })
        # notoria hub / figure
        self.step("open_figure_hub", {
            "hub": faculty_meta["notoria_hub"],
            "analogy": "Castle notae = discipline figure/room",
        })
        # install matrika row into caelum (Bruno places)
        scene = eng.encode_varna_row(self.series)
        self.step("install_series", {
            "series": self.series,
            "scene": scene.to_dict(),
            "method": "Bruno LOCUS+IMAGO · Castle method of places",
        })
        # contractio simulation: single locus focus
        focus = None
        for lid, loc in eng.loci.caelum.loci.items():
            if loc.content.get("kind") == "varna_imago":
                focus = loc
                break
        if focus:
            self.step("contractio", {
                "focus": focus.id,
                "label": focus.label,
                "technique": "fuse form+sound+colour+locus+emotion",
                "pair": "Laya bindu",
            })
        # Pāṇini mini-task
        if self.faculty == "intellect":
            der = pan.derive_guna("i")
            self.step("panini_trace", {"derive": der.to_dict()})
            rules = pan.browse("1.3", limit=5)
            self.step("browse_rules", {"rules": [r.to_dict() for r in rules]})
        else:
            pr = pan.expand_pratyahara("ac")
            self.step("panini_pratyahara", {"id": "ac", "expands": pr})
        # eloquence recoil
        self.step("speak_recoil", {
            "instruction": "Chant series eyes-closed then speak one Sanskrit word using a letter",
            "series": self.series,
        })
        # log
        self.step("log", {
            "what_dissolved": None,
            "what_became_skill": None,
            "vinculum_strength": None,
        })
        return self.summary()

    def summary(self) -> dict:
        return {
            "faculty": self.faculty,
            "series": self.series,
            "duration_min": self.duration_min,
            "steps": self.steps,
            "engine": self.engine.status(),
            "method_notes": [
                "Notoria = faculty shell + method of places (Castle)",
                "Bruno = internal geometry (Caelum/IMAGO)",
                "Pāṇini = transformation traces",
                "StoneDoorway = optional door + guide voice later",
            ],
        }


def run_daily(faculty: str = "memory", series: str = "dentals") -> dict:
    s = NotoriaSession(faculty=faculty, series=series)
    return s.run()


if __name__ == "__main__":
    out = run_daily("memory", "dentals")
    print(json.dumps({
        "faculty": out["faculty"],
        "series": out["series"],
        "n_steps": len(out["steps"]),
        "step_names": [x["name"] for x in out["steps"]],
        "engine": out["engine"],
    }, indent=2))
