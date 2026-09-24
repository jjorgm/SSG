from shlex import split

from extractmarkdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("invalid markdown syntax")
            for i, text in enumerate(split_text):
                if text == "":
                    continue
                elif i % 2 == 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text, text_type))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)

            if len(images) == 0:
                new_nodes.append(node)
                continue

            remaining_text = node.text

            for image_alt, image_link in images:
                sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)

                if len(sections) != 2:
                    raise ValueError("incorrect image syntax")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))

                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                remaining_text = sections[1]

            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)

            if len(links) == 0:
                new_nodes.append(node)
                continue

            remaining_text = node.text

            for link_alt, url in links:
                sections = remaining_text.split(f"[{link_alt}]({url})", 1)

                if len(sections) != 2:
                    raise ValueError("incorrect link syntax")

                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))

                new_nodes.append(TextNode(link_alt, TextType.LINK, url))
                remaining_text = sections[1]

            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    new_nodes = []
    nodes = [TextNode(text, TextType.TEXT)]

    bold_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    link_nodes = split_nodes_link(image_nodes)
    new_nodes.extend(link_nodes)

    return new_nodes
