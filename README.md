# Nexus

Study hub for Schulich MD2030, built with [Quartz](https://quartz.jzhao.xyz).

- Notes live in `content/` as Markdown.
- Every push to `v5` rebuilds the site on GitHub Pages (https://yaz7070.github.io/Med--Questions/).
- Rules for Claude live in `CLAUDE.md`.

## Run locally

```bash
npm ci
npx quartz plugin install
npx quartz build --serve
```

Open http://localhost:8080.
