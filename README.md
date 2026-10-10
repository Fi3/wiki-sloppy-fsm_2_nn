# Finite state machines to neural networks

This is a test wiki for my website. Nothing interesting is expected to be found here.

A local, agent-maintained knowledge base about converting finite state machines into neural networks, implementing [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Original documents live in `raw/`; an agent compiles them into connected pages in `wiki/`. [AGENTS.md](AGENTS.md) defines the workflows and evidence conventions.

The first reading batch is now available: start with the [reading queue](wiki/questions/reading-queue.md), [current synthesis](wiki/synthesis.md), and [research roadmap](wiki/questions/research-roadmap.md). There are 30 first-pass source summaries and four unresolved retrieval/extraction cases. Raw captures are browser-extracted text rather than original PDF/HTML files; each capture records its coverage. A summary is not a claim that every proof or experiment has been checked.

## Start here

1. Open this directory in your agent and optionally as an Obsidian vault.
2. Tell the agent which machine, construction, or research question you want to understand.
3. Supply your first document or URL and say: “Ingest this source into the wiki.”
4. Browse [the index](wiki/index.md), ask questions, and keep adding sources.

No package installation or model API key is needed. Python 3.10+ is sufficient for the optional local helpers. The agent performs the reading and synthesis; the script handles file bookkeeping and validation.

## Use on another PC

This directory is a Git repository. Install Git to clone it and Python 3.10+ to run the optional helpers. If the repository is hosted or accessible through SSH, replace `REPOSITORY_URL` with its location:

```bash
git clone REPOSITORY_URL rsm-2-nn
cd rsm-2-nn
python3 scripts/wiki.py lint
```

For offline transfer, copy `rsm-2-nn.bundle` to the other PC and run `git clone rsm-2-nn.bundle rsm-2-nn`. A bundle includes the committed files and Git history; create a fresh bundle after additional commits using the command below.

You can read the Markdown files in any text editor or open the project root as an Obsidian vault. All sources, provenance records, wiki pages, templates, helper scripts, tests, and shared Obsidian settings are included. The helper locates the project from its own path, so no machine-specific paths or configuration are needed.

For an existing clone, you can also copy the entire project directory, including `.git/`, to the other PC. Python caches and Obsidian workspace state are ignored. Git preserves the exact bytes under `raw/` so source checksums remain valid across operating systems.

## Project layout

```text
raw/                  Original documents and assets; existing files are immutable
wiki/index.md         Catalog of every wiki page
wiki/log.md           Append-only history of ingests, saved queries, and maintenance
wiki/overview.md      Your topic, scope, and research goals
wiki/synthesis.md     Current understanding, disagreements, and open questions
wiki/sources/         Source summaries with citations to originals
wiki/concepts/        Knowledge integrated across sources
wiki/entities/        People, projects, organizations, and other named subjects
wiki/questions/       Reusable answers and analyses
templates/            Page formats for the agent
scripts/wiki.py       Local import, inventory, search, and lint helpers
```

## Useful prompts

- “Ingest `raw/my-paper.pdf`; focus on the assumptions and experimental evidence.”
- “What does the wiki say about X? Cite the supporting pages.”
- “Compare X and Y and save the analysis.”
- “Answer this in chat only.”
- “Health-check the wiki for contradictions, stale claims, and missing connections.”

## Local helpers

Run from this directory; the script also locates the project correctly when called elsewhere.

```bash
python3 scripts/wiki.py add /path/to/article.md --title "Article title" --url https://example.com/article
python3 scripts/wiki.py sources
python3 scripts/wiki.py search "your phrase"
python3 scripts/wiki.py lint
```

`add` copies a document into `raw/<title-slug>/document.<extension>` and writes `source.json` with its title, import time, optional original URL, and SHA-256 checksum. It refuses existing destinations. Importing does **not** summarize a source; ask the agent to ingest it. You can also place files directly in `raw/`, including `raw/assets/` for attachments. Those files do not get checksum protection until registered through an import, but the agent must still leave them unchanged.

`sources` marks imports `pending` until a source summary lists the document in its frontmatter. `search` performs case-insensitive literal search across wiki pages. `lint` checks inline local Markdown links, metadata, catalog coverage, evidence paths, source checksums, and orphan content pages; it exits with status 1 for errors. It checks target files, not heading anchors, reference-style links, or Obsidian wikilinks. It does not assess truth, completeness, or contradictions: those need the agent's content review.

Use the page templates rather than leaving empty placeholder pages in the wiki. Add claims only after reading evidence. Check each source page's review scope before treating a claim as a fully verified result.

## Obsidian and history

Open the project root as a vault to make both sources and compiled pages accessible. Standard relative Markdown links work without plugins. Optionally set the attachment folder to `raw/assets/`; inspect clipped images as well as text during ingestion.

Commit source imports and compiled updates together; keep private material private. Use `git status` to review changes, then commit the relevant files. To create an updated portable snapshot after committing, run:

```bash
git bundle create rsm-2-nn.bundle --all
```

To verify the helpers themselves:

```bash
python3 -m unittest discover -s tests -v
```
