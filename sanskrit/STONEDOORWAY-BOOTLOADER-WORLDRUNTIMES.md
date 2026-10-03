# StoneDoorway — auditory bootloader + git world runtimes

> Trigger → liminal lobby → recall → select → walk → audio-guided imaginal world  
> **Not a renderer** — an **auditory bootloader / OS shell for inner worlds**  
> Sigil: **Gurdjieff Enneagram in a circle** — brand + boot + entry emblem  
> Worlds ship as **git runtimes** (JSON/protocol), not assets you must render  
> Companion: `STONEDOORWAY-AUDIAL-OS.md` · beds: `worlds/stonedoorway-world-beds.json`

---

## Interaction model (frozen)

```text
TRIGGER
  stone doorway appears (sigil + tone + voice)
        ↓
LIMINAL LOBBY
  grid of worlds / windows (imaginal)
        ↓
RECALL  ← killer mechanic
  you must reconstruct the worlds yourself
  AI: "What appears in the upper-left window?" → wait
        ↓
SELECTION
  choose one world
        ↓
ENTRY
  walk through doorway
        ↓
AUDIO-GUIDED IMAGINAL WORLD
  binaural beat + AI voice + inner construction
        ↓
RETURN
  threshold · log · bed fades
```

---

## Why audio-only is a strength

StoneDoorway is **not** a renderer.

| Not | Is |
|-----|-----|
| Gallery of images | **Bootloader for imagination** |
| Click menu | Reconstruct grid in the dark |
| AR world | Ear + voice + mind |
| App chrome | OS shell for inner worlds |

Constraint forces **you** to do the install.

---

## Gurdjieff Enneagram — the brand sigil

| Fact | Use |
|------|-----|
| Shape = **seven-pointed star** in a circle | Gurdjieff Enneagram (circle + 3-6-9 + 1-4-2-8-5-7) / {7/2} or {7/3} |
| Feel = portal, structured gateway, symmetry + mystery | activation sigil of entry |
| Not required to equal one historic system | **brand + boot + doorway emblem** |

**Boot use:**

```text
1. black field
2. Gurdjieff Enneagram sigil appears faintly
3. low binaural / drone starts
4. AI: "StoneDoorway. Enter."
5. doorway opens
6. lobby appears internally (imaginal)
```

---

## Progressive lobby (1 → 2 → 4 → 9)

| Stage | Grid | AI does NOT say | AI DOES say |
|-------|------|-----------------|-------------|
| S1 | **1 window** | “Here is your world” | “What appears in front of you?” → wait |
| S2 | **2** | “Two worlds available” | “Name both windows.” → wait |
| S3 | **4** (2×2) | “Select from this menu” | “What appears upper-left? …” |
| S4 | **9** (3×3) | “Welcome to the hub” | “Reconstruct the lobby. Name all nine.” |

**Advance when you reconstruct — not when time passes.**

### Recall prompts (before every entry)

```text
What is behind this door?
What do you hear there?
What is the first object?
What is the governing rule there?
```

---

## Git world runtimes (share + shape)

Worlds are **protocol packages**, not images.

```text
worlds/
  stonedoorway-os-lobby.json      # system lobby + progressive stages
  stonedoorway-world-beds.json    # bed map
  stonedoorway-lab-session.json   # daily lab protocol
  runtime/
    sanskrit-matrika/
      world.json                  # manifest + voice + bed + work
      GUIDE.md                    # what AI says
    sanskrit-laya/
      world.json
    ...
```

### `world.json` contract

```json
{
  "id": "sanskrit-matrika",
  "name": "Mātṛkā",
  "kind": "sanskrit_lab",
  "bed": {"preset": "matrika_install", "hz": 6.0},
  "trigger_phrases": ["Let's go into Sanskrit world", "Enter Mātṛkā"],
  "voice": {"on_walk": "...", "on_work": "...", "on_return": "..."},
  "recall_prompts": ["What do you hear?", "Which series?"],
  "work": {"protocol": "install_series", "series": "dentals|gutturals|labials"},
  "runtime_cli": "python3 sanskrit/lab/daily_runtime.py session --faculty memory --series dentals",
  "license_note": "protocol only; audio beds separately licensed",
  "provenance": {"sources": ["Castle faculty shell", "matrika practice schema"]}
}
```

You **shape** a world by editing this JSON + GUIDE lines — git commit — others run the same OS shell over your world.

---

## First Sanskrit world — what the AI actually says

### Trigger

```text
You: Let's go into Sanskrit world.
AI:  StoneDoorway.
     Tunnel open.
     Mātṛkā bed on.
```

### Lobby (first session — 1 window)

```text
Darkness. A single window.
What appears in front of you?
```

*Wait.*

```text
Name it. Walk through when you are ready.
```

### Entry

```text
You crossed. The letter is here.
Form. Sound. Colour. Place.
Chant it aloud — vaikharī.
```

### Work

```text
One series only tonight.
Gutturals or dentals — you choose.
Chant with the bed. Then stop the bed.
Chant alone. Silence three minutes.
Speak one word using a letter.
```

### Return

```text
Return to the threshold.
What stuck?
One line.
```

### Later (4-window stage)

```text
Four windows: Mātṛkā, Laya, Pāṇini, Threshold.
Reconstruct them.
What is upper-left?
What do you hear upper-right?
Choose one. Walk through.
```

---

## Boot sequence (brand)

| Beat | Audio |
|------|-------|
| 1 | Silence / black field (imaginal) |
| 2 | Gurdjieff Enneagram sigil (faint in mind) |
| 3 | Low drone / binaural bed |
| 4 | “StoneDoorway. Enter.” |
| 5 | Doorway opens (tunnel cue) |
| 6 | Lobby · recall · work |
| 7 | “Bring yourself back.” |

---

## Commands (natural language)

| Say | OS does |
|-----|---------|
| “Open the Stone Doorway” | Boot + lobby (current stage) |
| “Enter Sanskrit world” | Mātṛkā runtime + bed |
| “Enter silence” | Laya runtime |
| “What is the grid?” | Recall drill only |
| “Leave me here for one hour” | (roadmap) free walk |
| “Return” | Threshold + log |

---

## Product shape

```text
STONE DOORWAY OS SHELL     sigil · boot · lobby · recall · beds
         ↓
WORLD RUNTIMES (git)       sanskrit-matrika · sanskrit-laya · …
         ↓
LAB ENGINE (optional CLI)  daily_runtime.py · WorldIR · Pāṇini
         ↓
YOU                        reconstruct · walk · speak · log
```

**Grimoirer** stays reader/commerce.  
**Bruno** hosts lab + this OS design + runtime packages.  
**Stonedoorway** can later host the audio shell.

---

## Next builds (ordered)

1. ✅ Design docs + lobby + beds map  
2. World runtime package `worlds/runtime/sanskrit-matrika/`  
3. Guide scripts as first-class files  
4. Heptagram SVG/ASCII for brand (optional visual only — practice stays audial)  
5. Voice TTS boot (ElevenLabs/Workers later)  
6. Multi-world git repo (`stonedoorway-worlds`)  

---

## One-liner

> **StoneDoorway = heptagram bootloader + git-shareable world protocols: AI shape + you reconstruct the grid in the dark, walk through a named window, inhabit by ear.**
