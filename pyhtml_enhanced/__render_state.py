"""
# PyHTML Enhanced / Render State

Manage the state of the rendering process
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class RenderState:
    """
    Current state of the render
    """

    indent: int = 0
    """
    Current indentation level
    """

    inline_rendering: bool = False
    """
    Whether to use inline rendering of tags.

    ## With inline rendering

    ```html
    This text <i>does</i> have inline rendering
    ```

    ## Without inline rendering

    ```html
    This text
    <i>does not</i>
    have inline rendering
    ```
    """

    def derive(
        self,
        indent: Optional[int] = None,
        inline_rendering: Optional[bool] = None,
    ) -> 'RenderState':
        """
        Return a new RenderState with the given properties modified
        """
        if indent is None:
            indent = self.indent
        if inline_rendering is None:
            inline_rendering = self.inline_rendering

        return RenderState(
            indent=indent,
            inline_rendering=inline_rendering,
        )
