import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Important stuff")
        self.assertEqual(node.to_html(), "<b>Important stuff</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Proceed to checkout", {"href": "https://www.amazon.com/checkout"})
        self.assertEqual(node.to_html(), '<a href="https://www.amazon.com/checkout">Proceed to checkout</a>')


if __name__ == "__main__":
    unittest.main()
