import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("wiki_helpers", PROJECT / "scripts" / "wiki.py")
wiki = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(wiki)


class WikiTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "vault"
        self.root.mkdir()
        (self.root / "wiki" / "sources").mkdir(parents=True)
        (self.root / "wiki" / "index.md").write_text(
            '# Index\n[Overview](overview.md)\n[Synthesis](synthesis.md)\n[Log](log.md)\n', encoding="utf-8",
        )
        (self.root / "wiki" / "log.md").write_text("# Log\n", encoding="utf-8")
        for name in ("overview", "synthesis"):
            (self.root / "wiki" / f"{name}.md").write_text(
                f'---\ntitle: "Fixture {name}"\ntype: overview\ncreated: 2026-10-07\n'
                f'updated: 2026-10-07\nstatus: draft\nsources: []\n---\n\n# Fixture {name}\n',
                encoding="utf-8",
            )
        (self.root / "raw").mkdir()
        self.original = Path(self.temporary.name) / "input.md"
        self.original.write_text("# Test source\nEvidence for a test.\n", encoding="utf-8")

    def import_source(self):
        return wiki.add_source(self.root, self.original, "Test source", "https://example.com/source")

    def make_summary(self, document):
        path = self.root / "wiki" / "sources" / "test-source.md"
        path.write_text(
            '---\ntitle: "Test source"\ntype: source\ncreated: 2026-10-07\n'
            f'updated: 2026-10-07\nstatus: active\nsources: {json.dumps([document])}\n'
            f'---\n\n# Test source\n\n[Original](../../{document})\n',
            encoding="utf-8",
        )
        with (self.root / "wiki" / "index.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[Test source](sources/test-source.md) — Test summary.\n")
        with (self.root / "wiki" / "synthesis.md").open("a", encoding="utf-8") as stream:
            stream.write("\nEvidence: [Test source](sources/test-source.md).\n")
        return path

    def test_initial_structure_is_valid(self):
        self.assertEqual(wiki.lint(self.root), [])

    def test_import_preserves_original_and_refuses_overwrite(self):
        original_bytes = self.original.read_bytes()
        record = self.import_source()
        document = self.root / record["document"]
        self.assertEqual(document.read_bytes(), original_bytes)
        self.assertEqual(self.original.read_bytes(), original_bytes)
        self.assertEqual(record["sha256"], wiki.checksum(document))
        self.assertEqual(record["url"], "https://example.com/source")
        self.original.write_text("A different source", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            self.import_source()
        self.assertEqual(document.read_bytes(), original_bytes)

    def test_inventory_changes_only_after_summary_and_valid_ingestion(self):
        record = self.import_source()
        self.assertEqual(list(wiki.source_inventory(self.root))[0][0], "pending")
        self.make_summary(record["document"])
        self.assertEqual(list(wiki.source_inventory(self.root))[0][0], "summarized")
        self.assertEqual(wiki.lint(self.root), [])

    def test_changed_import_is_detected(self):
        record = self.import_source()
        (self.root / record["document"]).write_text("tampered", encoding="utf-8")
        self.assertTrue(any("checksum has changed" in message for _, _, message in wiki.lint(self.root)))

    def test_broken_links_and_uncatalogued_pages_are_detected(self):
        record = self.import_source()
        path = self.make_summary(record["document"])
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing](missing.md)\n")
        shutil.copyfile(path, path.with_name("uncatalogued.md"))
        issues = wiki.lint(self.root)
        self.assertTrue(any("broken or outside-project link" in message for _, _, message in issues))
        self.assertTrue(any("missing from wiki/index.md" in message for _, _, message in issues))

    def test_evidence_cannot_escape_raw(self):
        record = self.import_source()
        path = self.make_summary(record["document"])
        text = path.read_text(encoding="utf-8").replace(record["document"], "../input.md", 1)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("missing or non-raw evidence" in message for _, _, message in wiki.lint(self.root)))

    def test_code_examples_are_not_links(self):
        text = '[Real](real.md)\n`[Inline](missing.md)`\n```markdown\n[Example](missing.md)\n```\n'
        self.assertEqual(list(wiki.local_links(text)), ["real.md"])

    def test_unicode_titles_and_encoded_links(self):
        record = wiki.add_source(self.root, self.original, "机器 & café")
        self.assertTrue(record["document"].startswith("raw/机器-café/"))
        self.assertEqual(list(wiki.local_links('[Page](<a%20b.md>)')), ["a b.md"])

    def test_cli_locates_project_from_another_directory(self):
        (self.root / "scripts").mkdir()
        script = self.root / "scripts" / "wiki.py"
        shutil.copyfile(PROJECT / "scripts" / "wiki.py", script)
        result = subprocess.run(
            [sys.executable, str(script), "search", "FIXTURE OVERVIEW"],
            cwd=self.temporary.name, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("wiki/overview.md:", result.stdout)


if __name__ == "__main__":
    unittest.main()
