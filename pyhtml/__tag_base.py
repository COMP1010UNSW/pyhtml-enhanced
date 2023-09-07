"""
# PyHTML Enhanced / Tag Base

Tag base class, including rendering logic
"""
from typing import Any
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

    def render(self) -> str:
        """
        Render this tag and its contents to a string
        """
        if len(self.children):
            out = []
            # Tag and properties
            out.append(f"<{self._get_tag_name()}")
            if len(self.properties):
                out.append(
                    f" {util.render_tag_properties(self.properties)}>"
                )
            else:
                out.append(">")
            # Children
            out.append(util.render_children(self.children))
            # Closing tag
            out.append(f"</{self._get_tag_name()}>")

            return ''.join(out)

        elif len(self.properties):
            return (
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties(self.properties)}/>"
            )
        else:
            return f"<{self._get_tag_name()}/>"

    def __str__(self) -> str:
        return self.render()


class SelfClosingTag(Tag):
    def __init__(self, **properties: Any) -> None:
        # Self-closing tags don't allow children
        super().__init__(**properties)

    def __call__(self, **properties: Any) -> Tag:
        # Self-closing tags don't allow children
        return super().__call__(**properties)
