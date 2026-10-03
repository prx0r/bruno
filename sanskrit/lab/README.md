# Sanskrit lab — computational runtime

Wired stack: **WorldIR · Bruno engine · Pāṇini runtime · Notoria faculty shell · StoneDoorway doorway**

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
python3 daily_runtime.py explore --wheel varna_series --n 3
python3 daily_runtime.py doorway
```

| Module | Role |
|--------|------|
| `worldir.py` | KnowledgeGraph + Varna atom (knowledge ≠ representation) |
| `bruno_engine.py` | LEXICON · WHEEL · SCENE · LOCUS + Caelum + 30 seals |
| `panini_runtime.py` | 3983 rules · pratyāhāra · teaching derivations |
| `notoria_session.py` | Castle faculty shell (memory/intellect/eloquence) |
| `daily_runtime.py` | CLI |
| `test_lab.py` | Smoke tests |
| `data/` | Maheshvara, pratyāhāras, varnas, sutra index |

**Daily protocol:** intention → figure hub → install series → contractio → Laya silence → Pāṇini mini → speak → log

**Corpus:** `../../sources/panini/` · **Doorway:** `../worlds/stonedoorway-lab-session.json`

**Honesty:** derivation traces are teaching runtimes over real sūtra corpus — not a claim of complete computational Aṣṭādhyāyī fidelity. Colors = pedagogical scaffold unless sourceAttested.
