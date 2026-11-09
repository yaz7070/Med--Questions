# Differential: rules for Claude

Quartz 5 site. Content lives in `content/`. Pushing to branch `v5` redeploys the site on Netlify (config in netlify.toml).

## Structure

- `content/index.md`: home page
- `content/fom/block-N/week-NN-slug.md`: one page per FoM week, Nicole's Notes as the base
- `content/fom/block-N/index.md`: block index, list every week page
- `content/fom/block-N/question-bank/`: one wrapper page per quiz, plus `index.md` table
- `content/fom/block-N/flowcharts/`: one wrapper page per flowchart, plus `index.md` table
- `quartz/static/pages/slug.html`: raw quiz and flowchart HTML, embedded by wrapper pages via iframe to `/static/pages/slug.html`
- `content/question-bank/index.md`: overview of every quiz across blocks
- `content/templates/week.md`: template for new week pages (not published)

## Page style

- Site name: Differential. Teal accent (--secondary), styles in `quartz/styles/custom.scss`.
- Home, block, folder and question bank pages use raw HTML lists: `<ul class="rows">` with `<a class="row">` items (strong title + span.desc). Home uses `.hero`, `.blocks`/`.block-row`, `.chip`. Buttons use `.btn` and `.btn.primary`.
- `scripts/items.py` lists every quiz, practice test and flowchart. `python3 scripts/site_pages.py` regenerates all wrapper, folder, block and home pages from it.
- Quiz pages share one template: `scripts/quiz/template.html`. Question data lives in `scripts/quiz/data/<slug>.json` ({title, context, questions, objectives}). Run `python3 scripts/quiz/build.py` to write every quiz to `quartz/static/pages/`. Never hand-edit the built quiz HTML. Change the template or the data, then rebuild. Each block has `question-bank/` (one bank per week, no duplicates across banks), `practice-tests/` (full block tests) and `flowcharts/`.

- Layout: custom page frame `quartz/components/frames/DifferentialFrame.tsx` (no sidebars, top bar with title, nav, search and theme toggle, footer with credits and disclaimer). Set via `template: differential` in `quartz.config.yaml`. Edit credits or the disclaimer in that file.

## Rules

1. Keep Nicole's Notes wording for facts, cutoffs and tables. Label anything added from outside the notes.
2. Put the student's own summaries in the "High-yield" callout at the top of each week.
3. New page: copy `templates/week.md`, add frontmatter tags `block-N` and `week-N`, then link it from the block index.
4. New quiz or flowchart: save the HTML to `quartz/static/pages/`, add a wrapper page in the block's `question-bank/` or `flowcharts/` folder (copy an existing one), add a row to that folder's index, and for quizzes to `content/question-bank/index.md`.
5. Blocks 1 and 2 have no weekly notes pages. Do not add them unless asked.
6. No patient identifiers anywhere.
7. Run `npx quartz build` before pushing. Fix any errors first.
8. One commit per change, with a plain message ("Add Week 9 high-yield summary").

## Writing style

Clear, spartan, active voice. Short sentences. No em dashes or semicolons.
