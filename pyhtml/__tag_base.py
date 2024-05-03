"""
# PyHTML Enhanced / Tag Base

Tag base class, including rendering logic
"""
from typing import Optional, TypeVar
from . import __util as util
from .__types import ChildrenType, AttributeType


SelfType = TypeVar('SelfType', bound='Tag')


class Tag:
    """
    Base tag class
    """
    def __init__(
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> None:
        """
        Create a new tag instance
        """
        self.children = util.flatten_list(list(children))
        """Children of this tag"""

        self.attributes = util.filter_attributes(attributes)
        """Attributes of this tag"""

    def __call__(
        self: SelfType,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> 'SelfType':
        """
        Create a new tag instance derived from this tag. Its children and
        attributes are based on this original tag, but with additional children
        appended and additional attributes unioned.
        """
        new_children = self.children + util.flatten_list(list(children))
        new_attributes = util.dict_union(self.attributes, attributes)

        return self.__class__(*new_children, **new_attributes)

    def __iter__(self) -> None:
        """
        Override the __iter__ method to give a slightly nicer error message
        when using PyHTML with flask
        """
        raise TypeError(
            f"'{self._get_tag_name()}' object is not iterable.\n"
            f"**HINT:** if you're using Flask, try converting your PyHTML "
            f"into a string using the `str` function before returning it.\n"
        )

    def _get_tag_name(self) -> str:
        """
        Returns the name of the tag
        """
        return type(self).__name__.removesuffix('_')

    def _get_default_attributes(
        self,
        given: dict[str, AttributeType],
    ) -> dict[str, AttributeType]:
        """
        Returns the default attributes for the tag given the specified
        attributes.

        This is overridden by child classes to return a dictionary of default
        attributes that are applied to the class.
        """
        return {}

    def _get_tag_pre_content(self) -> Optional[str]:
        """
        Return "pre-content" for the tag.

        This is used by the `<html>` tag to add a `<!DOCTYPE html>` before the
        tag.
        """
        return None

    def _escape_children(self) -> bool:
        """
        Returns whether the contents of the element should be escaped, or
        rendered plainly.

        By default, all string content should be escaped to prevent security
        vulnerabilities such as XSS, but this is disabled for certain tags such
        as <script>.
        """
        return True

    def _render(self, indent: int) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        attributes = util.filter_attributes(util.dict_union(
            self._get_default_attributes(self.attributes),
            self.attributes,
        ))

        # Tag and attributes
        opening = f"{' ' * indent}<{self._get_tag_name()}"

        # Add pre-content
        if (pre := self._get_tag_pre_content()) is not None:
            opening = f"{pre}\n{opening}"

        if len(attributes):
            opening += f" {util.render_tag_attributes(attributes)}>"
        else:
            opening += ">"

        if not len(self.children):
            opening += f"</{self._get_tag_name()}>"
            return [opening]
        else:
            out = [opening]
            # Children
            out.extend(
                util.render_children(
                    self.children,
                    self._escape_children(),
                    indent + 2,
                )
            )
            # Closing tag
            out.append(f"{' ' * indent}</{self._get_tag_name()}>")

            return out

    def render(self) -> str:
        """
        Render this tag and its contents to a string
        """
        return '\n'.join(self._render(0))

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()


class SelfClosingTag(Tag):
    """
    Self-closing tags don't contain child elements
    """
    def __init__(self, **attributes: AttributeType) -> None:
        # Self-closing tags don't allow children
        super().__init__(**attributes)

    def _render(self, indent: int) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        attributes = util.filter_attributes(util.dict_union(
            self._get_default_attributes(self.attributes),
            self.attributes,
        ))
        if len(attributes):
            return [
                f"{' ' * indent}<{self._get_tag_name()} "
                f"{util.render_tag_attributes(attributes)}/>"
            ]
        else:
            return [f"{' ' * indent}<{self._get_tag_name()}/>"]


class WhitespaceSensitiveTag(Tag):
    """
    Whitespace-sensitive tags are tags where whitespace needs to be respected.
    """
    def __init__(
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> None:
        attributes |= {}
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        **attributes: AttributeType,
    ):
        attributes |= {}
        return super().__call__(*children, **attributes)

    def _render(self, indent: int) -> list[str]:
        attributes = util.filter_attributes(util.dict_union(
            self._get_default_attributes(self.attributes),
            self.attributes,
        ))

        # Tag and attributes
        output = f"{' ' * indent}<{self._get_tag_name()}"

        if len(attributes):
            output += f" {util.render_tag_attributes(attributes)}>"
        else:
            output += ">"

        output += '\n'.join(util.render_children(
            self.children,
            self._escape_children(),
            0,
        ))

        output += f"</{self._get_tag_name()}>"
        return output.splitlines()
