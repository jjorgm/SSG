import unittest

from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("### Heading3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("""```
            some code
        ```"""), BlockType.CODE)
        self.assertEqual(block_to_block_type("> A famous quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("""1. Ordered list item
            2. Second item
            """), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
