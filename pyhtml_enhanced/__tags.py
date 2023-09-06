"""
# PyHTML Enhanced / Tags

Tag definitions
"""
from .__tag_base import Tag, SelfClosingTag


class html(Tag):
    """
    HTML document
    """


class head(Tag):
    """
    HTML header, containing metadata about the document
    """


class body(Tag):
    """
    HTML body, containing the visible contents of the document
    """


class p(Tag):
    """
    Paragraph
    """
