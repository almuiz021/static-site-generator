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
    p_node = ParentNode("p", children=children)
    return p_node


def markdown_to_heading(text):
    line = text.strip()
    i = 0
    while i < len(line) and i < 6 and line[i] == "#":
        i += 1
    if i == 0 or (i < len(line) and line[i] != " "):
        return markdown_to_paragraph(text)
    content = line[i+1:].strip()
    children = text_to_children(content)
    return ParentNode(f"h{i}", children)


def markdown_to_quote(text):
    lines = []
    for ln in text.splitlines():
        if not ln.strip():
            continue
        if ln.lstrip().startswith(">"):
            ln = ln.lstrip()[1:]
            if ln.startswith(" "):
                ln = ln[1:]
        lines.append(ln.rstrip())
    content = " ".join(lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def markdown_to_ulist(text):
    ul_children = []
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("- ") or ln.startswith("* "):
            item = ln[2:].strip()
            li_children = text_to_children(item)
            ul_children.append(ParentNode("li", li_children))
    return ParentNode("ul", ul_children)


def markdown_to_olist(text):
    ol_children = []
    for ln in text.splitlines():
        ln = ln.strip()
        if not ln:
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", ln)
        if m:
            item = m.group(2).strip()
            li_children = text_to_children(item)
            ol_children.append(ParentNode("li", li_children))
    return ParentNode("ol", ol_children)


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
        html_node.append(text_node_to_html_node(textnode))
    return html_node


def text_normalizer(text):
    splitted = text.split()
    normalized_text = []
    for each in splitted:
        stripped = each.strip()
        normalized_text.append(stripped)
    return " ".join(normalized_text)    

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title_md = list(filter(lambda item:item.startswith("# "),blocks))
    if not title_md or len(title_md) > 1:
        raise Exception("No elements or more elements")
    title = title_md[0].strip("# ")
    return title


md = """
# Heading 1

## Heading 2

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

>QUOTE BLOCK MATE

"""

node = markdown_to_html_node(md)
# print("================================")
# print(node.to_html())

extract_title(md)