from enum import Enum

from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]


def block_to_block_type(md_block):
    if md_block.startswith("#"):
        return BlockType.HEADING
    elif md_block.startswith("```\n") and md_block.endswith("```"):
        return BlockType.CODE
    elif md_block.startswith(("> ", ">")):
        return BlockType.QUOTE
    elif md_block.startswith("- "):
        return BlockType.UNORDERED_LIST
    elif md_block.startswith("1. "):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH


def text_to_children(text: str) -> list[HTMLNode]:
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]

def markdown_to_html_node(markdown) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            paragraph_text = block.replace("\n", " ")
            children = text_to_children(paragraph_text)
            node = ParentNode("p", children)
            node_list.append(node)
        elif block_type == BlockType.HEADING:
            heading_level = len(block) - len(block.lstrip("#"))
            heading_text = block[heading_level +1:]
            children = text_to_children(heading_text)
            node = ParentNode(f"h{heading_level}", children)
            node_list.append(node)
        elif block_type == BlockType.CODE:
            content = block.replace("```", "").lstrip("\n")
            text = TextNode(content, TextType.CODE)
            code_node = text_node_to_html_node(text)
            node = ParentNode("pre", [code_node])
            node_list.append(node)
        elif block_type == BlockType.QUOTE:
            lines = block.splitlines()
            stripped_lines = []
            for line in lines:
                stripped_lines.append(line.lstrip("> "))
            joined_quotes = " ".join(stripped_lines)
            children = text_to_children(joined_quotes)
            node = ParentNode("blockquote", children)
            node_list.append(node)
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                stripped_lines = line.lstrip("- ")
                children = text_to_children(stripped_lines)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            node = ParentNode("ul", li_nodes)
            node_list.append(node)
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                stripped_lines = line.split(". ", 1)[1]
                children = text_to_children(stripped_lines)
                li_node = ParentNode("li", children)
                li_nodes.append(li_node)
            node = ParentNode("ol", li_nodes)
            node_list.append(node)
    return ParentNode("div", node_list)
