"""
# PyHTML Enhanced / Tag Base

Tag base class, including rendering logic
"""
from typing import Any, TypeVar
from . import __util as util


SelfType = TypeVar('SelfType', bound='Tag')


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

        self.properties = util.filter_properties(properties)
        """Properties of this tag"""

    def __call__(
        self: SelfType,
        *children: Any,
        **properties: Any,
    ) -> 'SelfType':
        """
        Create a new tag instance derived from this tag. Its children and
        properties are based on this original tag, but with additional children
        appended and additional properties unioned.
        """
        new_children = self.children + list(children)
        new_properties = self.properties | properties

        return self.__class__(*new_children, **new_properties)

    def _get_tag_name(self) -> str:
        """
        Returns the name of the tag
        """
        return type(self).__name__.removesuffix('_')

    def _render(self) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        # Tag and properties
        opening = f"<{self._get_tag_name()}"
        if len(self.properties):
            opening += f" {util.render_tag_properties(self.properties)}>"
        else:
            opening += ">"

        if not len(self.children):
            opening += f"</{self._get_tag_name()}>"
            return [opening]
        else:
            out = [opening]
            # Children
            out.extend(util.render_children(self.children))
            # Closing tag
            out.append(f"</{self._get_tag_name()}>")

            return out

    def render(self) -> str:
        """
        Render this tag and its contents to a string
        """
        return '\n'.join(self._render())

    def __str__(self) -> str:
        return self.render()


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
        self.comment_data = text
        super().__init__()

    def __call__(self):
        raise TypeError('Comment tags are not callable')

    def _get_tag_name(self) -> str:
        return '!--'

    def _render(self) -> list[str]:
        """
        Override of render, to render comments
        """

        return [
            '<!--',
            *util.escape_string(self.comment_data).splitlines(),
            '-->'
        ]


class SelfClosingTag(Tag):
    """
    Self-closing tags don't contain child elements
    """
    def __init__(self, **properties: Any) -> None:
        # Self-closing tags don't allow children
        super().__init__(**properties)

    def __call__(self, **properties: Any):
        # Self-closing tags don't allow children
        return super().__call__(**properties)

    def _render(self) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        if len(self.properties):
            return [
                f"<{self._get_tag_name()} "
                f"{util.render_tag_properties(self.properties)}/>"
            ]
        else:
            return [f"<{self._get_tag_name()}/>"]


class StylableTag(Tag):
    """
    Stylable tags suggest kwargs to do with element styling
    """
    def __init__(
        self,
        *children: Any,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ) -> None:
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
        }
        return super().__call__(*children, **properties)
