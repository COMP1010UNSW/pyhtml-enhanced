"""
# PyHTML Enhanced

A drop-in replacement for PyHTML with improved editor support and
documentation.
"""
__all__ = [
    'Tag',
    'SelfClosingTag',
    'html',
    'head',
    'body',
    'p',
]

from .__tag_base import Tag, SelfClosingTag
from .__tags import html, head, body, p
