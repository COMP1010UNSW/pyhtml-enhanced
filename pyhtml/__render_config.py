"""
# PyHTML Enhanced / Config

Options used to control the library's behaviour

## NOTE: Currently unused, as it just produces inline HTML
"""
from dataclasses import dataclass


@dataclass(kw_only=True)
class RenderConfig:
    """
    Configuration class, used to control the
    """

    compressed: bool = False
    """
    Whether to compress the generated HTML by always using inline rendering.

    Excluding tags that always output multiple lines, this results in all HTML
    being rendered to a single line
    """

    max_line_length: int = 100
    """
    Maximum line length for the rendered HTML

    Note that some items will be rendered as longer than this, such as in <pre>
    blocks, where the users line length is respected. Additionally, to avoid
    splitting up long words, this will be ignored sometimes.
    """

    min_line_length: int = 40
    """
    Minimum line length for the rendered HTML

    To avoid getting extremely cramped lines in deeply indented blocks of HTML,
    this minimum line length ensures that all lines will be of a reasonable
    length.

    For example, if the max line length is 80, the minimum is 20, and the
    current indentation is 70, contents would be allowed to render between 70
    and 90 characters to ensure that the minimum is respected.
    """

    indent_size: int = 2
    """
    The number of spaces to use for indentation
    """
