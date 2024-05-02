"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""
from typing import Any, TypeVar
from collections.abc import Generator, Sequence
from .__types import ChildrenType, ChildElementType


T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


def increase_indent(text: list[str], amount: int) -> list[str]:
    """
    Increase the indentation of all lines in a string list
    """
    prefix = amount * ' '

    return list(map(
        lambda line: prefix + line,
        text
    ))


def escape_string(text: str) -> str:
    """
    Escape a string by replacing unsafe characters with their HTML escape
    sequences
    """
    replacements = {
        # & needs to be replaced first or we break all other options
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#x27;',
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
    return attr_name \
        .removeprefix('_') \
        .removesuffix('_') \
        .replace('_', '-')


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
    return ' '.join([
        f'{escape_attribute(attr)}="{escape_string(str(val))}"'
        if val is not True
        else escape_attribute(attr)
        for attr, val in attributes.items()
    ])


def filter_attributes(attributes: dict[str, Any]) -> dict[str, Any]:
    """
    Filter out attributes where the value is `None`, so that they aren't
    rendered.
    """
    return {
        k: v
        for k, v in attributes.items()
        if v is not None and v is not False
    }


def render_inline_element(
    ele: ChildElementType,
    escape_strings: bool,
    indent: int,
) -> list[str]:
    """
    Render an element inline
    """
    from .__tag_base import Tag
    if isinstance(ele, Tag):
        return ele._render(indent)
    elif isinstance(ele, type) and issubclass(ele, Tag):
        e = ele()
        return e._render(indent)
    else:
        # Remove newlines from strings when inline rendering
        if escape_strings:
            return increase_indent([escape_string(str(ele))], indent)
        else:
            return increase_indent([str(ele)], indent)


def render_children(
    children: list[ChildElementType],
    escape_strings: bool,
    indent: int,
) -> list[str]:
    """
    Render child elements of tags.

    Elements are placed in the same string
    """
    rendered = []
    for ele in children:
        rendered.extend(render_inline_element(ele, escape_strings, indent))
    return rendered


def flatten_list(the_list: list[ChildrenType]) -> list[ChildElementType]:
    """
    Flatten a list by taking any list elements and inserting their items
    individually. Note that other iterables (such as str and tuple) are not
    flattened.

    FIXME: Currently doesn't support lists of lists
    """
    result: list[ChildElementType] = []
    for item in the_list:
        if isinstance(item, list):
            result.extend(item)
        elif isinstance(item, Generator):
            result.extend(item)
        elif isinstance(item, str):
            result.append(item)
        elif isinstance(item, Sequence):
            result.extend(item)
        else:
            result.append(item)
    return result


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
