# Med Notes: rules for Claude

Quartz 5 site. Content lives in `content/`. Pushing to branch `v5` redeploys the site on Cloudflare Workers.

## Structure

- `content/index.md`: home page
- `content/fom/block-N/week-NN-slug.md`: one page per FoM week, Nicole's Notes as the base
- `content/fom/block-N/index.md`: block index, list every week page
- `content/fom/block-N/question-bank/`: one wrapper page per quiz, plus `index.md` table
- `content/fom/block-N/flowcharts/`: one wrapper page per flowchart, plus `index.md` table
- `quartz/static/pages/slug.html`: raw quiz and flowchart HTML, embedded by wrapper pages via iframe to `/static/pages/slug.html`
- `content/question-bank/index.md`: overview of every quiz across blocks
- `content/templates/week.md`: template for new week pages (not published)

## Rules

1. Keep Nicole's Notes wording for facts, cutoffs and tables. Label anything added from outside the notes.
2. Put the student's own summaries in the "High-yield" callout at the top of each week.
3. New page: copy `templates/week.md`, add frontmatter tags `block-N` and `week-N`, then link it from the block index.
4. New quiz or flowchart: save the HTML to `quartz/static/pages/`, add a wrapper page in the block's `question-bank/` or `flowcharts/` folder (copy an existing one), add a row to that folder's index, and for quizzes to `content/question-bank/index.md`.
5. Block 1 and 2 week pages are intentionally blank. Do not refill them unless asked.
6. No patient identifiers anywhere.
7. Run `npx quartz build` before pushing. Fix any errors first.
8. One commit per change, with a plain message ("Add Week 9 high-yield summary").

## Writing style

Clear, spartan, active voice. Short sentences. No em dashes or semicolons.
