from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_site import check_site


class CheckSiteTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "style.css").write_text("body { margin: 0; }", encoding="utf-8")

    def check(self, html):
        (self.root / "index.html").write_text(html, encoding="utf-8")
        check_site(self.root)

    def test_valid_links_svg_and_accessibility_references(self):
        self.check('''<!doctype html><html><head><link href="./style.css" /></head>
            <body><h1 id="title">Title</h1><main id="main" aria-labelledby="title">
            <a href="./index.html#main">Main</a><a href="https://example.com">External</a>
            <svg><symbol id="icon"><path d="M0 0" /></symbol><use href="#icon"></use></svg>
            </main></body></html>''')

    def test_rejects_malformed_structure(self):
        for html in ("<div><p></div>", "<div>", '<p id="same"></p><p id="same"></p>', '<p id="a" id="b"></p>'):
            with self.subTest(html=html), self.assertRaises(ValueError):
                self.check(html)

    def test_rejects_broken_references(self):
        for html in ('<img src="missing.png">', '<a href="#missing">Link</a>', '<div aria-controls="missing"></div>'):
            with self.subTest(html=html), self.assertRaises(ValueError):
                self.check(html)

    def test_rejects_empty_files(self):
        (self.root / "empty.css").touch()
        with self.assertRaisesRegex(ValueError, "Missing or empty file"):
            self.check('<link href="empty.css">')

    def test_rejects_paths_outside_the_site(self):
        for path in ("../outside.css", "/style.css", "%2e%2e/outside.css"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                self.check(f'<link href="{path}">')


if __name__ == "__main__":
    unittest.main()
