"""
# PyHTML Enhanced / Tags / Comment

Definition for the comment tag.
"""

from .. import __util as util
from ..__render_options import FullRenderOptions
from ..__tag_base import Tag


class Comment(Tag):
    """
    An HTML comment.

    Renders as:

    ```html
    <!-- [comment text] -->
    ```

    Note that this does not render as a `<comment>` tag
    """

    def __init__(self, text: str) -> None:
        """
        An HTML comment.

        Renders as:

        ```html
        <!-- [comment text] -->
        ```

        Note that this does not render as a `<comment>` tag
        """
        self.comment_data = text
        super().__init__()

    def __call__(self, *args, **kwargs):
        raise TypeError("Comment tags are not callable")

    def _get_tag_name(self) -> str:
        # Ignore coverage since this is only implemented to satisfy inheritance
        # and is never used since we override _render
        return "!--"  # pragma: no cover

    def _render(
        self,
        indent: str,
        options: FullRenderOptions,
        skip_indent: bool = False,
    ) -> list[str]:
        """
        Override of render, to render comments
        """

        return util.increase_indent(
            ["<!--"]
            + util.increase_indent(
                util.escape_string(self.comment_data).splitlines(),
                "" if options.indent is None else indent + options.indent,
            )
            + ["-->"],
            indent,
        )
