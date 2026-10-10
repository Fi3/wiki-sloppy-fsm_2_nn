# LLM wiki instructions

This directory is a local knowledge base inspired by [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). Maintain the wiki as persistent, evidence-backed knowledge. Read this file, `wiki/index.md`, and the latest entries in `wiki/log.md` before working.

## Layout and ownership

- `raw/`: original sources and attachments. Read them; never edit, overwrite, rename, or delete existing sources. New imports are allowed when the user supplies a source or requests research. Extracted text from a PDF or other binary goes in its own new file, with a link to the original.
- `wiki/`: maintained Markdown pages. You may create and update these within the user's requested work.
- `templates/`: starting points for source, concept, entity, and question pages.
- `scripts/wiki.py`: dependency-free helpers for importing files, listing pending sources, searching, and structural linting.
- `README.md`: human-facing instructions. This file is the agent-facing schema.

The topic is converting finite state machines into neural networks. The user established this scope on 2026-10-07. Start from `wiki/overview.md` for research goals. Distinguish explicit construction from learning an approximation, and distinguish a finite state machine from other machine models. When reading a construction, capture the machine definition, state/input/output encodings, network architecture and parameters, execution semantics, correctness argument, limitations, and tests. Do not assume the title of this directory specifies a particular machine or architecture.

## Current intake and capture conventions

The first batch is cataloged in `wiki/questions/reading-queue.md`. It has first-pass summaries and explicit remaining work; do not treat these as full-paper audits. `raw/reading-list-original-order.md` is the canonical user list. The earlier `raw/reading-list.md` capture grouped URLs despite its original-order label and is retained unchanged.

Direct shell downloads were unavailable in the intake session. Successful captures live in `raw/<source-id>/document.txt` as browser-extracted text, with `source.json` recording the checksum and `capture.json` recording captured URLs and missing line ranges. These are not original PDF/HTML bytes. Browser line coverage is distinct from review coverage; equations, figures and assets may still be missing. PDF page labels in the extraction are zero-based. Capture any recovered original or additional extraction as a new file; never overwrite an existing snapshot.

Source summaries may include `review: first-pass` and must describe the reviewed sections and remaining work. Preserve these limits when querying or extending them. Upgrade review descriptions only after actually reading the missing material. The helper's `summarized` status only means a source summary references the raw file; use the queue and source page for review completeness. Inaccessible sources stay unresolved in the queue, with no invented source summary or bibliographic details.

## Page conventions

- Use descriptive lowercase hyphenated filenames. Put source summaries in `wiki/sources/`, concepts in `wiki/concepts/`, entities in `wiki/entities/`, and saved answers in `wiki/questions/`.
- Use the templates' frontmatter fields: `title`, `type`, `created`, `updated`, `status`, and `sources`. Dates are `YYYY-MM-DD`; types are `source`, `concept`, `entity`, `question`, or `overview`. Status is `draft`, `active`, or `superseded`.
- `sources` is a JSON-style YAML list of quoted paths relative to the project root, pointing to evidence in `raw/`, for example `["raw/example/document.md"]`. Use `[]` for navigation or pages with no evidence yet. JSON quoting also works for titles containing punctuation.
- Use inline relative Markdown links (`[Title](relative/path.md)`), including `.md`, so pages work in Obsidian and normal Markdown readers and the linter can check them. Cite evidence near the claim, linking either directly to a raw source or to a source summary that links to the original. For PDFs, include page numbers; for books, chapter/section; for web sources, preserve the URL and retrieval date when known.
- Separate sourced facts from interpretation, uncertainty, and open questions. Never invent bibliographic information, dates, quotations, or source contents. Use short quotations and original summaries, rather than copying large passages.
- Keep one page per distinct concept/entity and reuse existing pages. Connect relevant pages with contextual links. Add every page to `wiki/index.md` with a one-line description.
- Update `updated` on changed content pages. Log entries use `## [YYYY-MM-DD] operation | Description`. `wiki/log.md` is append-only.

## Ingest

1. Read the index and inspect existing pages relevant to the source. Use `python3 scripts/wiki.py sources` to find imported sources with no summary yet.
2. If the source is outside `raw/`, import it with `python3 scripts/wiki.py add PATH --title "Title"`, optionally supplying `--url` for provenance. The command copies it without changing the original, records a checksum, and refuses name collisions. For a supplied URL, retrieve the actual content using available tools and save a new snapshot under `raw/`; record its original URL and retrieval date. A link alone is not evidence that the content was read.
3. Read the complete source when feasible. For oversized material, process in labeled sections and explicitly record the coverage. For images, inspect them separately; for binary material, use available extraction tools and state extraction limitations.
4. Create a source summary using `templates/source.md`: bibliographic details, main claims, useful evidence, caveats, connections, and open questions. Link to the original and include its raw path in frontmatter.
5. Update relevant concept/entity pages and `wiki/synthesis.md` when the new evidence affects them. Preserve conflicting claims with their sources and dates; explain uncertainty instead of silently resolving disagreement. Newer evidence alone does not establish that a claim is correct.
6. Update the index and append an ingest entry with source and affected-page links. Do not claim ingestion is complete until these changes exist.
7. Run `python3 scripts/wiki.py lint`, fix structural errors, and report the key takeaways and any unresolved conflicts or coverage limits.

Process sources one at a time unless the user requests a batch. Routine wiki updates within an authorized ingest do not require another approval.

## Query

1. Start with the index, search as needed, and read the relevant pages. Follow citations back to raw evidence when needed for accuracy.
2. Answer with links supporting the claims. State when the wiki lacks evidence. Distinguish wiki knowledge from new external research; browse when required for current information.
3. Save substantial reusable comparisons, analyses, and connections in `wiki/questions/` as part of wiki exploration, unless the user asks for a chat-only answer. Do not save trivial replies or duplicate pages. Include the question, answer, supporting sources, assumptions, and unresolved points.
4. If saving, update related pages and the index, append a query entry, and run lint. Chat-only answers need no wiki mutation.

## Maintain / lint

Run the structural linter first. It checks imported-source integrity, required metadata, local links, evidence paths, catalog coverage, and orphan content pages. It cannot judge claims or contradictions.

Then review relevant content for conflicting claims, newer evidence, stale summaries, missing connections, missing concept pages, and unanswered questions. Do not turn a missing link into invented knowledge. Fix supported issues, record unresolved issues in `wiki/synthesis.md`, and suggest specific next sources or questions. Append a lint entry describing the scope, findings, and fixes. Refresh the index after creating or moving pages; avoid moves that break inbound links.

## Scope

Keep this a plain-file wiki. No embeddings, database, hosted site, scheduled jobs, external messages, or API-key setup are needed. Add infrastructure only for a concrete user need. Preserve user-authored content and unrelated files. Do not edit `.git/`, `.agents/`, `.codex/`, or `.aws/`.
