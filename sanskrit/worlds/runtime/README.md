# World runtimes (git-shareable)

Worlds are **protocol packages** — AI structure you shape + share.  
Practice stays **audial/imaginal** (no screen required).

| Package | World | Bed |
|---------|-------|-----|
| `sanskrit-matrika/` | Mātṛkā — install series | matrika_install |
| `sanskrit-laya/` | Laya — absorption | laya_silence |
| `sanskrit-panini/` | Pāṇini — grammar gates | grammar_machine |
| `memory-staged-tests/` | Memory — staged tests (guided) | memory_lab |

Each package:
- `world.json` — manifest, triggers, voice lines, work CLI
- `GUIDE.md` — what the AI says (human-readable)

**Shell docs:** `../../STONEDOORWAY-BOOTLOADER-WORLDRUNTIMES.md`  
**Beds map:** `../stonedoorway-world-beds.json`  
**Lobby:** `../stonedoorway-os-lobby.json`

```bash
# lab engine still works underneath
python3 /root/bruno/sanskrit/lab/daily_runtime.py session --faculty memory --series dentals
python3 /root/bruno/sanskrit/lab/daily_runtime.py doorway
```

To add a world: copy a package, edit `world.json` + `GUIDE.md`, commit.

**Tracks:** personal worlds (private) vs guided (`memory-staged-tests`) — keep separate.
