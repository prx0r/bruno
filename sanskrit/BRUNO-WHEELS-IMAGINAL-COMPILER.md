# Bruno Wheels + Imaginal Compiler Architecture (verbatim)

> Saved word-for-word from owner message (2026-10-03).  
> Forum: turducken et al. on Bruno’s memory wheels (Aug 2024) + architecture synthesis.  
> Companion: `BRUNO-STACK-V2.md` · `worlds/triginta-sigilli-inventory.json`  
> **Rule:** primary text → formalization → code, never forum summary → code.

---

doesn’t seem like there are many people that actually use them. I think they’re interesting, because they’re kind of like a multi-dimensional (possibly jagged) array that doesn’t hurt to picture.

Martin Faulks show how to use them as thinking devices and I think that’s probably the easiest way to use them.
For example you might have a wheel with 0 through 9, a second wheel that’s the same, and a third that says Person, Action, Object. On the numbered wheels you have the sounds associated with the major system.
This would give you a little device you can physically rotate and focus on, while you generate words from setting the wheels and thinking about it. 9(p/b) 4(r) person - Mr. Peanutbutter.

post by turducken on Aug 19, 2024
turducken
Aug 2024

Simply put, Bruno’s Wheels are an extended PAO for memorizing the constituent letters of a given word or sentence, meaning they are used to encode those letters into an image, which can then be placed into a memory palace.

Let us start with one of its simpler forms, which has three wheels:

bruno_memory_wheel
bruno_memory_wheel480×490 92.5 KB

Notice the 30 letters containing ones borrowed from the hebrew and greek alphabets. Bruno was fascinated with this number, as evident in his other works such as ‘Thirty Seals’ and ‘Thirty Statues’. The outer ring holds people, the middle actions, the innermost objects, each assigned to one of the letters. Bruno gives lists of such combinations inspired by characters from Ovid’s Metamorphoses. A few examples:

A Lycaon - feasting - in his chains
B Deucalion - ploughing stones - wearing his headband
C Apollo - with the Pythoness - wearing his belt

Now when using the wheels, we turn them against each other. The easiest way to visualize this would be to imagine them not nested within each other but rather beside each other, like the wheels on a combination bike lock. So if your code was ‘ABC’ you’d turn the first wheel so ‘A’ is facing toward you, then do the same with the other wheels. In our example, this leaves us with ‘Lycaon (A) ploughing stones (B) while wearing Apollo’s belt (C)’.

Bruno then adds on two more wheels signifying an attribute and a circumstance (or rather, another object to add to the scene). He then enlarges each wheel to hold not 30 individual letters, but 150 combinations of the letters and a vowel. So now we don’t have A, B, C but AA, AE, AI, AO, AU, BA, BE, etc, which allows one to memorize far more letters in a single image. The resulting wheels look like this:

page_1
page_11428×1485 349 KB

Now you’re probably wondering what to do when you have to memorize a word like ‘wondering’, since the ‘nd’ part could not be easily memorized with the letter-vowel structure we have now. For this, Bruno recommends the use of an additional figure (person) added to the locus, which is sitting, standing or lying down depending on whether its consonant is in the first, second or third two-letter combination of the word.

So for ‘wondering’ we would, judging from Bruno’s lists, have something like (to use modern examples, as Bruno recommends coming up with your own images) 'Wonder Woman (WO) nestling (NE) herself inside a ring (RI) that is gooey (G-) while Donald Duck (D-) is sitting down on the ring (denoting the position of his letter after ‘NE’, the second letter-vowel-combination).

And that is Bruno’s memory wheels in a nutshell. He also uses wheels in the llullian fashion, that, is, to combine questions and statements about metaphysics, but I imagine you’re more interested in the mnemonic side of things. Hope this helps!

post by Shelby on Aug 19, 2024
post by Shelby on Aug 19, 2024
post by Shelby on Aug 19, 2024
post by turducken on Aug 19, 2024 Yes. **This is the architecture.** I would phrase it slightly more precisely:

> **Bruno gives us a language for compiling knowledge into an imaginal/mnemonic world.
> Pāṇini gives us a language for compiling Sanskrit into transformations.
> Abhinavagupta gives us a language for compiling those sounds/structures into embodied experience.**

Then a text can consume all three.

There is also one important correction before we encode anything: **do not ingest that forum’s neat “30 Ideas = Mind, Intellect, Reason...” list.** It appears to be an LLM fabrication or at least a severe rewriting. Bruno really has thirty *Intentions* and thirty *Concepts* in *De umbris idearum*, but the actual first Concept begins with a Plotinian discussion involving Lucifer; it is not a standardized list beginning *Mens, Intellectus, Ratio*. Bruno says the thirty Intentions, thirty Concepts, and their combinations constitute the higher form of the art.

So: **primary text → formalization → code**, never forum summary → code.

## The common substrate

I would call the underlying system something like `WorldIR`.

Everything we learn gets compiled first into a neutral semantic object:

```ts
interface KnowledgeNode {
  id: string
  kind:
    | "sound"
    | "word"
    | "rule"
    | "concept"
    | "passage"
    | "argument"
    | "ritual"
    | "entity"
    | "state"
    | "action"

  label: string

  relations: Relation[]

  provenance: SourceAssertion[]

  representations: Representation[]

  learnerState?: LearnerState
}
```

The crucial distinction:

```text
KNOWLEDGE
what is actually being represented

≠

REPRESENTATION
how your mind is being taught to hold it
```

That lets the same Sanskrit concept have:

```text
semantic representation
grammatical representation
Brunian imaginal representation
Trika embodied representation
audio representation
visual representation
spatial representation
```

without confusing any of them.

---

# Bruno becomes the **Imaginal Compiler**

Not:

```ts
bruno = memoryPalace()
```

Instead:

```ts
BrunoCompiler.compile(knowledge, operator)
```

where an `operator` is one of Bruno’s representational procedures.

I’d define the primitive interface like this:

```ts
interface ImaginalOperator {
  id: string
  source: SourceRef

  accepts: KnowledgeShape[]
  produces: RepresentationShape[]

  encode(input: KnowledgeGraph): ImaginalGraph
  navigate(world: ImaginalGraph): NavigationModel
  retrieve(cue: Cue): KnowledgeNode[]
}
```

And then begin extracting Bruno’s seals into actual operators.

## The first verified operators

The surviving *Thirty Seals* itself calls the work an art for the **invention, disposition and memory** of all arts and sciences. Bruno isn’t presenting thirty pictures to worship; he is presenting procedures.

### `CAMPUS` — Field

Function:

> Establish an extensible **space of loci**.

Bruno describes imagination as capable of taking bounded things received from the senses and enormously multiplying them internally.

Computationally:

```ts
Campus {
  operation: "spatialize"

  createContainer()
  partition()
  assignLocus()
  subdivide()
  multiplyLocations()
}
```

So:

```text
knowledge domain
      ↓
FIELD
      ↓
regions
      ↓
loci
      ↓
images
```

This is basically your memory filesystem.

---

### `CAELUM` — Sky

Function:

> Represent a domain through **recursive spatial division and orientation**.

Bruno explicitly describes this seal as useful for cosmographic, geographical, and similar descriptions presented to the “inner eye”; his worked scheme maps hemispheres/quadrants into an imagined house.

So:

```ts
Caelum {
  operation: "coordinate"

  topology: "sphere"

  partition: {
    hemispheres: 2,
    quadrants: 4,
    recursive: true
  }

  relations: [
    "above",
    "below",
    "left",
    "right",
    "adjacent",
    "opposite",
    "inside"
  ]
}
```

This is a **coordinate system for imagination**.

---

### `CATENA` — Chain

Function:

> Encode ordered dependency.

```text
A → B → C → D
```

Use it for:

- derivations
- argument steps
- historical succession
- ritual sequences
- causation
- Sanskrit transformations.

Computationally:

```ts
Catena {
  operation: "sequence"
  graph: "directed-path"

  relations: [
    "precedes",
    "follows",
    "causes",
    "requires"
  ]
}
```

---

### `ARBOR` — Tree

Bruno’s fourth seal is explicitly **Arbor**, the Tree; descriptions of his system characterize it as branching outward like a trunk producing branches.

Computationally:

```ts
Arbor {
  operation: "hierarchize"
  graph: "tree"

  relations: [
    "parent",
    "child",
    "ancestor",
    "descendant",
    "sibling"
  ]
}
```

Use for:

```text
varṇa
 ├─ vowel
 │   ├─ simple
 │   └─ diphthong
 └─ consonant
     ├─ stop
     ├─ nasal
     ...
```

or:

```text
Śaiva tattvas
   ↓
Śuddha
Śuddhāśuddha
Aśuddha
```

---

### `SCALA` — Ladder

This one is especially interesting.

Bruno explicitly describes a graded ascent/descent and gives a sequence roughly of **being → living → sensing → imagining → reasoning → understanding → mentation**.

So:

```ts
Scala {
  operation: "grade"

  relations: [
    "higherThan",
    "lowerThan",
    "moreGeneral",
    "moreSpecific",
    "morePerfect",
    "derivesFrom"
  ]
}
```

That’s not simply storage.

It’s an internal **ordered dimension**.

For StoneDoorway we could use it for levels of abstraction, speech, consciousness, grammatical derivation, etc.—when the source genuinely has a graded structure.

---

### `FONS_SPECULUM` — Fountain / Mirror

This one is almost a **map function**.

Bruno describes one stable faculty/form/schema being successively turned toward many different subjects so they can all be examined according to it.

Computationally:

```ts
Mirror<T, R> {
  operation: "apply-schema"

  inspect(subject: T, schema: Schema): R
}
```

Example:

```text
same analysis template

          ↓
word 1 → root / affix / case / role
word 2 → root / affix / case / role
word 3 → root / affix / case / role
```

This is fantastically useful.

---

### `COMBINANS` — Combiner

Bruno’s twenty-ninth seal explicitly deals with representing enormous numbers of different syllables from a small number of images using combinations of consonants and vowels.

That one is almost ridiculously appropriate for Sanskrit.

```ts
Combinans {
  operation: "combinatorial-compose"

  atoms: Symbol[]
  constraints: CombinationRule[]

  compose(atoms): CompositeSymbol[]
}
```

This gives us:

```text
small symbolic alphabet
        +
combination rules
        ↓
huge representational vocabulary
```

Very Pāṇinian in spirit, though historically independent.

---

# Therefore Bruno’s layer is basically an **internal data-structure library**

This is the real insight.

Not every fact belongs in the same kind of memory palace.

If something is inherently sequential:

> use `CATENA`.

If hierarchical:

> use `ARBOR`.

If globally spatial:

> use `CAELUM`.

If graded:

> use `SCALA`.

If you’re repeatedly interrogating different things using the same frame:

> use `SPECULUM`.

If constructing huge vocabularies from atoms:

> use `COMBINANS`.

So the compiler can choose representation based upon **information topology**.

```ts
function chooseOperator(graph: KnowledgeGraph) {
  if (graph.isSequential()) return CATENA
  if (graph.isHierarchical()) return ARBOR
  if (graph.isSpatial()) return CAELUM
  if (graph.isGraded()) return SCALA
  if (graph.isCombinatorial()) return COMBINANS
}
```

This is much better than:

> “Put everything in a palace.”

---

# Now Pāṇini slots underneath beautifully

Pāṇini isn’t a mnemonic representation language.

He gives us another kind of grammar:

> **a transformation system.**

The *Aṣṭādhyāyī* is computationally interesting precisely because derivation consists of interacting rules, conditions and operations; modern researchers have implemented sections of it as rule networks and explicitly track derivational sequences.

So give Pāṇini a separate runtime:

```ts
interface PaniniRule {
  sutra: string

  domain: Domain
  conditions: Condition[]
  operation: Operation

  inheritedContext?: Anuvrtti[]
  exceptions?: RuleRef[]
  precedence?: PrecedenceRelation[]

  source: SourceRef
}
```

and:

```ts
interface Derivation {
  input: LinguisticState
  steps: DerivationStep[]
  output: LinguisticState
}
```

Each step:

```ts
interface DerivationStep {
  before: LinguisticState
  rule: SutraRef
  trigger: Condition[]
  operation: Operation
  after: LinguisticState
}
```

So Pāṇini produces something like:

```text
dhātu / base
      ↓
semantic intention
      ↓
affix selection
      ↓
technical designation
      ↓
phonological operations
      ↓
conflict resolution
      ↓
surface form
```

And critically:

> **the derivation trace itself becomes knowledge.**

---

# Then Bruno renders the Pāṇinian process

This is where the two suddenly meet.

Suppose you’re learning a derivation.

Pāṇini gives:

```text
STATE 0
  ↓ rule A
STATE 1
  ↓ rule B
STATE 2
  ↓ rule C
WORD
```

That’s naturally:

### Bruno `CATENA`

So the system generates an imagined route.

Each rule is a gate.

Each transformation physically changes the object.

Rather than memorizing:

> rule X causes guṇa here.

you **watch the vowel transform while crossing the rule-locus**.

Eventually you don’t need the imagery.

You know the derivation.

The Brunian scaffold disappears.

---

# Pratyāhāras become a perfect spatial/combinatorial object

We already have the Māheśvara Sūtras.

Pāṇini gives us:

```ts
interface Phoneme {
  sound: string
  features: PhoneticFeatures
  sivaSutraPosition: Coordinate
}

interface Pratyahara {
  start: Phoneme
  marker: ItMarker
  expandsTo: Phoneme[]
}
```

So:

```text
अ इ उ ण्
ऋ ऌ क्
ए ओ ङ्
ऐ औ च्
...
```

isn’t merely text.

It’s an **address system**.

A pratyāhāra becomes a query:

```ts
expand("ac") => vowels
```

So Pāṇini already contains a kind of compressed symbolic indexing language.

Bruno then tells us how to make that indexing **visually and spatially executable in imagination**.

---

# And the phoneme becomes our universal atom

This is where Abhinavagupta joins.

```ts
interface Varna {
  id: string

  // physical
  articulation: Articulation
  acoustic: AcousticFeatures
  audio: AudioRef

  // graphic
  devanagari: string
  iast: string

  // panini
  sivaSutraPosition: Position
  pratyaharas: PratyaharaRef[]

  // trika
  attestedAssociations: SourceAssertion[]

  // bruno
  imaginalRepresentations: ImaginalRepresentation[]

  // learner
  personalAssociations: PersonalAssociation[]
}
```

Now one /ka/ is simultaneously:

```text
SOUND
    physical articulation

SYMBOL
    क / ka

PĀṆINIAN OBJECT
    memberships + transformations

TRIKA OBJECT
    only source-attested correspondences

BRUNIAN OBJECT
    locus + image + actions + links

PERSONAL OBJECT
    felt sensation / emotional association / imagery
```

That’s an insanely rich learning atom.

---

# Then Abhinavagupta supplies a third kind of operator

Bruno:

> **How shall this exist in imagination?**

Pāṇini:

> **How does this linguistic object transform?**

Trika:

> **What operation is performed with sound/body/attention?**

So we’d eventually define something like:

```ts
interface ExperientialOperator {
  modality:
    | "utterance"
    | "breath"
    | "visualization"
    | "attention"
    | "body-placement"
    | "recitation"
    | "recognition"

  locus?: BodyLocus
  sound?: VarnaRef[]
  visualization?: VisualizationSpec

  provenance: SourceAssertion[]
}
```

That last field is non-negotiable.

We must distinguish:

```ts
sourceAttested: true
```

from:

```ts
pedagogicalInvention: true
```

because otherwise our AI eventually invents some gorgeous chakra/phoneme correspondence and six months later we think Abhinavagupta said it.

---

# And finally the TEXT WORLD is just the compiled result

```ts
interface TextWorld {
  work: WorkRef

  semanticGraph: KnowledgeGraph

  languageRuntime: {
    phonemes: VarnaRef[]
    vocabulary: LexemeRef[]
    rules: PaniniRuleRef[]
    derivations: DerivationRef[]
  }

  imaginalRuntime: {
    operators: ImaginalOperatorRef[]
    loci: Locus[]
    objects: ImaginalObject[]
    routes: Route[]
  }

  experientialRuntime: {
    practices: ExperientialOperator[]
  }

  sourceLayer: {
    passages: PassageRef[]
    commentary: CommentaryRef[]
    assertions: SourceAssertion[]
  }

  learnerModel: LearnerWorldState
}
```

So compiling the **Śiva Sūtras** might produce:

```text
ŚIVA SŪTRAS
│
├── LANGUAGE
│   Sanskrit + morphology + derivations
│
├── SEMANTICS
│   concepts / arguments / dependencies
│
├── BRUNO
│   spatial architecture + chains + trees + images
│
├── TRIKA
│   attention / recitation / experiential operations
│
└── MEMORY
    your accumulated encounters + recalls + associations
```

And when you eventually compile **Tantrāloka**, it is the exact same format.

Just enormous.

---

# One more thing: don’t hardcode “30 Bruno operators” yet

This is important.

We should create:

```text
bruno/
  sources/
  seals/
    01-campus.ts
    02-caelum.ts
    03-catena.ts
    04-arbor.ts
    ...
  tests/
  mappings/
```

But each seal begins life as:

```ts
status: "uninterpreted"
```

Then we process:

```text
LATIN
↓
translation
↓
literal operation
↓
examples Bruno gives
↓
historical interpretation
↓
OUR computational abstraction
↓
tests on real knowledge
```

Only after that does it become `status: "implemented"`.

Because that forum thread demonstrates exactly the danger: within a few posts, actual Bruno gets mixed with extrapolations, modern mnemonics and outright LLM hallucination.

---

## The master architecture therefore becomes

```text
                         OPENPĀṬALA
                       SOURCE / TRUTH
                             │
                             ▼
                       KNOWLEDGE GRAPH
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
       PĀṆINI              BRUNO          ABHINAVAGUPTA
      linguistic           imaginal          embodied
       runtime             runtime            runtime
          │                  │                  │
          └──────────────────┼──────────────────┘
                             ▼
                       WORLD COMPILER
                             │
                             ▼
                        STONEDOORWAY
                             │
                             ▼
                           YOU
```

That is substantially better than treating Bruno, Pāṇini and Abhinavagupta as one syncretic doctrine.

They’re **three independent compilers operating over the same knowledge graph**.

And yes: once we’ve done Bruno computationally, we can do the same thing to **Pāṇini in frightening detail**—sūtras as executable rules, anuvṛtti as inherited scope, pratyāhāras as compressed sets, *it* markers as metadata, adhikāra as scopes, utsarga/apavāda as rule relations, derivations as traces, kārakas as semantic relations, sandhi as boundary transforms, samāsa as composition.

Then StoneDoorway can literally **render a Pāṇinian derivation as a Brunian world operation**.

That is the architecture I would freeze now.
