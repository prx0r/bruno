# Pāṭala Worlds — adjacent architecture

> Fourth surface: **WORLD** — internalize texts as executable mental models.  
> **Not inside OpenPāṭala.** Adjacent consumer of OpenPāṭala + Pāṭala + sanskrithelp + StoneDoorway.  
> Essay: `OPENPATALA-WORLD-STACK.md` · Date: 2026-10-03

---

## Stack (keep all four)

| Project | Responsibility |
|---------|----------------|
| **openpatala** (`/root/openpatala`) | Canonical reality: works, passages, editions, provenance |
| **patalacheckpoints** (`/root/patalacheckpoints`) | Meaning: SOURCE→L0→L2→C1→themes→**education compiler** |
| **sanskrithelp** (`/root/sanskrithelp`) | Language machine: phonemes, Pāṇini, Mātṛkā |
| **patalaworlds** *(new, adjacent)* | Internalization: sound, space, recitation, simulation, recall |
| **stonedoorway** (`/root/stoned`) | Experiential renderer: audio worlds, night journeys |
| **bruno** (`/root/bruno`) | Personal mnemonic architecture (source-attested vs scaffold) |

**Pipeline fork after commentary:**

```text
SOURCE → philology/translation → C1 → CONCEPT MODEL
    → WORLD COMPILER
    → EXPERIENCE (StoneDoorway)  +  SCHOLAR VIEW (OpenPāṭala/Pāṭala)
    → RECALL / REFLECTION → DEEPER TEXT
```

**Essays demoted** for personal path — research artifacts, not the main interface.

---

## Worlds ladder

| World | Content | Engine substrate |
|-------|---------|------------------|
| **0 Sound** | Phonemes, articulation, Devanāgarī, **Māheśvara Sūtras**, pratyāhāras | sanskrithelp zones 1–2 |
| **1 Language machine** | guṇa/vṛddhi, sandhi, roots, kārakas, sup/tiṅ | sanskrithelp zones 3–10 |
| **2 Śiva Sūtras (Vasugupta)** | Memorize + parse + conceptual geometry | new curriculum layer |
| **3 Spanda** | Short text, dense network | new |
| **4 Pratyabhijñā** | IPK → IPVV (patala golds) | patalacheckpoints |
| **5 Parātrīśikā** | Letters, mantra, vāk, anuttara, aham | bruno working copy + sanskrithelp |
| **6 Mālinīvijayottara** | Mātṛkā/Mālinī, varṇa, ritual topology | sanskrithelp tantra + volume |
| **N Tantrāloka** | All prior worlds interlock | OpenPāṭala passage graph |

**Pāṇini Māheśvara sūtras ≠ Vasugupta Śiva Sūtras** — both in World 0/2 for different reasons.

---

## Atomic unit: the phoneme object

```text
अ
  LINGUISTIC   Devanāgarī, IAST, audio, articulation, features
  PĀṆINIAN     Māheśvara location, pratyāhāras, rules
  MNEMONIC     your locus / image / felt association
  TRIKA         SOURCE-ATTESTED ONLY — Mātṛkā/Mālinī positions,
                metaphysics, mantric functions, body placement,
                colour/deity/tattva — each with source passage
```

**Do not** ship one synthetic chakra-color chart as “Abhinavagupta.” Store associations per practice/text. App: *“In this text: X. Elsewhere: Y.”*

---

## Embodied learning primitive

```text
HEAR → PRODUCE → FEEL WHERE IT FORMS → SEE → DRAW
→ LOCATE IN SOUND WORLD → LOCATE IN PĀṆINI
→ SOURCE-ATTESTED ASSOCIATIONS → CHANT/RECALL → RE-ENTER FROM MEMORY
```

Not “अ = a. Next card.”

**End-state vocabulary:** phonemes = geography · grammar = physics · roots = generative objects · sandhi = boundaries · kārakas = actor-relations · mantra = internalized sound-configs · texts = worlds.

---

## AI roles (StoneDoorway + Pāṭala)

| Role | Job |
|------|-----|
| **Narrator** | Sanskrit + translation + commentary |
| **World Master** | What appears/transforms/connects |
| **Socratic** | You perform the distinction |
| **Scholar** | Exact source/grammar/provenance on demand |

**Always** an EXPERIENCE ↔ SOURCE button. Immersive learning must not become pseudo-tradition.

---

## Text Initiation (compile when you pick a text)

```text
Prerequisites · Root Sanskrit · Grammar · Lexicon · Concepts
Geometry · Recitation · Checkpoints · Commentary · Parallels · Unlock
```

IPVV C1 types map cleanly:
**ARGUMENT**→argument-space · **RITUAL**→executable sequence · **MANTRA**→sound+structure · **COSMOLOGY**→geometry · **YOGA**→body-space+state · **DEITY/INITIATION**→guarded.

**Doc drift note:** trust artifacts/certificates over older prose counts (49 vs 63 L200/C1/T1).

---

## Bruno boundary (source vs mnemonic)

| Border | Meaning |
|--------|---------|
| **Gold** | Source-attested visualization |
| **Plain/ghost** | Your generated mnemonic scaffold |

Pāṭala: “Abhinavagupta says X.” StoneDoorway may compile X into chamber/route/color/machine.

---

## Day / Night modes (StoneDoorway)

| Mode | Content |
|------|---------|
| **DAY** | Study, grammar, recitation, derivation, source |
| **NIGHT** | Audio journey, walk world, recall, reconstruct, silence |

Atmosphere = **retrieval context**, not decoration.

---

## Metric

Not “lesson 12 complete.”

> **What exists in your internal world now that did not exist before?**

Checkpoints: recite · reconstruct grammar · explain without notes · navigate dependencies · attention experiment · text claim vs visualization · connect two passages.

---

## First build (don’t design Tantrāloka now)

1. **World 0** — phonemes + Māheśvara (sanskrithelp)  
2. Tiny **patalaworlds** schema: phoneme object + world card + day/night stub  
3. Optional StoneDoorway **Doorway** “Mātṛkā Night” (no Hz-per-phoneme claims)  
4. Consume OpenPāṭala/Pāṭala IDs read-only when World 2–4 arrive  

**Progression:** READ → UNDERSTAND → REPRESENT → EXPERIENCE → RECALL → RECOGNIZE ELSEWHERE.

---

## Repo map (proposed)

```
patalaworlds/                 # new adjacent (or bruno/sanskrit/worlds/)
  README.md
  architecture.md             # this file
  schema/
    phoneme.json              # multi-layer phoneme object
    world.json                # text world card
  worlds/
    w0-sound/ …
  consume:
    openpatala  (passages, provenance)
    patalacheckpoints (C1, education compiler)
    sanskrithelp (zones, Mātṛkā)
    stonedoorway (experience renderer)
    bruno (personal mnemonic only)
```
