"""
# PyHTML Enhanced / Tag

Tag base class, including rendering logic
"""
from typing import Any, Optional
from .__render_config import RenderConfig
from .__render_state import RenderState
from . import __util as util


class Tag:
    def __init__(self, *children: Any, **properties: Any) -> None:
        self.children = list(children)
        """Children of this tag"""

        self.properties = properties
        """Properties of this tag"""

    def __call__(self, *children: Any, **properties: Any) -> 'Tag':
        """
        Create a new tag instance derived from this tag. Its children and
        properties are based on this original tag, but with additional children
        appended and additional properties unioned.
        """
        new_children = self.children + list(children)
        new_properties = self.properties | properties

        return Tag(*new_children, **new_properties)

    def _get_tag_name(self) -> str:
        """
        Returns the name of the tag
        """
        return type(self).__name__

    def _should_render_multiline(self) -> bool:
        """
        Returns whether a tag should render across multiple lines
        """
        return True

    def _use_multiline_opening_tag(
        self,
        state: RenderState,
        cfg: RenderConfig,
    ) -> bool:
        """
        Returns whether the opening tag should be split over multiple lines
        """
        return False

    def _inline_render(
        self,
        state: RenderState,
        cfg: RenderConfig,
    ) -> str:
        """
        Render this tag in a manner so that it can be embedded inline with
        other tags
        """
        assert state.inline_rendering
        if len(self.properties):
            return (
                # Tag and properties
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties_inline(self.properties)}>"
                # Children
                f"{util.render_children_inline(self.children, state, cfg)}"
                # Closing tag
                f"</{self._get_tag_name()}>"
            )
        else:
            return f"<{self._get_tag_name()} />"

    def _do_render(
        self,
        state: RenderState,
        cfg: RenderConfig,
    ) -> list[str]:
        """
        Perform the rendering process for this tag.

        Returns the rendered HTML as a list[str] where each element is a single
        line.
        """
        assert not state.inline_rendering
        if self._should_render_multiline():
            return util.increase_indent(
                [
                    self._inline_render(
                        state.derive(inline_rendering=True),
                        cfg,
                    )
                ],
                state.indent,
            )

        output = []

        if self._use_multiline_opening_tag(state, cfg):
            # <tag_name
            #   property="value"
            #   another_prop="another val"
            # >
            output += util.increase_indent(
                [f"<{self._get_tag_name()}"]
                + util.increase_indent(
                    util.render_tag_properties_multi_line(self.properties),
                    cfg.indent_size,
                )
                + ['>'],
                state.indent,
            )
        else:
            # <tag_name property="value">
            output += [
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties_inline(self.properties)}>"
            ]

        # Child elements
        output += util.render_children_multiline(
            self.children,
            state,
            cfg,
        )

        # Closing tag
        output += util.increase_indent(
            [f"</{self._get_tag_name()}>"],
            state.indent,
        )

        return output

    def render(
        self,
        cfg: Optional[RenderConfig] = None,
    ) -> str:
        """
        Render this tag and its contents to a string
        """
        if cfg is None:
            cfg = RenderConfig()

        state = RenderState(inline_rendering=cfg.compressed)

        if state.inline_rendering:
            return self._inline_render(state, cfg)
        else:
            return '\n'.join(self._do_render(state, cfg))

    def __str__(self) -> str:
        return self.render()


class SelfClosingTag(Tag):
    def __init__(self, **properties: Any) -> None:
        # Self-closing tags don't allow children
        super().__init__(**properties)

    def __call__(self, **properties: Any) -> Tag:
        # Self-closing tags don't allow children
        return super().__call__(**properties)

    def _inline_render(
        self,
        state: RenderState,
        cfg: RenderConfig,
    ) -> str:
        assert state.inline_rendering
        # No need to care about children
        if len(self.properties):
            return (
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties_inline(self.properties)} "
                f"/>"
            )
        else:
            return f"<{self._get_tag_name()} />"
