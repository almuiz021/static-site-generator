import unittest

from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","Hello World",None,{"class":"font-semibold"})


        node2 = HTMLNode("p","Hello World",None,{"class":"font-semibold"})
        
        print(node,type(node))
        print(node2,type(node2))
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()