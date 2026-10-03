# Sanskrit-first — Pāṇini × Bruno × Notoria

> Decision: **Sanskrit first** (cognitive experiment), not Hindi.  
> Hindi becomes the **spoken layer later** (India / BHU) — not the machine you build first.  
> Platform: **`/root/sanskrithelp`** (`prx0r/sanskrithelp`) — already a Pāṇini-zone learning app.  
> Method shell: **Notoria** (`ochemapp/docs/NOTORIA-METHOD.md`)  
> Memory OS: **Bruno** (`/root/bruno`)

---

## Why Sanskrit first (locked)

| Reason | Detail |
|--------|--------|
| Subject is already a rule-machine | Pāṇini *Aṣṭādhyāyī* derives forms by ordered transformations |
| Bruno fit | “External knowledge as internal symbolic machine” — roots, wheels, sandhi gates |
| Notoria fit | Grammar special = liberal arts home turf |
| Platform fit | `sanskrithelp` already zones: pratyāhāras → phonemes → sandhi → dhātus → kārakas → verbs → compounds |
| Hindi later | Living speech in India; **don’t** force modern Hindi through full Sanskrit grammar |

**One line:** Sanskrit = construct the machine. Hindi = talk to people (after).

---

## Disk / clone status

| Item | Status |
|------|--------|
| Disk | **~99% full, ~1.5G free** — be careful; prefer shallow clones, no big audio dumps yet |
| Clone | `/root/sanskrithelp` (~99MB) — **done** (`prx0r/sanskrithelp`) |
| Other | `/root/finalbuilds2/acceptance/sanskrit_benchmark_lab`, `/root/patalacheckpoints/research/SANSKRIT-*.md` |

---

## Compatibility map — Bruno machine ↔ sanskrithelp zones

| Bruno / your essay | Zone in sanskrithelp | Component / data already there |
|--------------------|----------------------|--------------------------------|
| **Sound Hall** | 1–2 Pratyāhāras + Phoneme Grid | `data/pratyaharas.json`, `data/phonemes.json`, `app/learn/compression`, PhonemeGrid |
| **Root Forest** | 5 Dhātus | `data/dhatus.json`, DhātuDash games, `lib/games/dhatus.ts` |
| **Kāraka Temple / statues** | 8 Kārakas | `app/learn/karakas`, ParseSentence |
| **Vibhakti rooms** | nominal endings CSV | `data/nominal-endings-inflected.csv` |
| **Sandhi Gates** | 4 Sandhi | `data/sandhi-rules.json`, `lib/sandhi.ts`, SandhiDrill, SandhiForge |
| **Samāsa workshop** | 10 Compounds | Compound zone in tutor map |
| **Lakāra wheel** | 9 Verbs | `data/verb-endings.csv`, conjugation zone |
| **Derivation engine** | 7 Suffixes + rule context | `lib/derivation.ts`, `DerivationTree.tsx`, `RuleContext.tsx` |
| **Operate → gacchati** | Verbs + ParseSentence | DerivationTree + parse UI |

**Verdict: highly compatible.** You do **not** need a parallel Bruno app. Use sanskrithelp as the **Pāṇini machine UI**; Bruno is how you **visualize/operate** it; Notoria is the **session shell**.

---

## Architecture (keep products separate)

```text
ARS NOTORIA          session shell: general → nota → study → log
        ↓
PĀṆINI ZONES        sanskrithelp: pratyāhāras → … → compounds
        ↓
BRUNO SPATIAL        Sound Hall · Root Forest · Kāraka Temple
                     Sandhi Gates · Lakāra wheel · Samāsa bench
        ↓
SANSKRIT I/O         meaning → roles → roots → morphology → sandhi → form
        ↓
HINDI (later)        spoken layer: high-freq + listening + speaking
```

| Product | Role |
|---------|------|
| **sanskrithelp** | Pāṇini curriculum + drills + RAG tutor (your code) |
| **bruno repo** | Essays, Latin texts, volvelle, visual architecture notes |
| **Grimoirer** | Notoria PD text + witnesses (faculty shell) |
| **Stonedoorway** | Optional later: audio for deep study — **not** the Sanskrit OS |

---

## Sanskrit Track vs Pāṇini Track

| Track | Goal | Tools |
|-------|------|-------|
| **Sanskrit Track** | Read + generate simple sentences | sanskrithelp zones 2–6–9–10 + Whitney/Cambridge refs in INDEX |
| **Pāṇini Track** | Explain *why* forms occur | Zones 1–5–7–8 + rule context + Bruno diagrams |
| **Bruno overlay** | Internal spatial/symbolic machinery | Mental halls/gates/wheels + optional volvelle |
| **Notoria overlay** | Attention / memory / grammar general | 3×/week shell + nota = zone chart |

**Recommended linear path (from tutor map):**  
1 Pratyāhāras → 2 Phonemes → 3 Guṇa → 5 Dhātus → 9 Verbs → 4 Sandhi → 7 Suffixes → 8 Kārakas → 6 Words → 10 Compounds

---

## Month 1 plan (simple — don’t build the cathedral)

| Week | sanskrithelp zone | Bruno room | Notoria |
|------|-------------------|------------|---------|
| **1** | Pratyāhāras + Devanāgarī + pronunciation | **Sound Hall** | Memory general · nota = Śivasūtra chart |
| **2** | Nominal cases / first nouns | **Case Temple** (kārakas + vibhakti) | Understanding general |
| **3** | Dhātus + present tense | **Root Forest** + first **Lakāra wheel** | Memory + understanding |
| **4** | Basic sandhi | **Sandhi Gates** connecting Hall/Temple/Forest | Understanding · operate one derivation |

**Night walk:** mental tour Hall → Temple → Forest → Gates.  
**Operate, don’t recite:** √gam → present → 3sg → **gacchati** → change person/number → negate → sentence → case temple → sandhi gate.

---

## Session template (Sanskrit)

```
Subject: Sanskrit (Pāṇini machine)
Zone: ____________  (sanskrithelp)
Nota: ____________  (Śivasūtra chart / case table / root card / sandhi pair)

1. Notoria general (memory | understanding)     2 min
2. Look at nota                                 2 min
3. Zone drill in sanskrithelp                   20–25 min
   — operate one derivation / one sandhi / one kāraka
4. Bruno step: place it in Hall/Temple/Gate/Wheel
5. Log one line
```

---

## What we keep from Hindi plan

| Hindi plan piece | Sanskrit-first use |
|------------------|--------------------|
| Notoria method shell | **Keep unchanged** |
| 3×/week cadence | **Keep** |
| One special per 4-week block | Grammar/understanding for Sanskrit |
| Notae = tables/charts | Śivasūtras, case tables, root cards, sandhi pairs |
| Hindi 12 weeks | **Park** — resume as spoken layer when in India / after machine exists |
| India speaking goal | Still real — but **after** Sanskrit machine month 1 (or parallel light Hindi later) |

---

## sanskrithelp — what to run first

```bash
cd /root/sanskrithelp
# data already present:
#   data/pratyaharas.json  data/phonemes.json
#   data/dhatus.json       data/sandhi-rules.json
#   data/verb-endings.csv  data/nominal-endings-inflected.csv
ls data/ | head
# start Next app when disk/network allows
# npm install && npm run dev   (if node_modules needed — watch disk 1.5G free)
```

**Components to open first:**  
`components/DerivationTree.tsx` · `SandhiDrill.tsx` · `ParseSentence.tsx` · `PhonemeGrid.tsx` · `lib/derivation.ts` · `lib/sandhi.ts`

**Docs to read:**  
`docs/TUTOR_ZONE_OBJECTIVES_MAP.md` (10 zones) · `INDEX.md` (data files)

---

## Disk hygiene

| Do | Don’t |
|----|--------|
| Stay on zone data already in repo | Mass-download 55 phoneme audios yet |
| Shallow clones | Clone huge corpora without need |
| Prefer JSON already in `data/` | New 100MB+ models until machine works |

---

## Alignment with existing docs

| Doc | Change |
|-----|--------|
| `ochemapp/docs/NOTORIA-METHOD.md` | **Unchanged** — shell works for Sanskrit |
| `ochemapp/docs/HINDI-12-WEEK.md` | **Parked** as spoken layer; not the cognitive OS |
| `bruno/sanskrit/README.md` | Expanded by this file |
| `bruno/bruno.md` | Reading path still valid; add Sanskrit machine as first domain |

---

## Start this week

1. Open `/root/sanskrithelp` → Zone 1 Pratyāhāras + phonemes  
2. Notoria session 1: memory general + Śivasūtra nota + 20 min zone work  
3. Night: walk Sound Hall only (don’t build Temple yet)  
4. Week 3: plant Root Forest with √gam and **operate gacchati**  
5. Park Hindi speaking drills until machine feels stable (or 15-min light later)

**Sanskrit constructs the machine. Hindi talks to people. Notoria keeps you at the desk. Bruno makes the machine visible.**
