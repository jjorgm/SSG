from enum import Enum


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
