"""
# PyHTML Enhanced / Tags / Text

Tags for creating and formatting text
"""
from typing import Any, Literal
from ..__tag_base import SelfClosingTag, StylableTag


class p(StylableTag):
    """
    Paragraph
    """


class br(SelfClosingTag):
    """
    Line break
    """


class b(StylableTag):
    """
    Bold
    """


class strong(StylableTag):
    """
    Strong text

    Usually rendered as bold, but is semantic, meaning it could be interpreted
    in other ways (eg by screen readers)
    """


class i(StylableTag):
    """
    Italics
    """


class em(StylableTag):
    """
    Emphasis

    Usually rendered as italics, but is semantic, meaning it could be
    interpreted in other ways (eg by screen readers)
    """


class h1(StylableTag):
    """
    Header 1 (largest header)
    """


class h2(StylableTag):
    """
    Header 2
    """


class h3(StylableTag):
    """
    Header 3
    """


class h4(StylableTag):
    """
    Header 4
    """


class h5(StylableTag):
    """
    Header 5
    """


class h6(StylableTag):
    """
    Header 6 (smallest header)
    """


class a(StylableTag):
    """
    Hyperlink
    """
    def __init__(
        self,
        *children: Any,
        href: Any = None,
        target: Literal['_blank'] | Any = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ) -> None:
        super().__init__(
            *children,
            href=href,
            target=target,
            id=id,
            _class=_class,
            style=style,
            **properties,
        )

    def __call__(
        self,
        *children: Any,
        href: Any = None,
        target: Literal['_blank'] | Any = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        return super().__call__(
            *children,
            href=href,
            target=target,
            id=id,
            _class=_class,
            style=style,
            **properties,
        )
