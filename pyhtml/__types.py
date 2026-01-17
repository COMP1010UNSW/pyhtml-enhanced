"""
# Pyhtml / Types

Type definitions
"""

import sys
from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING, Union

if sys.version_info >= (3, 14):
    from string.templatelib import Template
else:  # pragma: no cover
    from typing_extensions import Never
    
    Template = Never

if TYPE_CHECKING:
    from .__render_options import RenderOptions
    from .__tag_base import Tag


AttributeType = str | bool | None
"""
Objects that are valid values for tag attributes

* `str`: attribute is included with the given string value
* `True`: attribute is included with no associated string value
* `False` | `None`: attribute is explicitly excluded (ie the default value is
  overridden).
"""


ChildElementType = Union["Tag", type["Tag"], str, Template]
"""
Objects that are valid as a child element of an HTML element.

While more types can technically work (such as `int`, `bool` and `float`),
these aren't allowed in order to encourage proper use of string formatting.

When a Template (t-string) is given, PyHTML elements used as interpolations
will be rendered with no new-line spacing or indentation.
"""


ChildrenType = Union[
    ChildElementType,
    Sequence[ChildElementType],
    # TODO: Would an `Any` type for the generator return be better, even though
    # it would be discarded?
    "Generator[ChildElementType, None, None]",
    "RenderOptions",
]
"""
Objects that are valid when passed to a `Tag` for use as children.

* `ChildElementType`: a singular element
* `list[ChildElementType]`: a list of elements
* `GeneratorType[ChildElementType, None, None]`: a generator of elements
* `Options`: PyHTML render options.
"""
