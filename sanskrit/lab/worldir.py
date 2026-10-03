"""WorldIR — neutral knowledge graph + Varna atom (Bruno/Pāṇini/Trika).

knowledge ≠ representation.
"""
from __future__ import annotations

import json
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

LAB = Path(__file__).resolve().parent
DATA = LAB / "data"


def nid(prefix: str = "n") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@dataclass
class SourceAssertion:
    claim: str
    source: str
    kind: str = "pedagogicalInvention"  # sourceAttested | pedagogicalInvention
    locator: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Representation:
    modality: str  # semantic | grammatical | imaginal | embodied | audio | visual | spatial
    payload: dict
    provenance: SourceAssertion | None = None
    label: str = ""

    def to_dict(self) -> dict:
        d = {
            "modality": self.modality,
            "payload": self.payload,
            "label": self.label,
        }
        if self.provenance:
            d["provenance"] = self.provenance.to_dict()
        return d


@dataclass
class KnowledgeNode:
    id: str
    kind: str
    label: str
    relations: list[dict] = field(default_factory=list)
    provenance: list[SourceAssertion] = field(default_factory=list)
    representations: list[Representation] = field(default_factory=list)
    learner_state: dict = field(default_factory=dict)

    def relate(self, kind: str, other_id: str, meta: dict | None = None) -> None:
        self.relations.append({"kind": kind, "target": other_id, "meta": meta or {}})

    def add_assertion(self, a: SourceAssertion) -> None:
        self.provenance.append(a)

    def add_repr(self, r: Representation) -> None:
        self.representations.append(r)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "kind": self.kind,
            "label": self.label,
            "relations": self.relations,
            "provenance": [p.to_dict() for p in self.provenance],
            "representations": [r.to_dict() for r in self.representations],
            "learner_state": self.learner_state,
        }


@dataclass
class KnowledgeGraph:
    name: str
    nodes: dict[str, KnowledgeNode] = field(default_factory=dict)

    def add(self, node: KnowledgeNode) -> KnowledgeNode:
        self.nodes[node.id] = node
        return node

    def get(self, id: str) -> KnowledgeNode:
        return self.nodes[id]

    def by_kind(self, kind: str) -> list[KnowledgeNode]:
        return [n for n in self.nodes.values() if n.kind == kind]

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "n": len(self.nodes),
            "nodes": [n.to_dict() for n in self.nodes.values()],
        }

    def save(self, path: Path | str) -> None:
        Path(path).write_text(json.dumps(self.to_dict(), ensure_ascii=False, indent=2))


def load_varnas() -> list[dict]:
    raw = json.loads((DATA / "varnas.json").read_text())
    return raw["items"]


def load_pratyaharas() -> list[dict]:
    raw = json.loads((DATA / "pratyaharas.json").read_text())
    return raw["items"]


def load_maheshvara() -> list[dict]:
    raw = json.loads((DATA / "maheshvara_sutras.json").read_text())
    return raw["suras"]


def build_varna_graph() -> KnowledgeGraph:
    """Universal atom: one Sound/Symbol/Pāṇini/Trika/Bruno/Personal object each."""
    g = KnowledgeGraph(name="varna-atoms")
    for v in load_varnas():
        vid = f"varna_{v['id']}"
        node = KnowledgeNode(
            id=vid,
            kind="sound",
            label=f"{v.get('devanagari','')} {v.get('iast','')}",
            learner_state={"status": "uninstalled"},
        )
        node.add_repr(Representation("grammatical", {
            "devanagari": v.get("devanagari"),
            "iast": v.get("iast"),
            "manner": v.get("manner"),
            "place": v.get("place"),
            "kind": v.get("kind"),
            "pratyaharas": v.get("pratyaharas"),
            "gunaPair": v.get("gunaPair"),
            "vrddhiPair": v.get("vrddhiPair"),
            "vowelGrade": v.get("vowelGrade"),
        }, label="panini-phonetics"))
        node.add_repr(Representation("audio", {
            "file": v.get("audioFile"),
        }, label="local-ogg"))
        node.add_repr(Representation("visual", {
            "devanagari": v.get("devanagari"),
            "colorScaffold": v.get("colorScaffold"),
        }, provenance=SourceAssertion(
            claim="color is study scaffold not classical doctrine",
            source="tantrica2",
            kind="pedagogicalInvention",
        ), label="devanagari+color"))
        node.add_repr(Representation("spatial", {
            "caelum_hint": v.get("place") or "other",
            "series": v.get("place"),
        }, provenance=SourceAssertion(
            claim="caelum series mapping is lab pedagogy",
            source="bruno_stack_v2",
            kind="pedagogicalInvention",
        ), label="series-region"))
        for p in v.get("pratyaharas") or []:
            node.relate("member_of_pratyahara", f"pratyahara_{p}")
        g.add(node)
    for p in load_pratyaharas():
        pid = f"pratyahara_{p['id']}"
        node = KnowledgeNode(id=pid, kind="rule", label=f"pratyāhāra {p['id']}")
        node.add_repr(Representation("grammatical", {
            "id": p.get("id"),
            "sura": p.get("sura"),
            "marker": p.get("marker"),
            "result": p.get("result"),
            "explanation": p.get("explanation"),
        }, provenance=SourceAssertion(
            claim="pratyahara expansion",
            source="Māheśvara + Pāṇini convention / sanskrithelp",
            kind="sourceAttested",
        ), label="expansion"))
        for r in p.get("result") or []:
            # map iast-ish ids to varna nodes when possible
            node.relate("expands_to", f"varna_{r}")
        g.add(node)
    return g


if __name__ == "__main__":
    g = build_varna_graph()
    out = LAB / "worldir_varna.json"
    g.save(out)
    print(f"WorldIR: {len(g.nodes)} nodes -> {out}")
    print("kinds", {k: len(g.by_kind(k)) for k in ["sound", "rule"]})
