# Sanskrit — Pāṇini × Bruno machine

> **First domain** for the Bruno memory OS. Hindi is the later spoken layer.  
> Full plan: [`SANSKRIT-FIRST.md`](./SANSKRIT-FIRST.md)  
> Platform: `/root/sanskrithelp` (`prx0r/sanskrithelp`)  
> Method: Notoria shell · Memory OS: Bruno

---

## Machine map (Bruno rooms ↔ sanskrithelp zones)

| Room | Zone | Operate |
|------|------|---------|
| **Sound Hall** | 1–2 Pratyāhāras + phonemes | Śivasūtras, pratyāhāras, pronunciation |
| **Root Forest** | 5 Dhātus | √gam → tree of forms |
| **Kāraka Temple** | 8 Kārakas + endings | agent/object/instrument as statues |
| **Sandhi Gates** | 4 Sandhi | forms meet, transform, emerge |
| **Lakāra wheel** | 9 Verbs | root × person × number × voice × tense → form |
| **Samāsa workshop** | 10 Compounds | many objects → one object |
| **Derivation engine** | 7 Suffixes | prefixes/kṛt/taddhita as machinery |

---

## Five-ring wheel (Bruno)

```text
RING 1 — ROOT        √gam  √bhū  √kṛ  √dṛś  √vad
RING 2 — PERSON      aham  tvam  saḥ  vayam
RING 3 — TENSE/MOOD  present imperfect future imperative
RING 4 — VOICE       parasmaipada  ātmanepada
RING 5 — CONTEXT     home teacher river temple book
```

**Operate:** ROOT × PERSON × TENSE × VOICE → produce form → walk through sandhi gate.

Tool: clone `tools/volvelle` from bruno repo (see `/root/bruno/tools/README.md`).

---

## Pāṇinian cases as Lampas statues

| Kāraka | Role | Statue note |
|--------|------|-------------|
| **kartṛ** | agent | carries out |
| **karman** | object | undergoes |
| **karaṇa** | instrument | tools in hand |
| **sampradāna** | recipient | receives |
| **apādāna** | source | separates |
| **adhikaraṇa** | location | the room itself |

---

## Two tracks

1. **Sanskrit** — read/generate simple sentences (sanskrithelp zones)  
2. **Pāṇini** — explain why forms occur (pratyāhāras, rules, derivation)  

**Bruno** = spatial/symbolic machinery. **Notoria** = attention shell. **Don’t** memorize ~4,000 sūtras day one.

---

## Month 1

| Week | Focus | Room |
|------|--------|------|
| 1 | Sounds, Devanāgarī, Śivasūtras | Sound Hall |
| 2 | Nouns + cases | Case Temple |
| 3 | Roots + present tense | Root Forest + wheel |
| 4 | Basic sandhi | Sandhi Gates |

Operate **gacchati** in week 3. Night: mental walk.

---

## Sanskrit vs Hindi

| | Sanskrit | Hindi |
|--|----------|-------|
| Role | Cognitive architecture / machine | Spoken life in India |
| When | **Now** | After machine (or light parallel later) |
| Method | Pāṇini zones + Bruno rooms | High-freq + listening + speaking |
| Don’t | Force full grammar onto Hindi | Force Hindi through full Pāṇini |

---

## Session shell (Notoria)

1. General (memory | understanding)  
2. Nota = zone chart  
3. Drill in sanskrithelp  
4. Bruno step: place in Hall/Temple/Gate/Wheel  
5. One-line log  

See `SANSKRIT-FIRST.md` and ochemapp `NOTORIA-METHOD.md`.

---

## Data already in sanskrithelp

`data/pratyaharas.json` · `phonemes.json` · `dhatus.json` · `sandhi-rules.json` · `verb-endings.csv` · `nominal-endings-inflected.csv`

Components: DerivationTree · SandhiDrill · ParseSentence · PhonemeGrid · lib/derivation · lib/sandhi

---

## Full synthesis

**Pāṇini Palace × Ars Notoria × Tantraloka:** [`PANINI-PALACE-NOTORIA-TANTRALOKA.md`](./PANINI-PALACE-NOTORIA-TANTRALOKA.md)

- Palace that **behaves like** Pāṇini (executable zones)
- Notoria = faculty + Grammar notae I–III → morphology / kārakas / sandhi+samāsa
- Bruno = execution traces (location/agent/action/condition/output)
- Tantraloka = Sound Gate depth (50 varṇas, 4 speech levels, mātṛkā)
- Local stack: `/root/sanskrithelp` + volume tantraloka project

---

## Deeper synthesis (Abhinavagupta / vāk)

**Word-for-word essay:** [`PANINI-ABHINAVAGUPTA-SYNTHESIS.md`](./PANINI-ABHINAVAGUPTA-SYNTHESIS.md)

- Pāṇini = generation · Abhinavagupta = what sound IS · Bruno = internal machine · Notoria = preparation  
- Best next text: **Parātrīśikā-vivaraṇa** + **Tantrāloka III** (III.232–233)  
- Dual-view phonemes · four floors of speech · Mātṛkā vs Mālinī paths · word/grammar/mantric levels  
- Three maps: mouth + body (non-ritual) + Brunian space  

---

## World geometry (deepest formulation)

**Word-for-word:** [`WORLD-GEOMETRY-SANSKRIT.md`](./WORLD-GEOMETRY-SANSKRIT.md)

- Preferred edition: Singh / Bäumer / Lakshman Joo (Motilal Banarsidass) — better than full Tantrāloka first  
- Four layers: phonetic geometry · Pāṇini physics · Bruno topology · Trika vertical axis (parā→vaikharī)  
- Modes: Pāṇini · Trika · Bruno · Notoria  
- Tiny first structure: ANUTTARA → AHAM → phonemes → grammar → speech  
- End-state: internal symbolic environment to think Sanskrit philosophy from inside its categories  

---

## Build structures (implementable)

**[`BUILD-STRUCTURES.md`](./BUILD-STRUCTURES.md)** — web-researched stack:

| Layer | Steal from |
|-------|------------|
| Prakriyā engine | Vidyut / Padmini |
| Sandhi gates | Lakshmanan ontology + buda-base sandhi-engine |
| Parse pipeline | kmadathil/sanskrit_parser Level 0–3 |
| Spatial palace | GraphPalace Wing/Room/Drawer + KG |
| Executable knowledge | PM-KR (W3C CG) |
| Sanskrit KG | Terdalkar thesis / Sangrahaka |
| Trika depth | sanskrithelp tantra + Parātrīśikā working copy |

**Start:** palace JSON schema + dual-view phonemes + one TRACE.

---

## Adjacent project: Sanskrit Worlds

**[`SANSKRIT-WORLDS-PROJECT.md`](./SANSKRIT-WORLDS-PROJECT.md)**

- Embodied AI learning: chant phonemes + form + color + emotion → text-as-world
- Curriculum: Śivasūtras → sandhi → verbs → Parātrīśikā/IPVV → Tantrāloka
- Reuses: Pāṭala corpus IDs + education compiler (adjacent, not merged)
- Mātṛkā practice from `tantrica2.md` + tattvas colors
- Anti-theatre: track sessions/recall/passage walks

---

## Night phoneme track × Abhinavagupta science

**[`NIGHT-PHONEME-TRACK.md`](./NIGHT-PHONEME-TRACK.md)**

- Abhinavagupta: phonemes-as-awareness, Mātṛkā/Mālinī, 4 speech levels, dvādaśānta, color/body placement
- **No Hz-per-phoneme table in the texts** — binaural = modern bed overlay
- Volume: science thesis, platinum sound-matrix packs, Āhnika texts, ROs
- Night: Stonedoorway bed + spoken phonemes + tantrica2 color map + Notoria shell

---

## Pāṭala Worlds stack

**Essay:** [`OPENPATALA-WORLD-STACK.md`](./OPENPATALA-WORLD-STACK.md)  
**Architecture:** [`PATALAWORLDS-ARCHITECTURE.md`](./PATALAWORLDS-ARCHITECTURE.md)

- OpenPāṭala = canonical reality · Pāṭala = meaning/translation · Education → **WORLD** (internalize)
- Adjacent project: **patalaworlds** — not inside OpenPāṭala
- StoneDoorway = experiential renderer (day study / night journey)
- Essays demoted; experience → recall → recognize elsewhere
- Worlds ladder: Sound → Language machine → Śiva Sūtras → Spanda → Pratyabhijñā/IPVV → Parātrīśikā → Mālinīvijayottara → Tantrāloka
- Phoneme = atomic multi-layer object (linguistic + Pāṇinian + mnemonic + source-attested Trika)
- AI: narrator · world master · socratic · scholar (EXPERIENCE ↔ SOURCE)

---

## Colors · frequencies · Fuller

**[`COLORS-FREQUENCIES-FULLER.md`](./COLORS-FREQUENCIES-FULLER.md)**

- Color table = **study scaffold** (tantrica2) + source tags — not one universal Abhinavagupta chart
- Hz-per-chakra = modern contested overlay; voice mantra is the traditional path
- Volume: tetrahedron notes, science thesis (speculative), platinum sound packs
- Fuller: geometry/systems/monuments — **“frequency” = structure, not audio Hz**
- Cymatics: sound↔geometry in matter — analogy, not chakra-Hz proof

---

## Laya Yoga × Mātṛkā

**[`LAYA-YOGA-MATRIKA.md`](./LAYA-YOGA-MATRIKA.md)**

- Laya = **absorption** (not destruction) → bindu → recoil into daily life
- **Mantra = Kuṇḍalinī in sound-form** · Mātṛkā phonemes = tattva/bīja machine
- Fits four layers: Notoria shell → Mātṛkā install → **Laya absorb** → Pāṇini/Abhinavagupta
- Night = absorption (chant→mental→silence); morning = recoil (speak the language)
- Volume: `36-tattvas-sanskrit-layayoga.md` · sanskrithelp ROs + `layayoga.txt`
- Optional advanced: SAUḤ (emission) / KHPHREṀ (withdrawal)

---

## Convergence: Sanskrit lab in the head

**[`CONVERGENCE-SANSKRIT-LAB.md`](./CONVERGENCE-SANSKRIT-LAB.md)**

- Stacks converge: StoneDoorway ↔ Notoria ↔ Mātṛkā ↔ **Laya** ↔ Tantrāloka ↔ Pāṇini ↔ Bruno
- StoneDoorway = door into the lab (chanting, breath, VB optional, night journeys) — not replaced
- **Sanskrit lab** = living internal laboratory (sound bench → absorption → grammar machine → text worlds → residents → monuments)
- Bruno *Ars reminiscendi* downloaded: `texts/bruno_ars_reminiscenti.html`
- Tonight: install row → laya silence → speak one word → log
