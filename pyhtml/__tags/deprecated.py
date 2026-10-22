"""
# PyHTML Enhanced / Tags / Deprecated

Tags that are now deprecated, and should not be used.

Note that all documentation is licensed as CC-BY-SA-2.5

https://creativecommons.org/licenses/by-sa/2.5/
"""

from warnings import deprecated

from ..__tag_base import Tag
from ..__types import AttributeType, ChildrenType


@deprecated("deprecated tag: to be removed from browsers")
class fencedframe(Tag):
    """
    Represents a nested browsing context, like `<iframe>` but with more native
    privacy features built in.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fencedframe)
    """

    def __init__(
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a nested browsing context, like `<iframe>` but with more
        native privacy features built in.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fencedframe)
        """
        attributes |= {}
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ):
        """
        Represents a nested browsing context, like `<iframe>` but with more
        native privacy features built in.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fencedframe)
        """
        attributes |= {}
        return super().__call__(*children, **attributes)

    def _get_default_attributes(
        self, given: dict[str, AttributeType]
    ) -> dict[str, AttributeType]:
        return {}
