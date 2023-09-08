"""
# PyHTML Enhanced / Tags / Head

Tags used in the header of an HTML document
"""
from typing import Any
from ..__tag_base import SelfClosingTag


class base(SelfClosingTag):
    """
    Specifies the base URL to use for all relative URLs in a document. There
    can be only one such element in a document.
    """
    def __init__(
        self,
        /,
        href: Any = None,
        target: Any = None,
        **properties: Any,
    ) -> None:
        properties |= {
            'href': href,
            'target': target,
        }
        super().__init__(**properties)

    def __call__(
        self,
        /,
        href: Any = None,
        target: Any = None,
        **properties: Any,
    ):
        properties |= {
            'href': href,
            'target': target,
        }
        return super().__call__(**properties)


class Link(SelfClosingTag):
    """
    Specifies relationships between the current document and an external
    resource. This element is most commonly used to link to CSS but is also
    used to establish site icons (both "favicon" style icons and icons for the
    home screen and apps on mobile devices) among other things.
    """
