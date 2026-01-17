"""
# PyHTML / Tags / Element Group

Defines an `ElementGroup` tag, which groups a collection of children, allowing
them to be rendered, without increasing indentation or adding an enclosing tag.
"""

from .. import __util as util
from ..__render_options import FullRenderOptions
from ..__tag_base import SelfType, Tag
from ..__types import AttributeType, ChildrenType


class ElementGroup(Tag):
    """
    A group of PyHTML elements. When rendered, they will be rendered one-by-one
    without increasing indentation or wrapping them in an enclosing tag.
    """

    def __init__(self, *children: ChildrenType) -> None:
        super().__init__(*children)

    def __call__(
        self: SelfType, *children: ChildrenType, **attributes: AttributeType
    ) -> "SelfType":
        if len(attributes):
            raise TypeError("Attributes are not supported on ElementGroup")
        return super().__call__(*children, **attributes)

    def _render(
        self,
        indent: str,
        options: FullRenderOptions,
        skip_indent: bool = False,
    ) -> list[str]:
        # Determine what the options for this element are
        options = options.union(self.options)

        indent_increase = options.indent if options.spacing == "\n" else ""
        return util.render_children(
            self.children,
            self._escape_children(),
            "" if indent_increase is None else indent,
            options,
        )
