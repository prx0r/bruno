"""Pāṇini runtime — rules, pratyāhāra queries, derivation traces.

Transformation system, not mnemonic representation.
Source corpus: sources/panini (Vidyut sutrapatha + GRETIL astadhyayi).
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from worldir import load_pratyaharas, load_varnas

LAB = Path(__file__).resolve().parent
DATA = LAB / "data"
KEY = json.loads((DATA / "key_sutras.json").read_text())
MERGED = json.loads((DATA / "sutrapatha_merged.json").read_text())


@dataclass
class PaniniRule:
    sutra: str
    iast: str = ""
    hk: str = ""
    domain: str = "general"
    conditions: list[str] = field(default_factory=list)
    operation: str | None = None
    provenance: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "sutra": self.sutra,
            "iast": self.iast,
            "hk": self.hk,
            "domain": self.domain,
            "conditions": self.conditions,
            "operation": self.operation,
            "provenance": self.provenance,
        }


@dataclass
class DerivationStep:
    before: list[str]
    sutra: str
    rule: PaniniRule
    after: list[str]
    note: str = ""

    def to_dict(self) -> dict:
        return {
            "before": self.before,
            "sutra": self.sutra,
            "rule": self.rule.to_dict(),
            "after": self.after,
            "note": self.note,
        }


@dataclass
class Derivation:
    input: list[str]
    steps: list[DerivationStep] = field(default_factory=list)
    output: list[str] = field(default_factory=list)
    status: str = "open"

    def add(self, step: DerivationStep) -> None:
        self.steps.append(step)
        self.output = step.after

    def trace(self) -> list[dict]:
        return [s.to_dict() for s in self.steps]

    def to_dict(self) -> dict:
        return {
            "input": self.input,
            "output": self.output,
            "status": self.status,
            "steps": self.trace(),
        }


class PaniniRuntime:
    def __init__(self) -> None:
        self.rules: dict[str, PaniniRule] = {}
        self._index_rules()
        self.varnas = {v["id"]: v for v in load_varnas()}
        self.pratyaharas = {p["id"]: p for p in load_pratyaharas()}

    def _index_rules(self) -> None:
        for item in MERGED.get("items", []):
            code = item["sutra"]
            self.rules[code] = PaniniRule(
                sutra=code,
                iast=item.get("iast", ""),
                hk=item.get("hk", ""),
                domain=code.split(".")[0] if "." in code else "",
                provenance={
                    "hk": "Vidyut sutrapatha",
                    "iast": "GRETIL astadhyayi jsonl when present",
                    "kind": "sourceCorpus",
                },
            )
        # curated operations for common teaching sutras
        ops = {
            "1.1.1": {"operation": "define_vrddhi", "domain": "phonology"},
            "1.1.2": {"operation": "define_guna", "domain": "phonology"},
            "1.1.3": {"operation": "guna_vrddhi_targets", "domain": "phonology"},
            "1.2.1": {"operation": "operation_of_sutras", "domain": "method"},
            "1.2.2": {"operation": "operation_of_sutras", "domain": "method"},
            "1.2.3": {"operation": "operation_of_sutras", "domain": "method"},
            "1.2.4": {"operation": "operation_of_sutras", "domain": "method"},
            "1.2.5": {"operation": "operation_of_sutras", "domain": "method"},
            "1.2.6": {"operation": "operation_of_sutras", "domain": "method"},
            "1.3.1": {"operation": "dhAtu_class", "domain": "dhatu"},
            "1.3.2": {"operation": "it_marker", "domain": "pratyahara"},
            "1.3.3": {"operation": "hal_antya", "domain": "pratyahara"},
            "1.3.4": {"operation": "vibhaktau", "domain": "pratyahara"},
            "1.4.1": {"operation": "sangya", "domain": "it"},
            "1.4.2": {"operation": "sangya", "domain": "it"},
            "1.4.3": {"operation": "sangya", "domain": "it"},
            "1.4.4": {"operation": "sangya", "domain": "it"},
            "1.4.5": {"operation": "sangya", "domain": "it"},
            "1.4.7": {"operation": "sangya", "domain": "it"},
            "1.4.14": {"operation": "sangya", "domain": "it"},
            "1.4.33": {"operation": "sangya", "domain": "it"},
            "1.4.49": {"operation": "sangya", "domain": "it"},
            "1.4.102": {"operation": "sangya", "domain": "it"},
            "1.4.103": {"operation": "sangya", "domain": "it"},
        }
        for code, meta in ops.items():
            if code in self.rules:
                self.rules[code].operation = meta["operation"]
                self.rules[code].domain = meta.get("domain", self.rules[code].domain)

    def get(self, sutra: str) -> PaniniRule | None:
        return self.rules.get(sutra)

    def search(self, query: str) -> list[PaniniRule]:
        q = query.lower()
        hits = []
        for r in self.rules.values():
            if q in (r.iast or "").lower() or q in (r.hk or "").lower() or q in r.sutra:
                hits.append(r)
        return hits[:30]

    def expand_pratyahara(self, pid: str) -> list[str]:
        if pid not in self.pratyaharas:
            # allow bare marker style
            for p in self.pratyaharas.values():
                if p.get("id") == pid:
                    return list(p.get("result") or [])
            raise KeyError(pid)
        return list(self.pratyaharas[pid].get("result") or [])

    def members_of(self, pid: str) -> list[dict]:
        out = []
        for vid in self.expand_pratyahara(pid):
            v = self.varnas.get(vid)
            if v:
                out.append(v)
        return out

    def guna_map(self) -> dict[str, str]:
        """Zero/guna/vrddhi pairs from phoneme data (simplified teaching map)."""
        m = {}
        for v in self.varnas.values():
            if v.get("manner") != "vowel":
                continue
            z = v.get("id")
            if v.get("vowelGrade") == "zero" and v.get("gunaPair"):
                m[z] = v["gunaPair"]
            if v.get("vowelGrade") == "guna" and v.get("vrddhiPair"):
                m[z] = v["vrddhiPair"]
        return m

    def derive_guna(self, vowel_id: str) -> Derivation:
        """Demonstration derivation: apply guṇa mapping to a vowel.

        Full Aṣṭādhyāyī interaction is a research system; this runtime is a
        transparent teaching trace, not a claim of complete Paninian fidelity.
        """
        der = Derivation(input=[vowel_id])
        rule = self.get("1.1.2") or PaniniRule(sutra="1.1.2", iast="adeṅ guṇaḥ")
        gmap = self.guna_map()
        target = gmap.get(vowel_id)
        if not target:
            der.status = "no_guna_mapped"
            der.add(DerivationStep(
                before=[vowel_id],
                sutra=rule.sutra,
                rule=rule,
                after=[vowel_id],
                note=f"no teaching guṇa pair for {vowel_id}",
            ))
            return der
        der.add(DerivationStep(
            before=[vowel_id],
            sutra=rule.sutra,
            rule=rule,
            after=[target],
            note=f"teaching guṇa map {vowel_id}→{target}; source corpus: phonemes.json",
        ))
        der.status = "complete"
        return der

    def derive_parasmaipada_demo(self, dhatu: str = "gam") -> Derivation:
        """Illustrative derivation path for √gam (teaching trace).

        States are symbolic; rules cite sūtra numbers from corpus.
        Not a full computational Aṣṭādhyāyī.
        """
        steps_spec = [
            ("1.3.1", ["√" + dhatu], [f"{dhatu}-set"], "dhātu activated"),
            ("1.2.1", [f"{dhatu}-set"], [f"{dhatu}-set", "parasmaipada-lakāra"], "sārvadhātuka context (teaching)"),
            ("1.4.1", [f"{dhatu}-set", "parasmaipada-lakāra"], [f"{dhatu}-set", "laṭ"], "laṭ (present) as teaching placeholder"),
            ("1.3.3", [f"{dhatu}-set", "laṭ"], [f"{dhatu}-set", "laṭ", "hal-antya"], "hal-antya marked"),
        ]
        der = Derivation(input=["√" + dhatu])
        for code, before, after, note in steps_spec:
            rule = self.get(code) or PaniniRule(sutra=code, iast="(see corpus)")
            der.add(DerivationStep(before=before, sutra=code, rule=rule, after=after, note=note))
        # surface-ish placeholder
        surface = [f"{dhatu}+ti (surface placeholder — not full sangati)"]
        rule = self.get("1.2.1") or PaniniRule(sutra="1.2.1")
        der.add(DerivationStep(
            before=der.output,
            sutra="LAB-TEACHING",
            rule=rule,
            after=surface,
            note="surface placeholder; derivation TRACE is the knowledge object",
        ))
        der.status = "complete_teaching"
        return der

    def browse(self, adhyaya: str = "1.3", limit: int = 20) -> list[PaniniRule]:
        out = []
        for r in self.rules.values():
            if r.sutra.startswith(adhyaya + ".") or r.sutra.startswith(adhyaya):
                out.append(r)
                if len(out) >= limit:
                    break
        return out

    def summary(self) -> dict:
        ad = {}
        for code in self.rules:
            parts = code.split(".")
            key = parts[0] + "." + parts[1] if len(parts) >= 2 else parts[0]
            ad[key] = ad.get(key, 0) + 1
        return {
            "rules": len(self.rules),
            "with_iast": sum(1 for r in self.rules.values() if r.iast),
            "adhyaya_counts": dict(sorted(ad.items())[:40]),
            "pratyaharas": len(self.pratyaharas),
            "varnas": len(self.varnas),
            "corpus": {
                "vidyut": "sources/panini/vidyut/sutrapatha.tsv",
                "astadhyayi": "sources/panini/astadhyayi/sa_panini_astadhyayi.jsonl",
                "gretil": "sources/panini/gretil/",
            },
        }


def _demo() -> None:
    rt = PaniniRuntime()
    s = rt.summary()
    print("Pāṇini runtime")
    print(f"  rules={s['rules']} iast={s['with_iast']} pratyāhāra={s['pratyaharas']}")
    print(f"  sample 1.1.2 = {rt.get('1.1.2').iast if rt.get('1.1.2') else None}")
    print(f"  expand ac = {rt.expand_pratyahara('ac')}")
    print(f"  guna a→{rt.derive_guna('a').output}")
    d = rt.derive_parasmaipada_demo("gam")
    print(f"  √gam trace steps={len(d.steps)} status={d.status}")
    print(f"  search 'guṇa' hits={len(rt.search('guṇa'))}")


if __name__ == "__main__":
    _demo()
