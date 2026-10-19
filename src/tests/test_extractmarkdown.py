import unittest

from extractmarkdown import (
    extract_markdown_images,
    extract_markdown_links,
    extract_title,
)


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_extract_title(self):
        match = extract_title(
            "# H1 Title"
        )
        self.assertEqual("H1 Title", match)

    def test_non_title(self):
        match = extract_title("## H2 Title")
        self.assertNotEqual("H2 Title", match)
