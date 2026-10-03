# sanskrithelp compatibility (prx0r/sanskrithelp)

Cloned 2026-10-03 → `/root/sanskrithelp` (~99MB). Disk: ~1.5G free (99% used).

## What it already is
Full-stack Sanskrit learning platform (Next.js + zones + RAG tutor + games).

## Zone DAG (from TUTOR_ZONE_OBJECTIVES_MAP.md)
1 Pratyāhāras → 2 Phonemes → 3 Guṇa → 4 Sandhi → 5 Dhātus → 6 Words → 7 Suffixes → 8 Kārakas → 9 Verbs → 10 Compounds → 11 Reading

Recommended path: 1→2→3→5→9→4→7→8→6→10

## Data on disk
- pratyaharas.json, phonemes.json, dhatus.json, sandhi-rules.json
- verb-endings.csv, nominal-endings-inflected.csv, nouns-irregular-inflected.csv
- rag/ (Whitney/Pāṇini/Dhātupāṭha/MW embeddings plan)

## Components
DerivationTree, SandhiDrill, ParseSentence, PhonemeGrid, RuleContext, GunaDrill, DhātuDash games, SandhiForge, etc.

## Mapping
Bruno rooms ↔ zones — see ../sanskrit/SANSKRIT-FIRST.md

## Not in this clone yet
- Full phoneme audio (1/55 in INDEX) — skip until machine works (disk)
- Next.js node_modules — install only when starting the app
