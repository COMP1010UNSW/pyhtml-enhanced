"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""
from typing import Any


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
        # # Replace newlines with spaces, since they'll be rendered that way by
        # # browsers
        # '\n': ' ',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def escape_property(property_name: str) -> str:
    """
    Escape a tag property name.

    ## Replacements

    * Leading underscore `_` to '' (empty string), so Python keywords can be
      used for property names

    * `_` (underscore) to `-` (hyphen), so that kwargs can be used effectively
    """
    return property_name \
        .removeprefix('_') \
        .replace('_', '-')


def render_tag_properties(properties: dict[str, Any]) -> str:
    """
    Renders tag properties into a string that can be embedded within a tag.

    All properties with value `None` are ignored

    ## Example usage

    ```py
    >>> render_tag_properties_inline({
    ...     src="https://example.com/test.jpg",
    ...     alt="A test image",
    ... })
    'src="https://example.com/test.jpg" alt="A test image"'
    ```
    """
    return ' '.join([
        f'{escape_property(prop)}="{escape_string(val)}"'
        for prop, val in properties.items()
    ])


def filter_properties(properties: dict[str, Any]) -> dict[str, Any]:
    """
    Filter out properties where the value is `None`, so that they aren't
    rendered.
    """
    return {
        k: v
        for k, v in properties.items()
        if v is not None
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


def render_children(children: list[Any], sep: str = ' ') -> list[str]:
    """
    Render child elements of tags.

    Elements are placed in the same string, separated by the given separator
    """
    rendered = []
    for ele in children:
        rendered.extend(render_inline_element(ele))
    return increase_indent(rendered, 2)
