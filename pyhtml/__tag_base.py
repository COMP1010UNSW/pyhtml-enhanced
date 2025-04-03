"""
# PyHTML Enhanced / Tag Base

Tag base class, including rendering logic
"""

from typing import TypeVar

# from warnings import deprecated
from typing_extensions import deprecated

from . import __util as util
from .__render_options import FullRenderOptions, RenderOptions
from .__types import AttributeType, ChildrenType

SelfType = TypeVar("SelfType", bound="Tag")


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
        flattened, options = util.flatten_children(list(children))
        self.children = flattened
        """Children of this tag"""

        self.attributes = util.filter_attributes(attributes)
        """Attributes of this tag"""

        self.options = self._get_default_render_options().union(options)
        """Render options specified for this element"""

    def __call__(
        self: SelfType,
        *children: ChildrenType,
        **attributes: AttributeType,
    ) -> "SelfType":
        """
        Create a new tag instance derived from this tag. Its children and
        attributes are based on this original tag, but with additional children
        appended and additional attributes unioned.
        """
        flattened, options = util.flatten_children(list(children))
        new_children = self.children + flattened
        new_attributes = util.dict_union(self.attributes, attributes)
        new_options = self.options.union(options)

        return self.__class__(*new_children, new_options, **new_attributes)

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
        return type(self).__name__.removesuffix("_")

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

    def _get_default_render_options(self) -> RenderOptions:
        """
        Returns the default rendering options for this tag.

        This can be used to control how the element is rendered by default.
        For example a `<p>` element can specify `spacing=""` so that its child
        elements are not spaced out (thereby
        [reducing anger from Tom7](https://youtu.be/Y65FRxE7uMc?t=0)).

        When the user provides their own options, they will be merged with the
        element's default options using the `Options.union` method.
        """
        # By default, don't override any options
        return RenderOptions()

    def _get_tag_pre_content(self) -> str | None:
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
        as `<script>`.
        """
        return True

    def _render(
        self,
        indent: str,
        options: FullRenderOptions,
        skip_indent: bool = False,
    ) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output.

        Parameters
        ----------
        indent : str
            string to use for indentation
        options : FullOptions
            rendering options
        skip_indent : bool
            whether to skip indentation for this element

        Returns
        -------
        list[str]
            list of lines of output
        """
        # Determine what the options for this element are
        options = options.union(self.options)

        attributes = util.filter_attributes(
            util.dict_union(
                self._get_default_attributes(self.attributes),
                self.attributes,
            )
        )

        # Indentation to use before opening tag
        indent_pre = "" if skip_indent else indent
        # Indentation to use before closing tag
        indent_post = "" if skip_indent or options.indent is None else indent

        # Tag and attributes
        opening = f"{indent_pre}<{self._get_tag_name()}"

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
            indent_increase = options.indent if options.spacing == "\n" else ""
            # Children
            children = util.render_children(
                self.children,
                self._escape_children(),
                "" if indent_increase is None else indent + indent_increase,
                options,
            )
            closing = f"</{self._get_tag_name()}>"
            if options.spacing == "\n":
                return [
                    opening,
                    *children,
                    f"{indent_post}{closing}",
                ]
            else:
                # Children must have at least one line, since we would have
                # taken the `if not len(self.children)` branch if there were
                # no children to render
                out: list[str] = [
                    opening + options.spacing + children[0],
                    *children[1:],
                ]
                # Add the closing tag onto the end
                return [
                    *out[:-1],
                    # Only include post indentation if it's on a different line
                    # to the pre indentation
                    (indent_post if len(out) > 1 else "")
                    + out[-1]
                    + options.spacing
                    + closing,
                ]

    def render(self) -> str:
        """
        Render this tag and its contents to a string
        """
        return "\n".join(self._render("", RenderOptions.default()))

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return self.render()


class SelfClosingTag(Tag):
    """
    Self-closing tags don't contain child elements
    """

    def __init__(
        self, *options: RenderOptions, **attributes: AttributeType
    ) -> None:
        # Self-closing tags don't allow children
        super().__init__(*options, **attributes)

    def _render(
        self,
        indent: str,
        options: FullRenderOptions,
        skip_indent: bool = False,
    ) -> list[str]:
        """
        Renders tag and its children to a list of strings where each string is
        a single line of output
        """
        indent_str = "" if skip_indent else indent
        attributes = util.filter_attributes(
            util.dict_union(
                self._get_default_attributes(self.attributes),
                self.attributes,
            )
        )
        if len(attributes):
            return [
                f"{indent_str}<{self._get_tag_name()} "
                f"{util.render_tag_attributes(attributes)}/>"
            ]
        else:
            return [f"{indent_str}<{self._get_tag_name()}/>"]


@deprecated(
    "Overload `_get_default_render_options` to return "
    "`RenderOptions(indent=None, spacing='')` instead"
)
class WhitespaceSensitiveTag(Tag):  # pragma: no cover
    """
    Whitespace-sensitive tags are tags where whitespace needs to be respected.
    """

    def _get_default_render_options(self) -> RenderOptions:
        return RenderOptions(indent=None, spacing="")


def create_tag(name: str, base: type[Tag] = Tag) -> type[Tag]:
    """
    Create a new PyHTML tag definition.

    PyHTML already provides definitions for all standard HTML tags, so you
    don't need to use this unless you are using a JavaScript library that
    defines custom HTML elements.

    Args:
        name (str): the name of the tag. This is used during rendering, as
                    `<{name}> ... </{name}>`.

        base (type[Tag]): the base class to use for the custom tag. The new tag
                          will inherit from this base class.

    Returns:
        type[Tag]: a new tag definition.
    """

    def _get_tag_name(self) -> str:
        return name

    # Generate custom type inheriting from given base class
    CustomTag = type(
        name,
        (base,),
        {
            "_get_tag_name": _get_tag_name,
        },
    )

    return CustomTag
