"""
# PyHTML / Render Options

Definition for the `Options` object, used to control rendering.
"""

from dataclasses import asdict, dataclass
from typing import Optional

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
class FullOptions:
    indent: str
    """String to add to indentation for non-inline child elements"""
    spacing: str
    """String to use for spacing between child elements"""

    def union(self, other: "Options | FullOptions") -> "FullOptions":
        """
        Union this set of options with the other options, returning a new
        `Options` object as the result.

        Any non-`None` options in `other` will overwrite the original values.
        """
        values = asdict(self)
        for field in values:
            if (other_value := getattr(other, field)) is not None:
                values[field] = other_value

        return FullOptions(**values)


@dataclass(kw_only=True, frozen=True)
class Options:
    """
    PyHTML rendering options.

    * `indent` (`str`): string to add to indentation for non-inline child
      elements. For example, to indent using a tab, you could use `'\\t'`.
      Defaults to 2 spaces `'  '`.
    * `spacing` (`str`): string to use for spacing between child elements. When
      this is set to `'\\n'`, each child element will be placed on its own
      line, and indentation will be applied. Otherwise, each child element will
      be separated using the given value.
    """

    indent: Optional[str] = None
    """String to add to indentation for non-inline child elements"""
    spacing: Optional[str] = None
    """String to use for spacing between child elements"""

    @staticmethod
    def default() -> FullOptions:
        """
        Returns PyHTML's default rendering options.
        """
        return FullOptions(
            indent="  ",
            spacing="\n",
        )
