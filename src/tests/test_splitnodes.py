import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_bold(self):
        node = TextNode("**Warning** message", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Warning", TextType.TEXT),
                TextNode(" message", TextType.TEXT),
            ]
        )

    def test_italic(self):
        node = TextNode("I _love_ when you count me out", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("I ", TextType.TEXT),
                TextNode("love", TextType.ITALIC),
                TextNode(" when you count me out", TextType.TEXT),
            ]
        )

    def test_non_text(self):
        node = TextNode("`code`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("`code`", TextType.CODE)
            ]
        )

    def test_invalid(self):
        node = TextNode("This _should fail", TextType.TEXT)
        with self.assertRaisesRegex(ValueError, "invalid markdown syntax"):
            split_nodes_delimiter([node], "_", TextType.ITALIC)
