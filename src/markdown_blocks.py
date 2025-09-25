from enum import Enum
from textnode import text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from markdown_inline import text_to_textnodes
import re
from textnode import TextNode


def markdown_to_blocks(markdown):
    splitted_lines = markdown.split("\n\n")
    new_lines = []
    for line in splitted_lines:
        stripped = line.strip()
        if stripped:
            new_lines.append(stripped)
    return new_lines


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_html = ParentNode("div",[])
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            p_html = markdown_to_paragraph(block)
            parent_html.children.append(p_html)
    
        if block_to_block_type(block) == BlockType.HEADING:
            h_node = markdown_to_heading(block)
            parent_html.children.append(h_node)
    
        if block_to_block_type(block) == BlockType.CODE:
            code_block = markdown_to_code(block)
            parent_html.children.append(code_block)

        if block_to_block_type(block) == BlockType.QUOTE:
            quote_node = markdown_to_quote(block)
            parent_html.children.append(quote_node)
    
        if block_to_block_type(block) == BlockType.ULIST:
            ulist_node = markdown_to_ulist(block)
            parent_html.children.append(ulist_node)
    
        if block_to_block_type(block) == BlockType.OLIST:
            olist = markdown_to_olist(block)
            parent_html.children.append(olist)
    
    return parent_html


def markdown_to_paragraph(text):
    children = text_to_children(text)
    p_node = LeafNode("p", children)
    return p_node

    
def markdown_to_heading(text):
    children = text_to_children(text)
    heading_no = children.count("#", 0)
    heading_text = children.lstrip("# ")
    h_node = LeafNode(f"h{heading_no}", heading_text)
    return h_node


def markdown_to_quote(text):
    children = text_to_children(text)
    quote_node = LeafNode("blockquote", children)
    return quote_node


def markdown_to_ulist(text):
    children = text_to_children(text)
    remove_dash = children.split("- ")
    ul_parent = ParentNode("ul",[])
    for each in remove_dash:
        if each:
            li_node = LeafNode("li",each.strip())
            ul_parent.children.append(li_node)
    return ul_parent


def markdown_to_olist(text):
    children = text_to_children(text)
    pattern = f"\d+\.\s"
    remove_nos = re.split(pattern, children)
    ol_parent = ParentNode("ol",[])
    for each in remove_nos:
        if each:
            li_node = LeafNode("li",each.strip())
            ol_parent.children.append(li_node)
    return ol_parent


def markdown_to_code(text):
    splitted = text.splitlines()
    if splitted and splitted[0].startswith("```"):
        splitted = splitted[1:]
    if splitted and splitted[-1].startswith("```"):
        splitted = splitted[:-1]
    inner = "\n".join(splitted) + "\n"  

    code_node = LeafNode("code",inner)
    parent_node = ParentNode("pre",[code_node])
    return parent_node


def text_to_children(text):
    normal_text = text_normalizer(text)
    textnodes = text_to_textnodes(normal_text)
    html_node = []
    for textnode in textnodes:
        html_node.append(text_node_to_html_node(textnode).to_html())
    return "".join(html_node)

def text_normalizer(text):
    splitted = text.split()
    normalized_text = []
    for each in splitted:
        stripped = each.strip()
        normalized_text.append(stripped)
    return " ".join(normalized_text)
