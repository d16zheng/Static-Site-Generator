import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("This is different text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_equal_text_type(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_url(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

    def test_url_none_vs_provided(self):
        node = TextNode("Text", TextType.TEXT)  # url defaults to None
        node2 = TextNode("Text", TextType.TEXT, None)
        self.assertEqual(node, node2)

    def test_url_none_vs_actual_url(self):
        node = TextNode("Text", TextType.TEXT)  # url defaults to None
        node2 = TextNode("Text", TextType.TEXT, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_different_types_with_same_values(self):
        node = TextNode("Code", TextType.CODE)
        node2 = TextNode("Code", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_link_with_url(self):
        node = TextNode("Click me", TextType.LINK, "https://google.com")
        node2 = TextNode("Click me", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_image_type(self):
        node = TextNode("Alt text", TextType.IMAGE, "image.png")
        node2 = TextNode("Alt text", TextType.IMAGE, "image.png")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Test text", TextType.BOLD, "https://test.com")
        expected = "TextNode(Test text, bold, https://test.com)"
        self.assertEqual(repr(node), expected)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_type_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)

    def test_text_type_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, None)

    def test_text_type_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, None)

    def test_text_type_code(self):
        node = TextNode("print('hello')", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")
        self.assertEqual(html_node.props, None)

    def test_text_type_link(self):
        node = TextNode("Click here", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_text_type_link_no_url(self):
        node = TextNode("Click here", TextType.LINK)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "Link TextNode must have a URL")

    def test_text_type_image(self):
        node = TextNode("A beautiful sunset", TextType.IMAGE, "sunset.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "sunset.jpg", "alt": "A beautiful sunset"})

    def test_text_type_image_no_url(self):
        node = TextNode("A beautiful sunset", TextType.IMAGE)
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "Image TextNode must have a URL")

    def test_invalid_text_type(self):
        # Create a TextNode with an invalid text type by modifying the enum value
        class InvalidTextType:
            value = "invalid"
        
        node = TextNode("Some text", InvalidTextType())
        with self.assertRaises(ValueError) as context:
            text_node_to_html_node(node)
        self.assertIn("Invalid text type", str(context.exception))

    def test_link_to_html_output(self):
        node = TextNode("Visit Google", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<a href="https://google.com">Visit Google</a>')

    def test_image_to_html_output(self):
        node = TextNode("Logo", TextType.IMAGE, "logo.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), '<img src="logo.png" alt="Logo">')

    def test_bold_to_html_output(self):
        node = TextNode("Important", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<b>Important</b>")

    def test_italic_to_html_output(self):
        node = TextNode("Emphasis", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<i>Emphasis</i>")

    def test_code_to_html_output(self):
        node = TextNode("const x = 5;", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "<code>const x = 5;</code>")

    def test_text_to_html_output(self):
        node = TextNode("Plain text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_link_with_special_chars(self):
        node = TextNode("Search & Find", TextType.LINK, "https://example.com/search?q=test")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Search & Find")
        self.assertEqual(html_node.props, {"href": "https://example.com/search?q=test"})


if __name__ == "__main__":
    unittest.main()