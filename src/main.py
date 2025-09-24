from textnode import TextType, TextNode 
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_inline import split_nodes_delimiter, extract_markdown_images,extract_markdown_links
from markdown_blocks import block_to_block_type
def main():
    
    dummy = TextNode("Some Text",TextType.LINK,"https://www.muiz.com")
    # print(dummy)


if __name__ == "__main__":
    main()
