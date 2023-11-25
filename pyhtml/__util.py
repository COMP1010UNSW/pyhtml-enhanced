"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""
from typing import Any, TypeVar, Union


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


def render_inline_element(ele: Any) -> list[str]:
    """
    Render an element inline
    """
    from .__tag_base import Tag
    if isinstance(ele, Tag):
        return ele._render()
    else:
        # Remove newlines from strings when inline rendering
        return [escape_string(str(ele))]


def render_children(children: list[Any]) -> list[str]:
    """
    Render child elements of tags.

    Elements are placed in the same string
    """
    rendered = []
    for ele in children:
        rendered.extend(render_inline_element(ele))
    return increase_indent(rendered, 2)


def flatten_list(the_list: list[Union[T, list[T]]]) -> list[T]:
    """
    Flatten a list by taking any list elements and inserting their items
    individually. Note that other iterables (such as str and tuple) are not
    flattened.
    """
    result: list[T] = []
    for item in the_list:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def instantiate_tag_types(elements: list[Any]) -> list[Any]:
    """
    Map a list so that any element e for which issubclass(e, Tag) returns True
    is instantiated
    """
    # Can't wait for lazy imports in Python 3.12
    from .__tag_base import Tag
    return list(map(
        lambda e: e() if isinstance(e, type) and issubclass(e, Tag) else e,
        elements,
    ))


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
