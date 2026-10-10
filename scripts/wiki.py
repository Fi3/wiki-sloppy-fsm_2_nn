#!/usr/bin/env python3
"""Local wiki bookkeeping. Reading and synthesis belong to the agent."""

import argparse
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = {"sources": "source", "concepts": "concept", "entities": "entity", "questions": "question"}
NAVIGATION = {"index.md", "log.md"}


def checksum(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def metadata(text):
    """Read the deliberately small frontmatter format documented in AGENTS.md."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}
    result = {}
    for line in lines[1:]:
        if line == "---":
            return result
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return {}  # An unclosed block is invalid.


def evidence(meta):
    paths = json.loads(meta.get("sources", "[]"))
    if not isinstance(paths, list) or not all(isinstance(path, str) for path in paths):
        raise ValueError("sources must be a JSON-style list of quoted paths")
    return paths


def local_links(text):
    # Ignore fenced and inline code: examples are not navigational links.
    text = re.sub(r"^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text, flags=re.M | re.S)
    text = re.sub(r"`[^`\n]+`", "", text)
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", text):
        target = match.group(1).strip("<>")
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        yield unquote(parts.path)


def pages(root):
    return {path.resolve(): path.read_text(encoding="utf-8") for path in sorted((root / "wiki").rglob("*.md"))}


def raw_path(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to((root / "raw").resolve()) or not path.is_file():
        raise ValueError(f"missing or non-raw evidence: {value}")
    return path


def add_source(root, source, title, url=None):
    source = source.resolve()
    if not source.is_file():
        raise ValueError(f"not a source file: {source}")
    slug = re.sub(r"[^\w]+", "-", unicodedata.normalize("NFKC", title).lower()).strip("-_")
    if not slug:
        raise ValueError("title must contain letters or numbers")
    destination = root / "raw" / slug
    destination.mkdir(parents=True, exist_ok=False)
    try:
        document = destination / ("document" + source.suffix.lower())
        shutil.copyfile(source, document)
        record = {
            "title": title,
            "document": document.relative_to(root).as_posix(),
            "original_filename": source.name,
            "url": url,
            "imported_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sha256": checksum(document),
        }
        (destination / "source.json").write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception:
        shutil.rmtree(destination)  # Only the new, incomplete import is removed.
        raise
    return record


def source_inventory(root):
    summarized = set()
    for path, text in pages(root).items():
        if path.parent.name == "sources":
            try:
                summarized.update(evidence(metadata(text)))
            except (ValueError, TypeError):
                pass  # lint reports malformed pages.
    for manifest in sorted((root / "raw").rglob("source.json")):
        record = json.loads(manifest.read_text(encoding="utf-8"))
        yield ("summarized" if record["document"] in summarized else "pending", record)


def lint(root):
    root = root.resolve()
    texts = pages(root)
    issues = []
    inbound = {path: set() for path in texts}
    index = root / "wiki" / "index.md"
    catalog = set()

    def report(level, path, message):
        issues.append((level, path.relative_to(root).as_posix(), message))

    for required in ("index.md", "log.md", "overview.md", "synthesis.md"):
        path = root / "wiki" / required
        if path not in texts:
            report("ERROR", path, "required wiki file is missing")

    for path, text in texts.items():
        for target in local_links(text):
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                report("ERROR", path, f"broken or outside-project link: {target}")
            if resolved in inbound:
                if path != resolved:
                    inbound[resolved].add(path)
                if path == index:
                    catalog.add(resolved)
        if path.name in NAVIGATION and path.parent == root / "wiki":
            continue
        meta = metadata(text)
        for field in ("title", "type", "created", "updated", "status", "sources"):
            if not meta.get(field):
                report("ERROR", path, f"missing frontmatter field: {field}")
        if meta.get("type") not in {*CONTENT_DIRS.values(), "overview"}:
            report("ERROR", path, "invalid page type")
        expected = CONTENT_DIRS.get(path.parent.name)
        if expected and meta.get("type") != expected:
            report("ERROR", path, f"this directory requires type: {expected}")
        if meta.get("status") not in {"draft", "active", "superseded"}:
            report("ERROR", path, "invalid page status")
        dates = {}
        for field in ("created", "updated"):
            try:
                value = meta.get(field, "")
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError()
                dates[field] = date.fromisoformat(value)
            except ValueError:
                report("ERROR", path, f"invalid {field} date")
        if len(dates) == 2 and dates["updated"] < dates["created"]:
            report("ERROR", path, "updated date precedes created date")
        try:
            sources = evidence(meta)
            for value in sources:
                raw_path(root, value)
            if meta.get("type") == "source" and not sources:
                report("ERROR", path, "source summary requires raw evidence")
            elif meta.get("status") == "active" and not sources:
                report("WARN", path, "active page has no raw evidence")
        except (ValueError, TypeError) as error:
            report("ERROR", path, f"invalid evidence: {error}")

    for path in texts:
        if path != index and path not in catalog:
            report("ERROR", path, "page is missing from wiki/index.md")
        if path.parent.name in CONTENT_DIRS and not (inbound[path] - {index}):
            report("WARN", path, "no incoming links from another wiki content page")

    for manifest in sorted((root / "raw").rglob("source.json")):
        try:
            record = json.loads(manifest.read_text(encoding="utf-8"))
            document = raw_path(root, record["document"])
            if checksum(document) != record["sha256"]:
                report("ERROR", manifest, "imported source checksum has changed")
        except (ValueError, KeyError, TypeError, OSError) as error:
            report("ERROR", manifest, f"invalid source manifest: {error}")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="copy an original into raw/ without overwriting")
    add.add_argument("path", type=Path)
    add.add_argument("--title", required=True)
    add.add_argument("--url")
    commands.add_parser("sources", help="list imported sources and summary status")
    search = commands.add_parser("search", help="literal, case-insensitive wiki search")
    search.add_argument("query")
    commands.add_parser("lint", help="check structure, links, metadata, and source integrity")
    args = parser.parse_args()
    try:
        if args.command == "add":
            record = add_source(ROOT, args.path, args.title, args.url)
            print(f"Imported {record['document']}; ask the agent to ingest it.")
        elif args.command == "sources":
            inventory = list(source_inventory(ROOT))
            for status, record in inventory:
                print(f"{status}\t{record['document']}\t{record['title']}")
            if not inventory:
                print("No registered imports. Add a source or inspect raw/ for manually supplied files.")
        elif args.command == "search":
            matches = 0
            for path, text in pages(ROOT).items():
                for line_number, line in enumerate(text.splitlines(), 1):
                    if args.query.casefold() in line.casefold():
                        print(f"{path.relative_to(ROOT)}:{line_number}: {line}")
                        matches += 1
            if not matches:
                print("No matching wiki lines.")
        else:
            issues = lint(ROOT)
            for level, path, message in issues:
                print(f"{level} {path}: {message}")
            errors = sum(level == "ERROR" for level, _, _ in issues)
            warnings = len(issues) - errors
            print(f"Checked {len(pages(ROOT))} wiki pages: {errors} errors, {warnings} warnings.")
            return 1 if errors else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
