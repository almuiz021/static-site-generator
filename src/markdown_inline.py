import re
from textnode import TextNode, TextType
 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    for each_node in old_nodes:
        node_text = each_node.text
        node_type = each_node.text_type
        if node_type != TextType.TEXT:
            new_nodes.append(each_node)
        elif delimiter not in node_text:
            new_nodes.append(each_node)
        else:
            splitted = node_text.split(delimiter)
            if len(splitted) % 2 == 0:
                raise Exception("Invalid Syntax")
            for i in range(0, len(splitted)):
                if splitted[i]:
                    if i % 2 == 0:
                            text_node = TextNode(splitted[i], TextType.TEXT)
                            new_nodes.append(text_node)
                    else:
                        diff_node = TextNode(splitted[i], text_type)
                        new_nodes.append(diff_node)


    return new_nodes




[
    TextNode("This is text with an ", TextType.TEXT),
    TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
    TextNode(" and another ", TextType.TEXT),
    TextNode(
        "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
    ),
],

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

# def extract_markdown_images(text):
#     regex = r"\[(.*?)\]\((.*?)\)"
#     matches = re.findall(regex, text)
#     return matches

# def extract_markdown_links(text):
#     regex = r"\[(.*?)\]\((.*?)\)"
#     matches = re.findall(regex,text)
#     return matches




def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})",1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE, image[1]))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f'[{link[0]}]({link[1]})', 1)
            if len(sections) != 2:
                raise Exception("Invalid Markdown")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0],TextType.LINK, link[1]))

            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text,TextType.TEXT))
    return new_nodes
