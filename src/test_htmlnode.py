import unittest

from htmlnode import HTMLNode, LeafNode

class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","Hello World",None,{"class":"font-semibold"})


        node2 = HTMLNode("p","Hello World",None,{"class":"font-semibold"})
        
        self.assertNotEqual(node,node2)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("a","Click Me",{"href":"www.github.com/almuiz021","target":"_blank"})
        self.assertEqual(node2.to_html(),'<a href = "www.github.com/almuiz021" target = "_blank">Click Me</a>')

if __name__ == "__main__":
    unittest.main()