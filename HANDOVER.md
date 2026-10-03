# HANDOVER — Bruno / Sanskrit Lab / StoneDoorway OS

> **Repo:** `/root/bruno`  
> **Date:** 2026-10-03  
> **Owner work:** computational Sanskrit lab + imagination OS on top of Castle Notoria + Bruno + Pāṇini  
> **Gurdjieff:** **not used** in active stack (sigil/process notes archived only)

---

## 1. What this repo is today

A **Sanskrit lab runtime + StoneDoorway imagination OS design**, wired to:

| Layer | Role | Status |
|-------|------|--------|
| **Castle Ars Notoria** | Faculty shell — memory · intellect · eloquence · understanding; method of places; notae as rooms | **Bible / core** |
| **Bruno** | Imaginal runtime — LOCUS · IMAGO · VINCULUM · Caelum · 30 seals · wheels (encode/explore) | **Core** |
| **Pāṇini** | Transformation runtime — 3983 sūtras · pratyāhāra · teaching derivation traces | **Core** |
| **Trika / Abhinavagupta** | Content layer — uccāra · contractio · bindu (docs + practice schema) | Content (not full engine) |
| **StoneDoorway** | Audial imagination OS — doorway · lobby · beds · world runtimes | **Design + packages live** |
| **Gurdjieff** | — | **Not in active stack** |

**Not in this repo as product:** Grimoirer (reader) lives in `/root/ochemapp`.  
**Private study corpus** (copyrighted PDFs) on disk, gitignored.

---

## 2. Day map (what we built today)

### A. Practice foundation
| Artifact | Path |
|----------|------|
| Step 1 plan | `sanskrit/STEP1-DEVANAGARI.md` |
| Devanagari chart | `sanskrit/worlds/step1-devanagari-chart.html` |
| Phoneme practice player | `sanskrit/worlds/step1-phoneme-practice.html` |
| Laya × Mātṛkā deep dive | `sanskrit/LAYA-YOGA-MATRIKA.md` |

Player URL (docs server): `http://127.0.0.1:8820/step1-phoneme-practice.html`  
Audio copied to ochemapp docs: `/phenetics/*.ogg`

### B. Convergence + visions
| Artifact | Path |
|----------|------|
| Sanskrit lab convergence | `sanskrit/CONVERGENCE-SANSKRIT-LAB.md` |
| Visions (endgame) | `sanskrit/VISONS.md` |
| Bruno stack v2 (imagination tech) | `sanskrit/BRUNO-STACK-V2.md` |
| Wheels + imaginal compiler (verbatim) | `sanskrit/BRUNO-WHEELS-IMAGINAL-COMPILER.md` |
| Greer/provenance/Bruno→Pāṇini (verbatim) | `sanskrit/GREER-PROVENANCE-BRUNO-PANINI.md` |
| Bruno methods forum (verbatim) | `sanskrit/BRUNO-METHODS-FORUM-places-images.md` |

### C. Castle + corpus
| Artifact | Path |
|----------|------|
| **Castle fit (canonical)** | `sanskrit/CASTLE-ARS-NOTORIA-FIT.md` |
| Castle PDF | `sources/private/castle-ars-notoria.pdf` |
| R2 imports (9 files) | `sources/private/` + `IMPORT_MANIFEST.json` |
| Ars Reminiscendi HTML | `texts/bruno_ars_reminiscenti.html` |
| Thirty Seals inventory | `sanskrit/worlds/triginta-sigilli-inventory.json` |

**Private sources imported today (R2 `r2a:uploads`):**
- castle-ars-notoria.pdf
- bruno-on-the-composition.pdf
- rankine-claves-intelligentiarum.pdf
- bruno-cause-principle-unity.pdf
- leitch-magickal-grimoires.pdf
- dunn-orphic-hymns.epub
- art-of-memory-transformed.docx
- bruno.pdf
- morebruno.pdf  

**Policy:** private study only — not public grimoirer without rights check.

### D. Pāṇini corpus + computational lab
| Artifact | Path |
|----------|------|
| Corpus README | `sources/panini/README.md` |
| Vidyut sutrapatha (3983) | `sources/panini/vidyut/sutrapatha.tsv` |
| GRETIL astadhyayi JSONL | `sources/panini/astadhyayi/sa_panini_astadhyayi.jsonl` |
| GRETIL HTML | `sources/panini/gretil/` |
| Lab data (merged sutras, varnas, pratyāhāras) | `sanskrit/lab/data/` |
| **Lab README** | `sanskrit/lab/README.md` |
| WorldIR | `sanskrit/lab/worldir.py` |
| Bruno engine | `sanskrit/lab/bruno_engine.py` |
| Pāṇini runtime | `sanskrit/lab/panini_runtime.py` |
| Notoria session shell | `sanskrit/lab/notoria_session.py` |
| Daily CLI | `sanskrit/lab/daily_runtime.py` |
| Tests | `sanskrit/lab/test_lab.py` (**6/6 green**) |

**Bruno primitives (pre-lab):** `sanskrit/worlds/bruno_primitives.py` (Caelum/Catena/Arbor).

### E. StoneDoorway OS (audial)
| Artifact | Path |
|----------|------|
| OS imagination design | `sanskrit/STONEDOORWAY-OS-IMAGINATION.md` |
| Audial OS (no screen) | `sanskrit/STONEDOORWAY-AUDIAL-OS.md` |
| Bootloader + world runtimes | `sanskrit/STONEDOORWAY-BOOTLOADER-WORLDRUNTIMES.md` |
| Personal + memory tests | `sanskrit/STONEDOORWAY-PERSONAL-AND-MEMORY.md` |
| Lobby JSON | `sanskrit/worlds/stonedoorway-os-lobby.json` |
| Lab session JSON | `sanskrit/worlds/stonedoorway-lab-session.json` |
| World beds map | `sanskrit/worlds/stonedoorway-world-beds.json` |
| Runtime packages | `sanskrit/worlds/runtime/` |

**World packages:**
```
worlds/runtime/
  sanskrit-matrika/     world.json + GUIDE.md
  sanskrit-laya/        world.json + GUIDE.md
  sanskrit-panini/      world.json + GUIDE.md
  memory-staged-tests/  world.json + GUIDE.md
```

**Sigil:** Gurdjieff Enneagram *was* discussed as process symbol; **owner: not needed in active stack.** Lobby currently may still mention it — treat as **optional brand glyph only**, not a load-bearing theory.

---

## 3. Canonical stack (use this)

```text
CASTLE NOTORIA BIBLE
  faculty shell · method of places · notae rooms · Abbreviata ethic
        ↓
BRUNO RUNTIME
  LOCUS · IMAGO · VINCULUM · Caelum · seals · wheels
        ↓
PĀṆINI RUNTIME
  sūtra corpus · pratyāhāra · teaching derivations
        ↓
TRIKA (content)
  uccāra · contractio · Laya bindu · colour scaffold (labelled pedagogical)
        ↓
STONE DOORWAY OS
  audial bootloader · lobby · beds · git world packages
```

**Practice protocol (daily):**
```text
intention (faculty)
→ Castle figure hub
→ install matrika series into Caelum
→ contractio
→ Laya silence
→ Pāṇini mini (pratyāhāra | sūtra | √gam)
→ speak recoil
→ log
```

**StoneDoorway boot:**
```text
threshold → "Remember yourself" (presence cue — not Gurdjieff doctrine)
→ reconstruct lobby → walk window → bed on → work → return
```

---

## 4. How to run

```bash
cd /root/bruno/sanskrit/lab
python3 test_lab.py
python3 daily_runtime.py status
python3 daily_runtime.py session --faculty memory --series dentals
python3 daily_runtime.py session --faculty intellect --series gutturals
python3 daily_runtime.py panini --sutra 1.1.2
python3 daily_runtime.py panini --pratyahara ac
python3 daily_runtime.py panini --derive gam
python3 daily_runtime.py encode --series dentals
python3 daily_runtime.py explore --n 3
python3 daily_runtime.py doorway
```

**Practice player (if docs server up):**
- Chart: `http://127.0.0.1:8820/step1-devanagari-chart.html`
- Audio player: `http://127.0.0.1:8820/step1-phoneme-practice.html`

---

## 5. Honesty / product boundaries

| Rule | Detail |
|------|--------|
| Castle = bible | Faculty shell + places — not Goetic conjuration |
| Colors / loci | Pedagogical unless `sourceAttested` |
| Derivations | Teaching traces over real corpus — not full Aṣṭādhyāyī engine |
| Voces magicae ≠ Sanskrit bījas | Sacred sound form family only |
| Private PDFs | Disk only; gitignore binaries |
| Grimoirer | Separate product (`/root/ochemapp`) |
| Gurdjieff | **Not required** for this stack |
| Familiar | Mnemonic companion / voice cue — not claimed external entity |

---

## 6. Key files (quick index)

```
bruno/
  HANDOVER.md                 ← you are here
  README.md
  AGENTS.md                   (if present)
  sources/
    private/                  Castle + 9 R2 imports + manifest
    panini/                   Vidyut + GRETIL + astadhyayi
  sanskrit/
    README.md                 index
    CASTLE-ARS-NOTORIA-FIT.md bible fit
    BRUNO-STACK-V2.md
    STEP1-DEVANAGARI.md
    LAYA-YOGA-MATRIKA.md
    STONEDOORWAY-*.md
    lab/                      runtime + tests + data
    worlds/
      bruno_primitives.py
      triginta-sigilli-inventory.json
      step1-*.html
      stonedoorway-*.json
      runtime/                world packages
  texts/
    bruno_ars_reminiscenti.html
    ea_*.html, ia_*.pdf, warburg_*.pdf, paratrisika...
```

---

## 7. Git history (today, high level)

Approximate order (see `git log`):
1. Step 1 chart + plan + phoneme player  
2. Bruno stack v2 + 30 seals + Caelum runtime  
3. Visions + Laya/Mātṛkā (earlier thread)  
4. R2 import 9 books + Greer/provenance freeze  
5. Wheels/imaginal compiler + Bruno methods forum  
6. Castle fit + Notoria bible affirmation  
7. Pāṇini corpus + computational lab + tests  
8. StoneDoorway OS (audial, lobby, world runtimes, memory tests)  
9. Gurdjieff notes → **owner: not needed** (active stack without it)

---

## 8. Next steps (recommended)

| Priority | Task |
|----------|------|
| 1 | **Personal practice:** daily `session --faculty memory --series dentals` + Step 1 player |
| 2 | Fill more world packages (text-worlds, familiar room) |
| 3 | Optional: lobby HTML — **not required** (practice is audial) |
| 4 | Optional: TTS Guide voice boot later |
| 5 | When Greer De umbris available → provenance ladder (Sturlese / Gosnell / Greer / ours) |
| 6 | Keep Gurdjieff **out** unless owner reopens |

---

## 9. One-line handover

> **Castle is the Notoria bible. Bruno is the imaginal machine. Pāṇini is the grammar runtime. StoneDoorway is the audial OS shell with git world packages. Run `daily_runtime.py`, install one matrika row, speak one word, log — that’s the system.**
