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

    def _inline_render_children(
        self,
        state: RenderState,
        cfg: RenderConfig,
    ) -> str:
        """
        Render children of the tag in an inline style
        """
        assert state.inline_rendering
        # FIXME: This doesn't handle Tag elements
        return ' '.join(map(str, self.children))

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
                f"{self._inline_render_children(state, cfg)}"
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
            # TODO
            ...

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
