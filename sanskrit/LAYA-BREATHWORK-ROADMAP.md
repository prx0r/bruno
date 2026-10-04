# CANONICAL — Breathwork roadmap (advanced · Goswami · 1bref engine)

> For practitioners who **can handle bandhas and longer holds**.  
> Sources on disk: full Goswami *Layayoga* · `layayoga-reference.md` · `tantrica2.md` · VB mapping · **prx0r/1bref-meditation** (cloned `/root/1bref-meditation`).  
> Goal: kundalini breathwork · suṣumṇā · elongations · laya → prepare advanced tantric work.  
> Import target: **Stonedoorway** (night shells) + optional **sanskrithelp** `/tantra/practice`.

---

## 1. What we already have

| Asset | Where | Reuse |
|-------|-------|-------|
| **Full Goswami** | `sanskrithelp/data/rag/layayoga.txt` | Progression source of truth |
| **Layayoga reference** | `layayoga-reference.md` | Theory map |
| **tantrica2 schema** | 1:4:2 + mātṛkā + VB | Night practice grammar |
| **1bref breath engine** | `/root/1bref-meditation` · GitHub `prx0r/1bref-meditation` | **Visualizer + rhythm taps + technique library** |
| **layayoga_meditate.html** | 1bref | Nāḍī 4·16·8 · Sama Vṛtti · Green Core · SAUḤ · KHPHREṄ · 5 Voids · Bīja sequence |
| **Meditation mobile** | 1bref | Anapanasati progression + WebAudio clicks/bells + tempo |
| **Kernel protocols** | stoneseed `laya-142-nadi` · `laya-breath` | Night JSON shells |
| **Canonical tonight card** | `LAYA-BREATHWORK-CANONICAL.md` | Beginner-safe 1:4:2 |

### 1bref engine — what to import

| Piece | Value |
|-------|-------|
| **TECHNIQUES array** | ratios + howto + advance criteria (Nāḍī, Sama Vṛtti, Green Core, bījas, 5 Voids) |
| **Phase state machine** | inhale → holdIn → exhale → holdOut → rounds |
| **Ring visualizer** | canvas ring + phase colors |
| **Rhythm taps** | WebAudio `playClick` / `playBell` at phase boundaries |
| **Tempo controls** | meditation page tempo row |
| **Wrapper pattern** | don’t fork HTML; extract TECHNIQUES + state machine as JSON/TS |
| **Meditation entries** | anapanasati → elements (counting → duration → whole breath → tactile) |

**Import rule:** copy **data + state machine + audio cue logic**, not brittle string-patch wrapper. Engine stays clean in Stonedoorway; 1bref remains the lab sandbox.

---

## 2. Goswami progression (actual, advanced track)

Goswami is **not** “do 4-16-8 forever.” The book’s path is layered:

### A. Foundations (before force)

| Stage | Content |
|-------|---------|
| **Physical purification** | Diet · internal cleansing · exercise (walk/swim/bhastrika later) |
| **Posture** | Stable seat (vajrasana / accomplished posture) |
| **Nāḍī śuddhi** | Pranayama refines body → “health, vitality… super-purification” |
| **Mental purification** | Discipline before concentration |

### B. Breath ladder (sahita → kewala)

| Level | Measure | Notes |
|-------|---------|-------|
| Classical | **16 : 64 : 32** | 1:4:2 units — puraka : kumbhaka : rechaka |
| Reduced | **4 : 16 : 8** | Standard intermediate |
| Light | **1 : 4 : 2** | Entry |
| Sahita | Breath-control **with** in/out | Main workhorse |
| Kewala | Natural breathless suspension | **Outcome** of sahita + concentration — not forced |

**Pranayama signs (Sharadatilaka via Goswami):**  
1. perspiration → 2. body shakes → 3. levitation/lightness · calm mind  
**Appear after long regular practice** — not session targets.

### C. Tantrika laya stack (your advanced lane)

Goswami / Yogakuṇḍalinī lineage:

| Element | Role |
|---------|------|
| **Śakti-caraṇa / shaktichalana** | Internal power-conduction — first stage of control |
| **Yonimudrā** | Anogenital control — assists shaktichalana |
| **Śambhavī** | Mind concentrated at ājñā; sensory control |
| **Bandhas + kumbhaka** | mūla · jalandhara · uddiyana — with sahita kumbhaka to rouse kuṇḍalinī into suṣumṇā |
| **Bhastrika** | Short vigorous breath — hatha purification layer |
| **Mahāmudrā / mahābandha / mahāvedhā** | Advanced locks — only after bandhas are stable |
| **Mantra on breath** | Bīja as kuṇḍalinī in sound-form |
| **Bhutashuddhi** | Deep thinking replicating kundaliniyoga events (not only physical breath) |

### D. Concentration ladder (laya)

```text
pratyahara → dharana (3 forms) → dhyana → samprajñāta → asamprajñāta
```

| Practice | Goswami detail |
|----------|----------------|
| **Dharaṇā** | Holding-concentration **with kumbhaka** on 5 lower centres (earth→void) one at a time + bijas |
| **Dhyāna** | Continuous concentration; light may arise |
| **Mantra chain** | 100 units → 1,000 → 10,000 graduated |
| **Laya hierarchy** | Earth → water → fire → air → void → I-consciousness → mahat → avyakta → puruṣa |
| **Kuṇḍalinī arc** | coiled → uncoil → rise/absorb → **recoil** → spiritualize daily life |

### E. Your advanced nightly template (bandhas OK)

**Do not start here if new.** You said you can handle bandhas and longer holds.

| Block | Time | Practice |
|-------|------|----------|
| **1. Seat + intention** | 3m | Posture · one faculty/intention · stop available |
| **2. Elongation ladder** | 4m | Natural breath → **exhale 3–4× inhale** unforced · then both-nostril 1:4:2 soft |
| **3. Nāḍī Śodhana classical** | 12–15m | **16:64:32** (or 8:32:16 if not yet full) · **mūla + jalandhara on hold** · optional light uḍḍīyāna only if breath free · **5–8 rounds** |
| **4. Uḍḍīyāna / bhastrika (optional, not every night)** | 4–6m | Empty-lung uḍḍīyāna ×5–10 · or short bhastrika rounds · then rest natural breath |
| **5. Dharaṇā with kumbhaka** | 8m | Hold 16–32 units · attention on muladhara → heart → ājñā one at a time · bija optional |
| **6. Mantra-on-breath** | 5m | SAUḤ 3 → YAṄ 7 → KHPHREṄ 11 (or one seed only) on 4:16:8 |
| **7. Laya / kewala window** | 5–8m | Stop all control · wait for breath to thin · **do not force breathless** |
| **8. Recoil / close** | 3m | Soft both-nostril · stand · log |

**Alternate night (recovery):** Session A from `LAYA-BREATHWORK-CANONICAL` only (4-16-8, no bandhas) + 5 Voids light + mātṛkā.

---

## 3. 12-week advanced roadmap

| Week | Focus | Ratio / method | Engine (1bref) |
|------|-------|----------------|----------------|
| **1–2** | Lock classical sahita | 4:16:8 → 8:32:16 · bandhas on hold | Nāḍī Śodhana 4·16·8 |
| **3–4** | Classical measure | **16:64:32** · 5 rounds · mūla+jalandhara | Same + longer hold |
| **5** | Empty-lung control | Uḍḍīyāna ×5–10 + natural breath reset | New technique entry |
| **6** | Bhastrika short | 20–30 pumps ×3 · then nāḍī | Add bhastrika technique |
| **7** | Dharaṇā centres | Kumbhaka 16–32 · muladhara/heart/ājñā | “Dharaṇā Hold” technique |
| **8** | Mantra-on-breath | SAUḤ/YAṄ/KHPHREṄ on 4:16:8 | Existing bīja techniques |
| **9** | 5 Voids light | 5:5:5 · one void per cycle | The 5 Voids |
| **10** | Kewala window | Sahita + 5–8 min silent thinning | Meditation mobile silence |
| **11** | Mahāmudrā prep | Only if bandhas + posture solid | Optional new entry |
| **12** | Integrate + assess | Full advanced night ×3/week · recovery nights | Log + ochema diary |

**Signs of progress (Goswami):** steady 16:64:32 · both nostrils even · hold without strain · breath thins on its own · mind calm during hold.  
**Not progress:** panic holds · chasing levitation · skipping recovery nights.

---

## 4. Roadmap → Stonedoorway import plan

### Phase 0 — Extract engine (clean)

From 1bref, extract to **JSON/TS module** (no HTML string patches):

```json
{
  "techniques": [
    {"id":"nadi_16_64_32","name":"Nāḍī Śodhana","ratio":"16·64·32",
     "inhale":16,"holdIn":64,"exhale":32,"holdOut":0,"rounds":5,
     "bandhas":["mula","jalandhara"],"level":"advanced"},
    {"id":"sama_vritti","name":"Sama Vṛtti","ratio":"4·4·4·4", "...": "..."},
    {"id":"green_core","...":"4·8·8"},
    {"id":"sauh","...":"4·8·8"},
    {"id":"khphremg","...":"4·16·8","rounds":11},
    {"id":"five_voids","...":"5·5·5"},
    {"id":"bija_sequence","...":"complete session"}
  ],
  "phases": ["inhale","holdIn","exhale","holdOut"],
  "cues": {"click_on_phase": true, "bell_on_round_end": true}
}
```

Also port:
- Phase state machine (`nextPhase` / `endRound`)
- WebAudio click/bell (or leave audio to Stonedoorway beds)
- Meditation anapanasati progression as optional day track

### Phase 1 — Stonedoorway doorway presets

| Preset | Content |
|--------|---------|
| `laya-classical-16-64-32.json` | Advanced nāḍī + bandha labels + recovery note |
| `laya-bhastrika-uddiyana.json` | Optional morning purification (not every night) |
| `laya-dharana-hold.json` | Kumbhaka + centre attention |
| `laya-bija-sequence.json` | SAUḤ → YAṄ → KHPHREṄ → silence |
| `laya-kewala-window.json` | Sahita + silent thinning |

Map onto existing kernel: `laya-breath` world + new protocols under `protocols/night/`.

### Phase 2 — UI in Stonedoorway

- Breath tab / Journey phase: **ring + countdown + phase colors** (from 1bref visualizer)
- Optional **rhythm taps** at phase change (click) and round end (bell)
- Bandha checklist as protocol steps (not auto-forced)
- Log → ochema diary

### Phase 3 — sanskrithelp parity

- `/tantra/practice` already has 1:4:2 + 5 voids  
- Add advanced techniques as selectable practice types  
- Same TECHNIQUES JSON shared (single source)

### Phase 4 — Day/night split

```text
DAY (sanskrithelp / 1bref lab)
  anapanasati · elongation · technique drills · tempo taps

NIGHT (Stonedoorway)
  advanced sahita · bandhas · dharaṇā · bīja · kewala · mātṛkā optional
```

---

## 5. Safety (advanced still applies)

| Rule | Detail |
|------|--------|
| Stop available | Always in UI + practice |
| Bandhas | Only if already competent; soft jalandhara ≠ throat crush |
| Uḍḍīyāna | Empty lungs; not after heavy meals; not every night |
| Bhastrika | Short sets; stop if dizzy |
| Kewala window | Wait — don’t seize breathless |
| Recovery nights | 4-16-8 or natural breath — required |
| Not medical | Practice grammar only |

---

## 6. What “done” looks like in 12 weeks

1. **16:64:32** comfortable ×5 rounds with light bandhas  
2. Elongation obvious without forcing  
3. Both nostrils balanced after practice  
4. Dharaṇā holds at centres without panic  
5. Bīja sequence or single-seed mantra-on-breath stable  
6. Kewala window = breath thins **on its own**  
7. Recoil: calm after session · daily life slightly clearer  
8. Ready for **advanced tantric work** (mantra initiation, deeper dhyāna, full bhutashuddhi) under real guidance  

---

## 7. Files

| Path | Role |
|------|------|
| `/root/1bref-meditation/` | Engine lab (cloned) |
| `bruno/sanskrit/LAYA-BREATHWORK-CANONICAL.md` | Tonight-safe card |
| `bruno/sanskrit/LAYA-BREATHWORK-ROADMAP.md` | This roadmap |
| `sanskrithelp/data/rag/layayoga.txt` | Full Goswami |
| stoneseed `laya-breath` · `laya-142-nadi` | Kernel night shells |
| stonewordway presets (to add) | Classical / advanced doorway |

---

## 8. Next build steps

1. Extract 1bref TECHNIQUES + phase machine → `stoned/app/breath_engine.json` (or kernel data)  
2. Add Stonedoorway preset `laya-classical-16-64-32.json`  
3. Optional: import ring visualizer into Stonedoorway Journey tab  
4. Log advanced sessions in ochema diary  
5. Week 4 check: can you run 16:64:32 ×5 without strain?
