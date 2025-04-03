"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""

from collections.abc import Generator, Sequence
from typing import Any, TypeVar

from .__render_options import FullRenderOptions, RenderOptions
from .__types import ChildElementType, ChildrenType

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def increase_indent(text: list[str], indent: str) -> list[str]:
    """
    Increase the indentation of all lines in a string list
    """
    return list(map(lambda line: indent + line, text))


def escape_string(text: str) -> str:
    """
    Escape a string by replacing unsafe characters with their HTML escape
    sequences
    """
    replacements = {
        # & needs to be replaced first or we break all other options
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#x27;",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def escape_attribute(attr_name: str) -> str:
    """
    Escape a tag attribute name.

    ## Replacements

    * Prefix and suffix underscores `_` to '' (empty string), so Python
      keywords can be used for attribute names

    * `_` (underscore) to `-` (hyphen), so that kwargs can be used effectively
    """
    return attr_name.removeprefix("_").removesuffix("_").replace("_", "-")


def render_tag_attributes(attributes: dict[str, Any]) -> str:
    """
    Renders tag attributes into a string that can be embedded within a tag.

    All attributes with value `None` are ignored

    ## Example usage

    ```py
    >>> render_tag_attributes_inline({
    ...     src="https://example.com/test.jpg",
    ...     alt="A test image",
    ... })
    'src="https://example.com/test.jpg" alt="A test image"'
    ```
    """
    return " ".join(
        [
            f'{escape_attribute(attr)}="{escape_string(str(val))}"'
            if val is not True
            else escape_attribute(attr)
            for attr, val in attributes.items()
        ]
    )


def filter_attributes(attributes: dict[str, Any]) -> dict[str, Any]:
    """
    Filter out attributes where the value is `None`, so that they aren't
    rendered.
    """
    return {
        k: v for k, v in attributes.items() if v is not None and v is not False
    }


def render_inline_element(
    ele: ChildElementType,
    escape_strings: bool,
    indent: str,
    options: FullRenderOptions,
) -> list[str]:
    """
    Render an element inline
    """
    from .__tag_base import Tag

    skip_indent = options.spacing is not None and "\n" not in options.spacing

    if isinstance(ele, Tag):
        return ele._render(indent, options, skip_indent)
    elif isinstance(ele, type) and issubclass(ele, Tag):
        e = ele()
        return e._render(indent, options, skip_indent)
    else:
        # Remove newlines from strings when inline rendering
        if escape_strings:
            return increase_indent(
                [escape_string(line) for line in str(ele).splitlines()],
                "" if skip_indent else indent,
            )
        else:
            return increase_indent(
                str(ele).splitlines(), "" if skip_indent else indent
            )


def render_children(
    children: list[ChildElementType],
    escape_strings: bool,
    indent: str,
    options: FullRenderOptions,
) -> list[str]:
    """
    Render child elements of tags.

    Elements are placed in the same string
    """
    rendered: list[str] = []
    for ele in children:
        rendered_child = render_inline_element(
            ele, escape_strings, indent, options
        )
        if options.spacing == "\n":
            rendered.extend(rendered_child)
        else:
            # Custom spacing
            if len(rendered) == 0:
                rendered = rendered_child
            else:
                *r_head, r_tail = rendered
                # rendered_child should not have length zero, otherwise
                # something has gone horribly wrong, and it's ok to crash
                c_head, *c_tail = rendered_child
                # Join it all nicely
                rendered = [
                    *r_head,
                    # Join using spacing as separator
                    r_tail + options.spacing + c_head,
                    *c_tail,
                ]
    return rendered


def flatten_children(
    the_list: list[ChildrenType],
) -> tuple[list[ChildElementType], RenderOptions]:
    """
    Flatten the given list of child elements, and extract the given render
    options.

    Note that other iterables (such as str and tuple) are not flattened. Lists
    of lists are not supported.

    Parameters
    ----------
    the_list : list[ChildrenType]
        list of children elements

    Returns
    -------
    (result, options) - tuple[list[ChildElementType], Options]
        * `result` is the flattened list
        * `options` is the `Options` object containing the render options
    """
    result: list[ChildElementType] = []
    options = RenderOptions()
    for item in the_list:
        if isinstance(item, list | Generator):
            result.extend(item)
        elif isinstance(item, str):
            result.append(item)
        elif isinstance(item, Sequence):
            result.extend(item)
        elif isinstance(item, RenderOptions):
            options = options.union(item)
        else:
            result.append(item)
    return result, options


def dict_union(base: dict[K, V], additions: dict[K, V]) -> dict[K, V]:
    """
    Smart union of a dictionary - if a value in `base` is `None` and the
    value in `additions` exists, the value is replaced
    """
    result = base.copy()
    for k, v in additions.items():
        if k in base and v is None:
            pass
        else:
            result[k] = v

    return result
