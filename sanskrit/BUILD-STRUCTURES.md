# Build structures — Pāṇini × Bruno × Notoria × Tantraloka

> Web-research results for **structures we can actually implement** (2026-10-03).  
> Goal: a palace that **behaves like Pāṇini**, not a museum of sūtras.  
> Stack: `/root/sanskrithelp` · `/root/bruno` · optional Vidyut engine

---

## TL;DR — what to steal

| Need | Best structure | Source |
|------|----------------|--------|
| **Executable grammar** | `Prakriya` + rule modules + prakriyā traces | **Vidyut / Padmini** (ambuda-org) |
| **Sandhi as gates** | Ordered sandhi modules + sūtra sets Ω | Sandhi ontology (Lakshmanan et al.) |
| **Parse pipeline** | Level 0–3: split → morph → sentence graph | kmadathil/sanskrit_parser |
| **Rule engine (data)** | Rules in tables/YAML, not hard-coded | buda-base/sandhi-engine · SCL |
| **Spatial palace graph** | Wing → Room → Drawer + typed edges | **GraphPalace** / MemPalace |
| **Knowledge as procedure** | One executable source, many outputs | **PM-KR (W3C CG)** |
| **Sanskrit KG** | Ontology + triplets + query templates | Terdalkar thesis / Sangrahaka |
| **Your world layers** | Phonetics · physics · topology · vertical vāk | This project’s synthesis docs |

---

## 1. The engine skeleton (make grammar executable)

### Vidyut / Padmini model — **use this as the palace physics core**

Repo: [ambuda-org/vidyut](https://github.com/ambuda-org/vidyut) · [Padmini docs](https://padmini.readthedocs.io/)

| Object | Role in your palace |
|--------|---------------------|
| **`Term`** | A sound/form unit with tags (dhātu, tin, sub, it…) — *inhabitant of a zone* |
| **`Prakriya`** | Derivation stack — the **machine trace** you operate |
| **Rule modules** | angasya, it_agama, dvitva, ac_sandhi… — *rooms in Rule Tower* |
| **Prakriyā output** | Every step lists rule + result — **execution trace** (Bruno TRACE) |
| **API** | `derive_tinantas`, `derive_subantas`, `derive_krdantas`, `derive_taddhitanta` |

**Install path (when disk allows):**
```bash
# Python bindings (preferred for sanskrithelp)
pip install vidyut
# or clone
git clone --depth 1 https://github.com/ambuda-org/vidyut.git
```

**How it maps to your zones:**

| Zone | Vidyut module |
|------|----------------|
| Sound Gate | phoneme / SLP1 layer |
| Root Forest | Dhātupāṭha data + `Dhatu` |
| Verb Engine | `derive_tinantas` (lakāra, person, voice) |
| Case Temple | `derive_subanta` (sup, vibhakti) |
| Derivation Workshop | `derive_krdanta` / `derive_taddhitanta` |
| Sandhi Gates | vidyut-sandhi + your gate viz |
| Rule Tower | ordered rule modules + blocking (Padmini) |

**Prakriyā = the Bruno execution trace.** Each line: rule id + before/after form. That’s your TRACE template filled automatically.

---

## 2. Sandhi Gates — modular ontology (not one giant table)

Paper: [An Ontology for Comprehensive Tutoring of Euphonic Conjunctions](https://arxiv.org/pdf/1410.2871v2.pdf) (Lakshmanan)

| Structure | Use |
|-----------|-----|
| **6 sandhi classes** | prakṛtibhāva · vowel · consonant · ṛtva · visarga · anusvāra |
| **13 modules** | progressive order — later modules only use earlier knowledge |
| **Ω = 104 sūtras** | scoped set for tutoring (not all 4000) |
| **Ordering function** | output of sūtra *i* feeds only *j > i* — **exactly your Gate physics** |
| **Voice component** | sandhi is phonological — pair with Tantraloka speech levels |

**Implement in sanskrithelp:** `data/sandhi-rules.json` already exists — tag each rule with `class` + `module` + `order` + `input_phonemes` + `output_phonemes`. UI: INPUT → CONDITION → OPERATION → OUTPUT at the Gate.

**Engine alternative:** [buda-base/sandhi-engine](https://github.com/buda-base/sandhi-engine) — data-driven nested lookup (finals × initials), no hard-coded rules. Perfect for “rules as world laws.”

---

## 3. Full parse pipeline (meaning ↔ Sanskrit both ways)

Repo: [kmadathil/sanskrit_parser](https://github.com/kmadathil/sanskrit_parser)

| Level | Job | Palace floor |
|-------|-----|--------------|
| **0** | Sandhi split at phoneme | Sandhi Gates |
| **1** | dhatu+lakāra ↔ pada; prātipadika+vibhakti ↔ pada | Root Forest + Case Temple |
| **2** | DP over split/no-split choices | Derivation Workshop |
| **3** | Morphological constraint graphs (karaka, vacana…) | Kāraka Court + Output Theatre |

**Bidirectional walks** (your vertical axis):
- **Top-down:** meaning → roles → morphology → sandhi → speech  
- **Bottom-up:** speech → phonemes → morphology → karaka → meaning  

Also useful: [Process-Sanskrit](https://github.com/giacomo-de-luca/process-sanskrit) (cascading pipeline, modern Python) and [samsaadhanii/scl](https://github.com/samsaadhanii/scl) (Amba Kulkarni: morph analyser, sandhi, Ashtadhyayi simulator).

---

## 4. Spatial palace as a real graph

### GraphPalace / MemPalace hierarchy

```
Palace
 └── Wing (domain)
      ├── Room (subsystem zone)
      │    ├── HALL edges (same wing)
      │    ├── TUNNEL edges (cross-wing)
      │    └── Drawer (verbatim memory — never summarized)
      │         └── REFERENCES → Knowledge Graph entity
      └── Closet (topic summary)
```

| Feature | Why it fits Bruno/Pāṇini |
|---------|---------------------------|
| **Wings/Rooms** | Sound Hall · Root Forest · Case Temple · Sandhi Gates… |
| **Drawers verbatim** | Store sūtra text + prakriyā trace unmodified |
| **Typed KG edges** | `planet→grimoire→spell` style: `phoneme→class→rule→form` |
| **Pheromones / hot paths** | Which zones you actually use (Notoria log → palace heat) |
| **Temporal validity** | Rule supersession, edition changes (MemPalace `valid_from/valid_to`) |

**Local options:**
- JSON graph first (matches sanskrithelp + ochemapp style)  
- Later: Kùzu / Neo4j / MemPalace SQLite if you want Cypher  

**Schema sketch (JSON):**
```json
{
  "zones": [
    {"id": "sound_gate", "kind": "phonetics", "geometry": "vocal_tract"},
    {"id": "sandhi_gates", "kind": "transformation", "geometry": "gate"},
    {"id": "root_forest", "kind": "lexicon", "geometry": "tree"}
  ],
  "edges": [
    {"from": "phoneme:a", "memberOf": "pratyahara:ac", "layer": "paninian"},
    {"from": "phoneme:a", "signifies": "anuttara", "layer": "trika"},
    {"from": "phoneme:a", "locatedAt": "sound_gate.kaṇṭha", "layer": "bruno"}
  ],
  "traces": [
    {"prakriya": "bhavati", "steps": [{"rule": "3.1.12", "before": "bhū+ti", "after": "bhavati"}]}
  ]
}
```

---

## 5. PM-KR — knowledge as executable procedure

Repo: [w3c-cg/pm-kr](https://github.com/w3c-cg/pm-kr)

> KGs describe what things **are**. PM-KR describes how things **work**.

| PM-KR idea | Your use |
|------------|----------|
| One canonical procedure | One sūtra/rule as executable JSON, not N copies |
| Multi-modal outputs | Same rule → plate SVG · spoken drill · graph edge · derivation step |
| Spatial knowledge | Semantic proximity = spatial proximity (Bruno rooms) |
| Dual-client (human + AI) | You *operate* it; agent *traces* it |

**This is the philosophical match for “palace behaves like Pāṇini.”**  
Store: `rule.json` = { id, scope, conditions, transform, examples[], counterexample, neighbors[] } → renders as Gate animation + prakriyā line + agent tool.

---

## 6. Sanskrit knowledge graph (text ↔ ontology)

Thesis: [Sanskrit Knowledge-based Systems](https://hrishikeshrt.github.io/publication/phd/thesis.pdf) · tools Sangrahaka / Antarlekhaka

| Pattern | Use |
|---------|-----|
| **Ontology first** (entity + relation types) | Define phoneme / rule / form / karaka / tattva types |
| **Triplets** (S, P, O) | `(a, memberOf, ac)`, `(bhavati, derivedFrom, √bhū+ti)` |
| **Query templates** | “What operations apply to {phoneme}?” → Cypher/JSON |
| **Sandhi splitter + morph analyser** | Pipeline stages for bottom-up walks |
| **Manual annotation when tools fail** | Your Notoria sessions annotate weak links |

Complements Vidyut: Vidyut **generates**; KG **navigates**.

---

## 7. Tantraloka / Parātrīśikā layers (vertical axis)

Already in `sanskrithelp`:
- `data/tattvas.json` — 36 tattvas + mātṛkā rows  
- `data/rag/tantraloka-reference.md` · `tantrica2.md`  
- `app/tantra/` — tattvas, Mātṛkā, Layayoga  

**Structure to add (not invent):**

| Layer | Representation |
|-------|----------------|
| **4 levels of speech** | parā → paśyantī → madhyamā → vaikharī as palace **floors** |
| **Dual phoneme view** | Each phoneme: `paninian[]` + `trika[]` addresses |
| **Mātṛkā vs Mālinī** | Two path types through Sound Hall (unfold / return) |
| **aham chain** | anuttara → aham → phonemes → grammar → speech (your first diagram) |

**Don’t** claim Pāṇini = Trika. **Do** give the same phoneme two linked coordinate systems.

---

## 8. Notoria as outer ritual (meta layer)

Not a data structure — a **session protocol**:

```
general (memory|understanding|perseverance|eloquence)
  → nota (one zone chart)
  → operate one derivation / one sandhi / one kāraka
  → TRACE into palace
  → log
```

Grammar notae I–III → morphology / kārakas / sandhi+samāsa (see `PANINI-PALACE-NOTORIA-TANTRALOKA.md`).

---

## 9. Recommended build order (concrete)

### Phase A — structures only (no full engine yet)
1. **JSON palace schema** (zones + edges + traces) in `sanskrithelp/data/palace/`  
2. **Phoneme stations** dual-view (Pāṇinian + Trika) for 50 varṇas  
3. **Sandhi gate cards** from `sandhi-rules.json` (class + order + I/O)  
4. **TRACE template** = Padmini prakriyā line format  

### Phase B — engine behind the palace
5. Install **Vidyut Python** (watch disk — 1.5G free)  
6. Wire `derive_tinantas` / `derive_subanta` to Verb Engine + Case Temple  
7. Optional: sandhi-engine table lookup for Gates  

### Phase C — graph + agent
8. Export palace + traces as KG edges (like ochemapp `joinEdges`)  
9. Agent tools: `get_prakriya`, `apply_sandhi`, `phoneme_view`  
10. Notoria logs → hot-path stats on zones  

### Phase D — vertical Trika axis
11. Floors parā→vaikharī on utterances (bidirectional walks)  
12. Mātṛkā vs Mālinī as two Sound Hall routes  
13. Read Parātrīśikā working copy alongside Zone 1–2  

---

## 10. One-page data model (start here)

```text
PHONEME
  id: "a"
  articulation: {kaṇṭha|tālu|…}
  paninian: { classes: ["ac"], pratyaharas: ["ac","aK"] }
  trika: { anuttara: true, matrika_row: "vowels" }
  bruno: { zone: "sound_gate.vowels", image: "…" }

RULE
  id: "3.1.12"
  class: "ac_sandhi" | "sandhi.vowel" | …
  module: 4
  order: 12
  input: ["i", "a"]
  condition: "…"
  output: "ya" | "e" | …
  trace_examples: 3
  counterexample: 1

PRAKRIYA
  word: "bhavati"
  steps: [{rule, before, after}, …]
  zones_touched: ["root_forest", "verb_engine"]

ZONE
  id: "sandhi_gates"
  geometry: "gate"
  physics: "input → condition → operation → output"
```

---

## 11. Resources checklist

| Resource | URL | Use |
|----------|-----|-----|
| Vidyut | github.com/ambuda-org/vidyut | Prakriyā engine |
| Padmini | padmini.readthedocs.io | Rule selection model |
| sandhi ontology | arxiv 1410.2871 | Gate modules + ordering |
| sandhi-engine | github.com/buda-base/sandhi-engine | Data-driven sandhi |
| sanskrit_parser | github.com/kmadathil/sanskrit_parser | Level 0–3 pipeline |
| SCL | github.com/samsaadhanii/scl | Amba Kulkarni tools |
| Process-Sanskrit | github.com/giacomo-de-luca/process-sanskrit | Modern cascading |
| GraphPalace | graphpalace.org | Wing/Room/Drawer graph |
| PM-KR | github.com/w3c-cg/pm-kr | Executable knowledge |
| Sanskrit KG thesis | hrishikeshrt.github.io | Ontology + triplets |
| Local | sanskrithelp · bruno · volume tantraloka | Your corpus |

---

## Bottom line

**Don’t invent a new grammar system. Compose:**

1. **Vidyut** = physics (prakriyā)  
2. **Sandhi ontology + engine** = gates  
3. **GraphPalace schema** = spatial topology  
4. **PM-KR** = knowledge as executable procedure  
5. **Tantraloka/Parātrīśikā** = vertical depth + dual phoneme views  
6. **Ars Notoria** = outer faculty ritual  

**Next single step:** JSON palace schema + 5 dual-view phoneme stations + one TRACE from Vidyut (or hand-traced √bhū→bhavati) in `sanskrithelp/data/palace/`.
