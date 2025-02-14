"""
# PyHTML / Render Options

Definition for the `Options` object, used to control rendering.
"""

from dataclasses import asdict, dataclass
from types import EllipsisType

# While it could be cleaner (and far less-repetitive) to use a TypedDict and
# declare the partial options class as per
# https://discuss.python.org/t/introduce-partial-for-typeddict/45176/4
# I elected not to do this, as by using a dataclass, the type is much more
# explicit, meaning that users won't encounter very confusing type-checker
# errors if they inadvertently pass a non-Options-shaped `dict` to a tag
# constructor.
# By using a `dataclass`, it is also much easier to perform `isinstance`
# checking on the object, which simplifies the implementation significantly.
# The only down-side is the duplicated definitions and copy-pasted
# documentation.


@dataclass(kw_only=True, frozen=True)
class FullRenderOptions:
    indent: str | None
    """String to add to indentation for non-inline child elements"""
    spacing: str
    """String to use for spacing between child elements"""

    def union(
        self, other: "RenderOptions | FullRenderOptions"
    ) -> "FullRenderOptions":
        """
        Union this set of options with the other options, returning a new
        `Options` object as the result.

        Any non-`None` options in `other` will overwrite the original values.
        """
        values = asdict(self)
        for field in values:
            if (other_value := getattr(other, field)) is not Ellipsis:
                values[field] = other_value

        return FullRenderOptions(**values)


@dataclass(kw_only=True, frozen=True)
class RenderOptions:
    """
    PyHTML rendering options.
    """

    indent: str | None | EllipsisType = ...
    """
    String to add to indentation for non-inline child elements. For example,
    to indent using a tab, you could use `'\\t'`. Setting the indent to `None`
    means that the output will not be indented at all, meaning that indentation
    from parent elements is discarded.

    Defaults to 2 spaces (`'  '`).
    """

    spacing: str | EllipsisType = ...
    """
    String to use for spacing between child elements. When this is set to
    `'\\n'`, each child element will be placed on its own line, and indentation
    will be applied. Otherwise, each child element will be separated using the
    given string.

    Defaults to a new-line (`'\\n'`).
    """

    def __repr__(self) -> str:
        """
        `__repr__` function excludes values that are `None`.
        """
        attrs = [
            f"{key}={repr(value)}"
            for key, value in asdict(self).items()
            if value is not Ellipsis
        ]
        return f"RenderOptions({', '.join(attrs)})"

    @staticmethod
    def default() -> FullRenderOptions:
        """
        Returns PyHTML's default rendering options.
        """
        return FullRenderOptions(
            indent="  ",
            spacing="\n",
        )

    def union(
        self, other: "RenderOptions | FullRenderOptions"
    ) -> "RenderOptions":
        """
        Union this set of options with the other options, returning a new
        `Options` object as the result.

        Any non-ellipsis options in `other` will overwrite the original values.
        """
        values = asdict(self)
        for field in values:
            if (other_value := getattr(other, field)) is not Ellipsis:
                values[field] = other_value

        return RenderOptions(**values)
