import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_multiple_prop(self):
        node = HTMLNode("a", "Boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"},)
        expected = ' href="https://www.boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_single_prop(self):
        node = HTMLNode("h2", "Palpatine Quotes:", props={"class": "character"},)
        expected = ' class="character"'
        self.assertEqual(node.props_to_html(), expected)

    def test_empty_prop(self):
        node = HTMLNode("p", "Something something dark side...",)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

if __name__ == "__main__":
    unittest.main()
