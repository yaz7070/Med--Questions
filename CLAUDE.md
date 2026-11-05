# Med Notes: rules for Claude

Quartz 5 site. Content lives in `content/`. Pushing to branch `v5` redeploys the site on Cloudflare Pages.

## Structure

- `content/index.md`: home page
- `content/fom/block-N/week-NN-slug.md`: one page per FoM week, Nicole's Notes as the base
- `content/fom/block-N/index.md`: block index, list every week page
- `content/question-bank/`: quizzes (HTML pages) plus `index.md` table linking them
- `content/lce/`: LCE clinical notes, de-identified only
- `content/templates/week.md`: template for new week pages (not published)

## Rules

1. Keep Nicole's Notes wording for facts, cutoffs and tables. Label anything added from outside the notes.
2. Put the student's own summaries in the "High-yield" callout at the top of each week.
3. New page: copy `templates/week.md`, add frontmatter tags `block-N` and `week-N`, then link it from the block index.
4. New quiz: build it with the med-school-quiz-builder skill, save to `content/question-bank/`, add a row to the index table.
5. No patient identifiers anywhere.
6. Run `npx quartz build` before pushing. Fix any errors first.
7. One commit per change, with a plain message ("Add Week 9 high-yield summary").

## Writing style

Clear, spartan, active voice. Short sentences. No em dashes or semicolons.
