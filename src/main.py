from textnode import TextType, TextNode 
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    
    dummy = TextNode("Some Text",TextType.LINK,"https://www.muiz.com")
    # print(dummy)


if __name__ == "__main__":
    main()
