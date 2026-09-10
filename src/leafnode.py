from typing import override

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None = None
        ) -> None:
            super().__init__()
            self.tag = tag
            self.value = value
            self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return f'{self.value}'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    @override
    def __repr__(self) -> str:
        return f'LeafNode({self.tag}, {self.value})'
