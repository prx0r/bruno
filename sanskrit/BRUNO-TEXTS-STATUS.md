# Bruno texts — on-disk status (reviewed 2026-10-05)

> What we hold, what we lack, and what our docs may/may not claim.
> Texts live in `bruno/texts/` (106 MB, gitignored binaries stay local).

## On disk — primary Bruno

| File | Work | Status |
|------|------|--------|
| `ea_umbris.html` (+ `ea_umbris2.html`) | *De umbris idearum* (1582) | Esoteric Archives HTML — wheels + intentions/concepts. Our wheel PAO readings must be checked against THIS, not forum summaries |
| `ea_arsmemor.html` (+ `ea_arsmemor2.html`) | *Ars memoriae* | EA HTML |
| `bruno_ars_reminiscenti.html` | *Ars reminiscendi* + associated Sigilli material (EA) | 30 seal headings (DE CAMPO…DE INTERPRETE) verified present via grep — `triginta-sigilli-inventory.json` titles trace to THIS file |
| `ea_magia2.html` / `ea_theses.html` | *De magia* / *Theses de magia* | EA HTML — Notoria-mention context lives here |
| `ea_furori2.html` | *Eroici furori* | EA HTML |
| `bruno_de_imaginum_liano.pdf` | *De imaginum…* (Gómez de Liaño trans.) | Full book PDF |
| `ia_opera_vol2.pdf` / `ia_opera_tall.pdf` / `ia_bruni_vol.pdf` / `warburg_oplatII_I.pdf` | *Opera latine* scans (IA + Warburg) | Latin authority on disk for spot-checks |
| `sep_bruno.html` | SEP entry | Secondary overview, citable |

## NOT on disk — do not quote as consulted

- *Explicatio triginta sigillorum* full text (only TOC/headings via the EA reminiscendi file)
- *Sigillus sigillorum*, *Lampas triginta statuarum*, *De vinculis in genere*,
  *De causa / De infinito* (metaphysics behind the wheels)
- Greer *De umbris* translation, Gosnell translation, Sturlese critical edition
  (the GREER-PROVENANCE ladder names the standard; we hold none of its rungs yet)

## Consequences for our docs

1. `triginta-sigilli-inventory.json` — seal TITLES verified (EA HTML); per-seal
   OPERATIONS are ours (`status: interpreted`). Fixed 2026-10-05: `work` field
   now says this. Do not cite a seal's "operation" as Bruno's.
2. The "30 Ideas = Mind, Intellect, Reason…" list is flagged fabricated in
   BRUNO-WHEELS-IMAGINAL-COMPILER.md — keep that flag; never rehabilitate
   without Sturlese.
3. Wheel PAO structure (person/action/attribute/circumstance, 150 divisions)
   per GREER-PROVENANCE.md rests on Warburg reconstruction + forum — marked as
   such; confirm against `ea_umbris.html` before encoding anything new.
4. `bruno.md` Eso-teric-Archives/Warburg/artoformemory source list: local files
   confirmed present except Warburg browser-only PDFs (noted as browser-only —
   accurate).

## To acquire (browser, bots block us)

Explicatio full text → Sigillus → Vinculis → Lampas → Greer/Gosnell/Sturlese.
Order matters: seal operations stay `interpreted` until Explicatio lands.
