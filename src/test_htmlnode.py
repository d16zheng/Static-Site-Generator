import unittest 

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            "class": "link"
        })
        expected = ' href="https://www.google.com" target="_blank" class="link"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://boot.dev"})
        expected = "HTMLNode(tag=a, value=Click me, children=None, props={'href': 'https://boot.dev'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_node_with_children(self):
        child1 = HTMLNode("span", "child1")
        child2 = HTMLNode("span", "child2")
        parent = HTMLNode("div", None, [child1, child2])
        self.assertEqual(parent.children, [child1, child2])
        self.assertIsNone(parent.value)

    def test_node_with_value(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertIsNone(node.children)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("div", "Content", {"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<div class="container" id="main">Content</div>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_empty_string_value(self):
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_leaf_to_html_heading(self):
        node = LeafNode("h1", "Main Title")
        self.assertEqual(node.to_html(), "<h1>Main Title</h1>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Inline text", {"style": "color: red;"})
        self.assertEqual(node.to_html(), '<span style="color: red;">Inline text</span>')

    def test_leaf_repr(self):
        node = LeafNode("a", "Link", {"href": "https://example.com"})
        expected = "LeafNode(tag=a, value=Link, props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

    def test_leaf_children_none(self):
        node = LeafNode("p", "Text")
        self.assertIsNone(node.children)
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            "class": "link"
        })
        expected = ' href="https://www.google.com" target="_blank" class="link"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Hello")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://boot.dev"})
        expected = "HTMLNode(tag=a, value=Click me, children=None, props={'href': 'https://boot.dev'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_node_with_children(self):
        child1 = HTMLNode("span", "child1")
        child2 = HTMLNode("span", "child2")
        parent = HTMLNode("div", None, [child1, child2])
        self.assertEqual(parent.children, [child1, child2])
        self.assertIsNone(parent.value)

    def test_node_with_value(self):
        node = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertIsNone(node.children)

    def test_leaf_node(self):
        node = HTMLNode(tag="p", value="Hello World")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello World")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("div", "Content", {"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<div class="container" id="main">Content</div>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_empty_string_value(self):
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_leaf_to_html_heading(self):
        node = LeafNode("h1", "Main Title")
        self.assertEqual(node.to_html(), "<h1>Main Title</h1>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Inline text", {"style": "color: red;"})
        self.assertEqual(node.to_html(), '<span style="color: red;">Inline text</span>')

    def test_leaf_repr(self):
        node = LeafNode("a", "Link", {"href": "https://example.com"})
        expected = "LeafNode(tag=a, value=Link, props={'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)

    def test_leaf_children_none(self):
        node = LeafNode("p", "Text")
        self.assertIsNone(node.children)


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_to_html_no_children(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", None)
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_to_html_empty_children(self):
        with self.assertRaises(ValueError) as context:
            parent_node = ParentNode("div", [])
            parent_node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have at least one child")

    def test_to_html_complex_nesting(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                        ParentNode(
                            "li",
                            [
                                LeafNode("span", "Nested item")
                            ]
                        )
                    ]
                )
            ]
        )
        expected = "<div><ul><li>Item 1</li><li>Item 2</li><li><span>Nested item</span></li></ul></div>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_mixed_content(self):
        node = ParentNode(
            "article",
            [
                LeafNode("h1", "Article Title"),
                LeafNode(None, "This is the introduction. "),
                LeafNode("strong", "Important point"),
                LeafNode(None, " Continue reading..."),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "Paragraph with "),
                        LeafNode("em", "emphasis"),
                        LeafNode(None, " and more text.")
                    ]
                )
            ]
        )
        expected = "<article><h1>Article Title</h1>This is the introduction. <strong>Important point</strong> Continue reading...<p>Paragraph with <em>emphasis</em> and more text.</p></article>"
        self.assertEqual(node.to_html(), expected)

    def test_parent_repr(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child], {"class": "container"})
        expected = "ParentNode(tag=div, children=[LeafNode(tag=span, value=child, props=None)], props={'class': 'container'})"
        self.assertEqual(repr(parent), expected)

    def test_parent_value_none(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertIsNone(parent.value)
if __name__ == "__main__":
    unittest.main()