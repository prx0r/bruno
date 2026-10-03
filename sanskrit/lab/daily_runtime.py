#!/usr/bin/env python3
"""Daily runtime CLI — Sanskrit lab in the head.

Usage:
  python3 daily_runtime.py status
  python3 daily_runtime.py session --faculty memory --series dentals
  python3 daily_runtime.py encode --series gutturals
  python3 daily_runtime.py explore --wheel varna_series --n 3
  python3 daily_runtime.py panini --search guṇa
  python3 daily_runtime.py panini --sutra 1.1.2
  python3 daily_runtime.py panini --pratyahara ac
  python3 daily_runtime.py panini --derive gam
  python3 daily_runtime.py install --series labials
  python3 daily_runtime.py doorway
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bruno_engine import build_default_engine
from notoria_session import FACULTIES, NotoriaSession, run_daily
from panini_runtime import PaniniRuntime
from worldir import build_varna_graph


def cmd_status() -> None:
    eng = build_default_engine()
    pan = PaniniRuntime()
    g = build_varna_graph()
    print("SANSKRIT LAB — daily runtime")
    print(f"  BrunoEngine: {json.dumps(eng.status())}")
    print(f"  Pāṇini: rules={pan.summary()['rules']} pratyāhāra={pan.summary()['pratyaharas']}")
    print(f"  WorldIR nodes: {len(g.nodes)}")
    print(f"  Faculties: {', '.join(FACULTIES)}")
    print("  Protocol: intention → figure hub → install row → contractio → (Pāṇini) → speak → log")


def cmd_session(args: argparse.Namespace) -> None:
    out = run_daily(args.faculty, args.series)
    print(json.dumps({
        "faculty": out["faculty"],
        "series": out["series"],
        "n_steps": len(out["steps"]),
        "steps": [s["name"] for s in out["steps"]],
        "scene": next((s.get("scene") for s in out["steps"] if s["name"] == "install_series"), None),
        "engine": out["engine"],
    }, indent=2, ensure_ascii=False))


def cmd_encode(args: argparse.Namespace) -> None:
    eng = build_default_engine()
    scene = eng.encode_varna_row(args.series)
    print(json.dumps(scene.to_dict(), indent=2, ensure_ascii=False))


def cmd_explore(args: argparse.Namespace) -> None:
    eng = build_default_engine()
    scenes = eng.explore(args.wheel, n=args.n, seed=args.seed)
    print(json.dumps([s.to_dict() for s in scenes], indent=2, ensure_ascii=False))


def cmd_install(args: argparse.Namespace) -> None:
    eng = build_default_engine()
    export = eng.caelum_install_matrika(args.series)
    print(json.dumps({
        "series": args.series,
        "n_loci": export["n_loci"],
        "sample": export["loci"][:8],
    }, indent=2, ensure_ascii=False))


def cmd_panini(args: argparse.Namespace) -> None:
    pan = PaniniRuntime()
    if args.search:
        hits = pan.search(args.search)
        print(json.dumps([h.to_dict() for h in hits], indent=2, ensure_ascii=False))
    elif args.sutra:
        r = pan.get(args.sutra)
        print(json.dumps(r.to_dict() if r else {"error": "not found", "sutra": args.sutra}, indent=2, ensure_ascii=False))
    elif args.pratyahara:
        print(json.dumps({
            "id": args.pratyahara,
            "expands": pan.expand_pratyahara(args.pratyahara),
            "members": pan.members_of(args.pratyahara),
        }, indent=2, ensure_ascii=False))
    elif args.derive:
        d = pan.derive_parasmaipada_demo(args.derive)
        print(json.dumps(d.to_dict(), indent=2, ensure_ascii=False))
    elif args.guna:
        d = pan.derive_guna(args.guna)
        print(json.dumps(d.to_dict(), indent=2, ensure_ascii=False))
    else:
        print(json.dumps(pan.summary(), indent=2, ensure_ascii=False))


def cmd_doorway() -> None:
    worlds = Path(__file__).resolve().parent.parent / "worlds"
    for name in ("stonedoorway-os-lobby.json", "stonedoorway-lab-session.json"):
        p = worlds / name
        if p.exists():
            print(p.read_text())
            if name.endswith("os-lobby.json"):
                print("\n--- also: sanskrit/STONEDOORWAY-OS-IMAGINATION.md ---")
            return
    print(json.dumps({"error": "doorway files missing", "dir": str(worlds)}))


def main() -> None:
    ap = argparse.ArgumentParser(description="Sanskrit lab daily runtime")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status")
    p = sub.add_parser("session")
    p.add_argument("--faculty", default="memory", choices=sorted(FACULTIES))
    p.add_argument("--series", default="dentals", choices=["dentals", "gutturals", "labials"])
    p = sub.add_parser("encode")
    p.add_argument("--series", default="dentals")
    p = sub.add_parser("explore")
    p.add_argument("--wheel", default="varna_series")
    p.add_argument("--n", type=int, default=3)
    p.add_argument("--seed", type=int, default=42)
    p = sub.add_parser("install")
    p.add_argument("--series", default="dentals")
    p = sub.add_parser("panini")
    p.add_argument("--search")
    p.add_argument("--sutra")
    p.add_argument("--pratyahara")
    p.add_argument("--derive")
    p.add_argument("--guna")
    sub.add_parser("doorway")

    args = ap.parse_args()
    if args.cmd == "status":
        cmd_status()
    elif args.cmd == "session":
        cmd_session(args)
    elif args.cmd == "encode":
        cmd_encode(args)
    elif args.cmd == "explore":
        cmd_explore(args)
    elif args.cmd == "install":
        cmd_install(args)
    elif args.cmd == "panini":
        cmd_panini(args)
    elif args.cmd == "doorway":
        cmd_doorway()


if __name__ == "__main__":
    main()
