from typing import override

from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        children: list[HTMLNode] | None,
        props: dict[str, str] | None = None
    ) -> None:
        super().__init__()
        self.tag = tag
        self.children = children
        self.props = props

    @override
    def to_html(self):
        if not self.tag:
            raise ValueError
        elif not self.children:
            raise ValueError("no children")
        else:
            children_nodes = ''
            for child in self.children:
                children_nodes += child.to_html()
            return f'<{self.tag}>{children_nodes}</{self.tag}>'
