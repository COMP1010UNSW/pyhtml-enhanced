"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""
from typing import Any


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


def escape_property(property_name: str) -> str:
    """
    Escape a tag property name.

    ## Replacements

    * `_` (underscore) to `-` (hyphen), so that kwargs can be used effectively
    """
    return property_name.replace('_', '-')


def render_tag_properties(properties: dict[str, Any]) -> str:
    """
    Renders tag properties into a string that can be embedded within a tag.

    All properties are included on the one line.

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
        f"{escape_property(prop)}={escape_string(val)}"
        for prop, val in properties.items()
    ])


def render_inline_element(ele: Any) -> str:
    """
    Render an element inline
    """
    from .__tag_base import Tag
    if isinstance(ele, Tag):
        return ele.render()
    else:
        # Remove newlines from strings when inline rendering
        return str(ele).replace('\n', ' ')


def render_children(children: list[Any], sep: str = ' ') -> str:
    """
    Render child elements of tags.

    Elements are placed in the same string, separated by the given separator
    """
    rendered = []
    for ele in children:
        rendered.append(render_inline_element(ele))
    return sep.join(rendered)
