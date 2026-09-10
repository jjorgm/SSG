import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is link node", TextType.LINKS, "www.somelink.com")
        node2 = TextNode("This is an image node", TextType.IMAGES, "/imagefolder/someimage.png")
        self.assertNotEqual(node, node2)

    def test_url_empty(self):
        node = TextNode("This url argument is empty", TextType.LINKS)
        node2 = TextNode("This url arugment is not empty", TextType.LINKS, "www.somelink.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
