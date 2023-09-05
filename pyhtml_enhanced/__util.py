"""
# PyHTML Enhanced / Util

Random helpful functions used elsewhere
"""
from typing import Any
from .__render_config import RenderConfig
from .__render_state import RenderState


def increase_indent(text: list[str], amount: int) -> list[str]:
    """
    Increase the indentation of all lines in a string list
    """
    prefix = amount * ' '

    return list(map(
        lambda line: prefix + line,
        text
    ))


def prettify_string(
    text: str,
    state: RenderState,
    cfg: RenderConfig,
) -> list[str]:
    """
    Format string so that it looks nice in the output HTML

    Prevents overly long lines, except when it is unavoidable (eg if there is
    an extremely long word)
    """
    line_length = max(
        cfg.max_line_length - state.indent,
        cfg.min_line_length,
    )
    lines: list[str] = []
    curr_line = ""
    for og_line in text.splitlines():
        for word in og_line.split(' '):
            if (
                len(curr_line) + 1 + len(word) > line_length
                and curr_line != ""
            ):
                curr_line += f" {word}"
            else:
                lines.append(curr_line)
                curr_line = word
        # End of the current line
        lines.append(curr_line)
        curr_line = ""

    # Remove the very last newline
    lines = lines[:-1]

    return increase_indent(lines, state.indent)


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


def render_tag_properties_inline(properties: dict[str, Any]) -> str:
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
    return ' '.join(render_tag_properties_multi_line(properties))


def render_tag_properties_multi_line(properties: dict[str, Any]) -> list[str]:
    """
    Renders tag properties into a string that can be embedded within a tag.

    Each property is placed on its own line for readability.

    ## Example usage

    ```py
    >>> render_tag_properties_inline({
    ...     src="https://example.com/test.jpg",
    ...     alt="A test image",
    ... })
    [
        'src="https://example.com/test.jpg"',
        'alt="A test image"',
    ]
    ```
    """
    return [
        f"{escape_property(prop)}={escape_string(val)}"
        for prop, val in properties.items()
    ]


def render_inline_element(
    ele: Any,
    state: RenderState,
    cfg: RenderConfig
) -> str:
    """
    Render an element inline
    """
    assert state.inline_rendering
    from .__tag import Tag
    if isinstance(ele, Tag):
        return ele._inline_render(state, cfg)
    else:
        # Remove newlines from strings when inline rendering
        return str(ele).replace('\n', ' ')


def render_element(
    ele: Any,
    state: RenderState,
    cfg: RenderConfig
) -> list[str]:
    """
    Render an element
    """
    assert not state.inline_rendering
    from .__tag import Tag
    if isinstance(ele, Tag):
        return ele._do_render(state, cfg)
    elif isinstance(ele, str):
        return prettify_string(ele, state, cfg)
    else:
        return increase_indent(str(ele).splitlines(), state.indent)


def render_child_elements_inline(
    children: list[Any],
    state: RenderState,
    cfg: RenderConfig,
    sep: str = ' '
) -> str:
    """
    Render child elements of tags.

    Elements are placed in the same string, separated by the given separator
    """
    rendered = []
    for ele in children:
        rendered.append(render_inline_element(ele, state, cfg))
    return sep.join(rendered)


def render_child_elements_multi_line(
    children: list[Any],
    state: RenderState,
    cfg: RenderConfig,
) -> list[str]:
    """
    Render child elements of tags.

    Each element is placed on its own line for readability
    """
    rendered = []
    for ele in children:
        rendered.extend(render_element(ele, state, cfg))
    return rendered
