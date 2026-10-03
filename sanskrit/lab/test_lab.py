"""Lab smoke tests — no network."""
from __future__ import annotations
import json
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent
sys.path.insert(0, str(LAB))
WORLDS = LAB.parent / "worlds"
sys.path.insert(0, str(WORLDS))

from worldir import build_varna_graph, load_pratyaharas, load_maheshvara
from panini_runtime import PaniniRuntime
from bruno_engine import build_default_engine
from notoria_session import NotoriaSession, run_daily


def test_worldir():
    g = build_varna_graph()
    assert len(g.nodes) > 30
    assert any(n.kind == "rule" for n in g.nodes.values())
    assert any(n.kind == "sound" for n in g.nodes.values())


def test_panini():
    rt = PaniniRuntime()
    assert rt.summary()["rules"] > 1000
    assert rt.get("1.1.2") and "guṇa" in (rt.get("1.1.2").iast or "").lower()
    assert "a" in rt.expand_pratyahara("ac")
    d = rt.derive_guna("a")
    assert d.output  # mapped or same
    d2 = rt.derive_parasmaipada_demo("gam")
    assert d2.status.startswith("complete")
    assert len(d2.steps) >= 3


def test_bruno():
    eng = build_default_engine()
    st = eng.status()
    assert st["lexicon_size"] >= 10
    assert st["seals"] == 30
    scene = eng.encode_varna_row("dentals")
    assert "ta" in scene.text or "series" in scene.text
    assert eng.seal_of(2) is not None
    assert eng.choose_operator("sequential") == "catena"


def test_notoria_session():
    out = run_daily("memory", "dentals")
    names = [s["name"] for s in out["steps"]]
    assert "intention" in names
    assert "install_series" in names
    assert "contractio" in names
    assert "log" in names
    assert out["engine"]["caelum_loci"] > 0


def test_doorway_json():
    p = LAB.parent / "worlds" / "stonedoorway-lab-session.json"
    assert p.exists()
    d = json.loads(p.read_text())
    assert d["name"] == "stonedoorway-lab-session"
    assert "voice_script" in d


def test_corpus():
    assert (LAB / "data" / "sutrapatha_merged.json").exists()
    assert (LAB.parent.parent / "sources" / "panini" / "vidyut" / "sutrapatha.tsv").exists()
    mah = load_maheshvara()
    pr = load_pratyaharas()
    assert len(mah) >= 1, f"mah empty {mah}"
    assert len(pr) >= 1, f"pr empty {pr}"


if __name__ == "__main__":
    fns = [v for k,v in list(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in fns:
        try:
            fn()
            print("OK", fn.__name__)
        except Exception as e:
            failed += 1
            print("FAIL", fn.__name__, type(e).__name__, e)
    sys.exit(1 if failed else 0)
