"""
# PyHTML Enhanced / Tag Base

Tag base class, including rendering logic
"""
from typing import Any
from . import __util as util


class Tag:
    """
    Base tag class
    """
    def __init__(self, *children: Any, **properties: Any) -> None:
        """
        Create a new tag instance
        """
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

    def _render(self) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        if len(self.children):
            # Tag and properties
            opening = f"<{self._get_tag_name()}"
            if len(self.properties):
                opening += f" {util.render_tag_properties(self.properties)}>"
            else:
                opening += ">"

            out = [opening]
            # Children
            out.extend(util.render_children(self.children))
            # Closing tag
            out.append(f"</{self._get_tag_name()}>")

            return out

        elif len(self.properties):
            return [
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties(self.properties)}/>"
            ]
        else:
            return [f"<{self._get_tag_name()}/>"]

    def render(self) -> str:
        """
        Render this tag and its contents to a string
        """
        return '\n'.join(self._render())

    def __str__(self) -> str:
        return self.render()


class SelfClosingTag(Tag):
    """
    Self-closing tags don't contain child elements
    """
    def __init__(self, **properties: Any) -> None:
        # Self-closing tags don't allow children
        super().__init__(**properties)

    def __call__(self, **properties: Any) -> Tag:
        # Self-closing tags don't allow children
        return super().__call__(**properties)
