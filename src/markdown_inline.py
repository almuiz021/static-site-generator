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
