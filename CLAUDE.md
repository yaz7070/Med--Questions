# Nexus: rules for Claude

Quartz 5 site. Content lives in `content/`. Pushing to branch `v5` redeploys the site on GitHub Pages via `.github/workflows/deploy.yml` (live at https://yaz7070.github.io/Med--Questions/).

## Structure

The site has three kinds of page and nothing else:

- `content/index.md`: home. Overall progress, a Continue link, and one row per block.
- `content/fom/block-N/index.md`: block page. Lists that block's weekly banks, practice tests and flowcharts, with progress on every row.
- `content/fom/block-N/{question-bank,practice-tests,flowcharts}/<slug>.md`: wrapper page. One slim line (block link, title, full screen link), then an iframe of `/static/pages/<slug>.html`.

Old addresses (`/question-bank/`, `/flowcharts/`, `/progress/`, `/fom/`, and the folder indexes) are "Moved" stubs that forward to the home or block page. Do not bring those pages back: they repeated the same lists.

All of these are generated. `scripts/items.py` lists every quiz, practice test and flowchart. `python3 scripts/site_pages.py` regenerates every page from it. Never hand-edit generated pages.

## Page style

- Site name: Nexus. Internal names (the frame "differential", quiz storage keys "differential-<slug>") keep the old name on purpose: renaming the keys would wipe saved progress.
- One typeface: Atkinson Hyperlegible Next. Neutral greys for the page. Compact rows, small radii, no pills, no big hero.
- Colour belongs to the blocks: Block 1 teal, Block 2 indigo, Block 3 berry, Block 4 amber (`--b1` to `--b4` in `quartz/styles/custom.scss`, repeated in `scripts/quiz/template.html`). Block 3 is not red, so it never reads as a wrong answer. A page picks its colour from its address (`fom/block-N`) or a `data-b="N"` attribute.
- Progress on home and block pages comes from the inline script that `site_pages.py` writes (`PROG_JS`). It reads each quiz's saved answers from localStorage.
- Quiz pages share one template: `scripts/quiz/template.html`. Question data lives in `scripts/quiz/data/<slug>.json` ({title, context, questions, objectives}). Run `python3 scripts/quiz/build.py` to write every quiz to `quartz/static/pages/`. Change the template or the data, then rebuild. The quiz takes its block colour from `items.py` and follows the site's light or dark toggle.
- Layout: custom page frame `quartz/components/frames/DifferentialFrame.tsx` (no sidebars, top bar with title, four block links, search and theme toggle, footer with credits and disclaimer). Top nav links are in `NAV` there and are rendered relative to each page, so the site works under `/Med--Questions/` or any domain. Content links stay root-relative (`/fom/...`) and Quartz rewrites them.

## Rules

1. Keep Nicole's Notes wording for facts, cutoffs and tables. Label anything added from outside the notes.
2. Put the student's own summaries in the "High-yield" callout at the top of each week.
3. New page: copy `templates/week.md`, add frontmatter tags `block-N` and `week-N`, then link it from the block index.
4. New quiz or flowchart: add the data file (quiz) or HTML (flowchart), add one entry to `scripts/items.py`, then run `scripts/quiz/build.py` and `scripts/site_pages.py`.
5. No block has weekly notes pages. Do not add them unless asked.
6. No patient identifiers anywhere.
7. Run `npx quartz build` before pushing. Fix any errors first.
8. One commit per change, with a plain message ("Add Week 9 high-yield summary").

## Writing style

Clear, spartan, active voice. Short sentences. No em dashes or semicolons.
