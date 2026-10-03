# Greer · Provenance · Bruno wheels → Pāṇini constraints (verbatim)

> Saved word-for-word from owner message (2026-10-03).  
> Companion: `BRUNO-WHEELS-IMAGINAL-COMPILER.md` · `BRUNO-STACK-V2.md`

---

Yes — **Greer’s translation is good**, and for our purposes it may actually be the most useful English *De umbris* edition.

John Michael Greer’s 2020 *On the Shadows of the Ideas* is a complete translation with extensive notes and an explicit practical orientation. A comparative review notes that Scott Gosnell gives a plainer, serviceable translation with about 45 explanatory notes, whereas Greer supplies nearly 200 notes and much more Renaissance/esoteric context.

The caveat is important: **Greer is a practitioner-interpreter as well as translator**. For our computational project, I would therefore ingest:

**Greer = practical interpretation**
**Gosnell = independent English cross-check**
**Sturlese critical Latin edition = textual authority**

Rita Sturlese’s 1991 *De umbris idearum* is part of the historical-critical edition of Bruno’s Latin works, and the later Adelphi *Opere mnemotecniche* gives the Latin alongside Italian translation and scholarly commentary.

So if the LLM says “Bruno’s operator does X,” ideally it can distinguish:

```text
BRUNO_LATIN
GREER_TRANSLATION
GOSNELL_TRANSLATION
GREER_COMMENTARY
OUR_COMPUTATIONAL_INTERPRETATION
```

That provenance system matters.

## The forum explanation of the wheels is mostly right

The PAO analogy is useful, but slightly too modern/simplified.

The Warburg Institute’s reconstruction of *De umbris* confirms Bruno’s first wheel structure:

**first ring:** mythological/heroic figures
**second:** actions/scenes
**third:** attributes/*insignia*

Then the larger system expands into **five concentric rings with 150 positions**, involving categories such as agent, action, insignia, associated/bystanding material and circumstance.

So:

> “Person–Action–Object”

is a very good **modern mental model**, but Bruno's actual categories are richer.

For example, the forum's idea:

> Lycaon + ploughing + Apollo's belt

is exactly the kind of permutation Bruno wants. The point is that familiar elements become **active scenes**, not merely static symbols. Scholarship on Bruno's wheel specifically emphasizes that rotation makes images interact dynamically, turning symbolic contents into active subjects of thought.

## Your “multidimensional jagged array” analogy is excellent

Computationally, I think that's almost exactly how we should represent it.

A Bruno wheel is roughly:

```ts
type WheelAxis<T> = {
  id: string
  values: T[]
}

type WheelSystem = {
  alphabet: Symbol[]
  axes: WheelAxis<ImaginalToken>[]
  constraints?: Constraint[]
}

type WheelState = {
  selections: number[]
}
```

For the full *De umbris* system:

```text
AXIS 1 = agent
AXIS 2 = action
AXIS 3 = insignia
AXIS 4 = attendant / associated thing
AXIS 5 = circumstance
```

So a state is:

```ts
[
  "Apollo",
  "ploughing",
  "chain",
  "green bird",
  "at the seashore"
]
```

and the renderer turns it into **one vivid animated scene**.

Mathematically:

> `Scene = Agent × Action × Insignia × Adjunct × Circumstance`

But **jagged/sparse tensor** is even better than a plain Cartesian product because not every combination is equally meaningful.

We can have:

```ts
score(scene) =
  semanticCoherence +
  vividness +
  distinctiveness +
  retrievability
```

And reject garbage combinations.

## Bruno actually has TWO distinct uses of combinatorics

This is critical.

### 1. Encoding

Something external becomes a scene.

```text
WO + NE + RI + NG
       ↓
symbol lookup
       ↓
agent + action + objects
       ↓
one bizarre scene
       ↓
store in locus
```

That is essentially compression/decompression.

```ts
encode(symbols) -> scene
decode(scene) -> symbols
```

This is what the forum PAO description is mostly explaining.

### 2. Thinking

This is much more interesting for StoneDoorway.

Instead of starting with symbols you want to memorize:

```text
concept A
concept B
concept C
      ↓
COMBINE
      ↓
unexpected relation
      ↓
inspect it
```

The wheels become a **combinatorial search engine for imagination**.

That is the Lullian side of Bruno.

Modern Bruno scholarship explicitly describes the wheel as more than rote memory: his combinatorial system produces different philosophical perspectives and uses movement/permutation as part of cognition.

So we should have:

```ts
mode: "encode" | "explore"
```

That's huge.

---

## Why almost nobody uses Bruno today

I think your observation is right, but there isn't good quantitative data on contemporary use.

There are active enthusiasts — the Art of Memory community, Greer, Martin Faulks and a handful of modern implementations — but it's clearly niche. The forum discussion you pasted itself notes the scarcity of actual practitioners, and there are now some digital Bruno-style volvelles, but nothing remotely like Anki or mainstream competitive-memory PAO adoption.

There's a simple reason.

If your problem is:

> memorize 1,000 random digits rapidly

modern PAO systems are easier.

Bruno asks you to learn a **huge permanent internal symbolic language before the system becomes powerful**.

That overhead is awful for competitive memory.

But that may make Bruno **better for what we're doing**.

Because we're not trying to memorize shuffled cards.

We're trying to install:

> Sanskrit + grammar + philosophy + texts + conceptual structures

over **years**.

Now amortizing the cost of learning an internal symbolic language makes sense.

---

# This is where Pāṇini becomes insane

You can immediately see how the same primitive generalizes.

Bruno:

```text
AGENT × ACTION × ATTRIBUTE × CONTEXT
```

Pāṇinian Sanskrit might have spaces like:

```text
ROOT
×
DERIVATIONAL OPERATOR
×
TENSE/MOOD
×
PERSON
×
NUMBER
×
VOICE
```

Except now we introduce **constraints**.

Not every tuple is legal.

So:

```ts
type PaninianSpace = {
  dimensions: Dimension[]
  constraints: Sutra[]
}
```

Take a candidate point:

```text
√gam
+ present
+ parasmaipada
+ 3rd person
+ singular
```

The Pāṇini engine tells us which rule path makes that configuration realizable.

Then Bruno renders the rule path into something imaginable.

This is beautiful computationally:

```text
BRUNO
defines representational dimensions

PĀṆINI
defines constraints + transformations

AI
explores the resulting state space

STONEDOORWAY
renders it
```

### Even better: Sanskrit phonemes make the Bruno wheel less arbitrary

Bruno had to create an artificial 30-symbol code.

We already possess a deeply structured symbol system:

> **Sanskrit varṇas.**

And unlike an arbitrary A–Z encoding, they already have relationships:

```text
place of articulation
manner
voicing
aspiration
vowel length
Pāṇinian grouping
pratyāhāra membership
```

So instead of:

```text
A → Apollo
B → Deucalion
C → Lycaon
```

our base symbols can be:

```text
क
ख
ग
घ
ङ
...
```

and their imaginal identities can be built from their **actual phonetic structure** first.

Then the imagery is layered on top.

That means our inner symbolic alphabet isn't arbitrary.

It's grounded in Sanskrit itself.

---

# I would therefore split the Bruno engine into four primitives

This is enough to start coding:

```ts
BrunoEngine {
  // stable symbolic dictionaries
  lexicons: ImaginalLexicon[]

  // combinatorial axes
  wheels: Wheel[]

  // spatial storage
  loci: SpatialTopology[]

  // operations
  operators: ImaginalOperator[]
}
```

And specifically:

```text
LEXICON
symbol → stable imaginal object

WHEEL
combine dimensions

SCENE
turn combination into animated experience

LOCUS
give the result a stable address
```

That's already a usable cognitive runtime.

Then things like **Field, Sky, Chain, Tree, Ladder** become different `SpatialTopology` / `ImaginalOperator` implementations.

---

The big realization is therefore:

> **Bruno isn't giving us one weird Renaissance memory trick. He's giving us a representational language.**

And Pāṇini gives us something complementary:

> **a transformational language.**

So yes — computationalizing Bruno first is exactly the right move. Then we can mine Pāṇini with the same discipline, but instead of asking “what mnemonic trick is this?”, we ask:

> **What primitive computation is this grammatical mechanism performing?**

That gives us two clean runtimes before we even touch the much harder Abhinavagupta experiential layer.
