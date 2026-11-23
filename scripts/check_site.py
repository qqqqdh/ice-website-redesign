from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class SiteHTML(HTMLParser):
    void_tags = set("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.ids = set()
        self.references = []
        self.files = []

    def handle_starttag(self, tag, attrs):
        if len(attrs) != len(dict(attrs)):
            raise ValueError(f"Duplicate attribute on <{tag}>")
        attrs = dict(attrs)
        if "id" in attrs:
            identifier = attrs["id"]
            if not identifier or identifier in self.ids:
                raise ValueError(f"Empty or duplicate id: {identifier!r}")
            self.ids.add(identifier)
        for name in ("aria-controls", "aria-labelledby", "aria-describedby"):
            self.references.extend((attrs.get(name) or "").split())
        for name in ("src", "href"):
            if attrs.get(name):
                self.files.append(attrs[name])
        if tag not in self.void_tags:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if not self.stack or self.stack[-1] != tag:
            raise ValueError(f"Unexpected closing tag: </{tag}>")
        self.stack.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.void_tags:
            self.handle_endtag(tag)


def check_site(root):
    root = root.resolve()
    index = root / "index.html"
    page = SiteHTML()
    page.feed(index.read_text(encoding="utf-8"))
    page.close()
    if page.stack:
        raise ValueError(f"Unclosed tags: {', '.join(page.stack)}")

    for reference in page.files:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        if url.path.startswith("/"):
            raise ValueError(f"Use a relative path for GitHub Pages: {reference}")
        target = (root / unquote(url.path)).resolve() if url.path else index
        if not target.is_relative_to(root):
            raise ValueError(f"Reference leaves the site directory: {reference}")
        if not target.is_file() or target.stat().st_size == 0:
            raise ValueError(f"Missing or empty file: {reference}")
        if target == index and url.fragment:
            page.references.append(unquote(url.fragment))

    for identifier in page.references:
        if identifier not in page.ids:
            raise ValueError(f"Missing target id: {identifier}")


if __name__ == "__main__":
    check_site(Path(__file__).resolve().parents[1])
    print("HTML structure, local files and ID references passed.")
