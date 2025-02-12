"""
# Meta / Scrape Tags

Using the MDN documentation on HTML elements, generate all HTML element classes
including their documentation.

It also embeds suggested kwargs for some elements, using info from tags.yml.
"""

import sys
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, TypedDict

import requests
import yaml
from typing_extensions import NotRequired

from pyhtml.__render_options import RenderOptions

TAGS_YAML = "meta/tags.yml"
"""File location to load custom tag data from"""


MDN_WEB_DOCS = (
    "https://raw.githubusercontent.com"
    "/mdn/content/main/files/en-us/web/html/element/index.md"
)
"""Location to grab web docs from"""

MDN_ELEMENT_PAGE = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"
"""
Base element page

By appending an element name, you get the docs for that element
"""


MDN_BASE = "https://developer.mozilla.org/en-US/docs/Web/"
"""
Base page of MDN
"""


def htmlElementReplace(lookup: str, presentation: str | None = None) -> str:
    """
    Replace text in an HTML reference
    """
    if presentation is None:
        presentation = f"<{lookup.lower()}>"

    url = f"https://developer.mozilla.org/en-US/docs/Web/HTML/Element/{lookup}"

    return f"[{presentation}]({url})"


def glossaryReplace(lookup: str, presentation: str | None = None) -> str:
    """
    Replace text in a glossary reference
    """
    if presentation is None:
        presentation = lookup

    url = f"https://developer.mozilla.org/en-US/docs/Glossary/{lookup}"

    return f"[{presentation}]({url})"


def cssXrefReplace(lookup: str, presentation: str | None = None) -> str:
    """
    Replace text for CSS cross reference lookup
    """
    if presentation is None:
        presentation = lookup

    url = f"https://developer.mozilla.org/en-US/docs/Web/CSS/{lookup}"

    return f"[{presentation}]({url})"


def domXrefReplace(lookup: str, presentation: str | None = None) -> str:
    """
    Replace text for DOM cross reference lookup
    """
    if presentation is None:
        presentation = lookup

    url = f"https://developer.mozilla.org/en-US/docs/Web/API/{lookup}"

    return f"[{presentation}]({url})"


DESCRIPTION_LOOKUPS = {
    "htmlelement": htmlElementReplace,
    "glossary": glossaryReplace,
    "cssxref": cssXrefReplace,
    "domxref": domXrefReplace,
}


TagMdnInfo = tuple[str, str]
"""Type definition for info grabbed from MDN docs"""


class AttrYmlItem(TypedDict):
    """
    Attributes of a tag, defined in tags.yml
    """

    doc: str
    """Documentation for the attribute"""

    default: NotRequired[str]
    """
    Default value of the attribute - this is passed to eval to convert to
    Python code.
    """

    type: NotRequired[str]
    """Python type to accept for the attribute"""


class RenderOptionsYmlItem(TypedDict):
    """
    Render options as a dictionary
    """

    indent: NotRequired[str]
    spacing: NotRequired[str]


class TagsYmlItem(TypedDict):
    """
    A tag which has suggested keys
    """

    skip: NotRequired[bool]
    """Whether to skip this tag when generating tags"""

    attributes: NotRequired[dict[str, str | AttrYmlItem]]
    """Mapping of attributes used by the tag (name: description)"""

    base: NotRequired[str]
    """Name of the base class to derive from (eg SelfClosingTag)"""

    rename: NotRequired[str]
    """Value to rename the class to (to avoid bad keyword usage)"""

    escape_children: NotRequired[bool]
    """Whether to escape the contents of the tag (default True)"""

    pre_content: NotRequired[str]
    """
    Pre-content for the element (eg `<!DOCTYPE html>`)
    """

    render_options: NotRequired[RenderOptionsYmlItem]
    """
    Render options for this element
    """


TagsYaml = dict[str, TagsYmlItem]
"""Type alias for type of tags.yml file"""


@dataclass
class Attr:
    """
    Information about a attribute
    """

    name: str
    """
    Name of the attribute
    """

    doc: str | None
    """
    Documentation of the attribute if applicable
    """

    type: str
    """
    Type to accept for the attribute
    """

    default: Any | None
    """
    Default value for the attribute
    """


@dataclass
class TagInfo:
    """
    Information about a tag
    """

    name: str
    """
    Name of the tag
    """

    description: str
    """
    Description of the tag, yoinked from MDN
    """

    base: str
    """
    Name of the base class to use for the tag (default "Tag")
    """

    mdn_link: str
    """
    Link to full documentation on MDN
    """

    escape_children: bool
    """
    Whether to escape child elements for the tag
    """

    attributes: list[Attr]
    """
    List of attributes and their documentation.
    """

    pre_content: str | None
    """
    Pre-content for the element (eg `<!DOCTYPE html>`)
    """

    render_options: RenderOptions | None
    """
    Render options
    """


def fetch_mdn():
    """
    Fetch MDN docs page and return the contents
    """
    # TODO: Error handling
    docs = requests.get(MDN_WEB_DOCS)
    return docs.text


def handle_header_elements(description) -> list[TagMdnInfo]:
    """
    Because the markdown for header levels is very gross, we're just doing it
    manually.
    """

    tags = []

    for i in range(6):
        tags.append((f"h{i + 1}", description))

    return tags


def format_description(description: str, ele: str) -> str:
    """
    Replace parts of the description to fix broken links

    Also includes element name for debugging purposes
    """
    # Manual links
    description = description.replace(
        "](/en-US/docs/Web/",
        f"]({MDN_BASE}",
    )

    # Other elements - keep looping until none left
    while (start := description.find("{{")) != -1:
        end = description.find("}}", start)

        element_text = description[start + 2 : end]
        # In format key("arg1", "arg2")

        key, args = element_text.split("(")
        args = args.removesuffix(")")

        # Split up args
        if "," in args:
            # Two args
            lookup, presentation = args.split(",")
            presentation.strip()
            lookup = lookup.replace('"', "")
            presentation = presentation.replace('"', "")

        else:
            # One arg (presentation determined automatically
            lookup = args.replace('"', "")
            presentation = None

        # Check for missing keys
        if key.lower() not in DESCRIPTION_LOOKUPS:
            print(f"lookup '{key}' not in table", file=sys.stderr)
            print(f"Element: {ele}", file=sys.stderr)
            exit(1)

        # Replace elements
        description = (
            description[:start]
            + DESCRIPTION_LOOKUPS[key.lower()](lookup, presentation)
            + description[end + 2 :]
        )

    return description


def parse_markdown_table(lines: Iterator[str]) -> list[TagMdnInfo]:
    """
    Parse table from markdown
    """

    # Read in header row
    assert next(lines).startswith("| ---")

    # Now grab each line
    tags: list[TagMdnInfo] = []
    try:
        while (line := next(lines)).startswith("|"):
            _, tag_base, description, _ = line.split("|")

            tag_base = tag_base.strip()

            # Header elements are yucky - we should handle them separately
            if tag_base.startswith("[`<h1>`]"):
                tags.extend(handle_header_elements(description))
                continue

            tag_name = tag_base.removeprefix('{{HTMLElement("').removesuffix(
                '")}}'
            )

            description = format_description(description.strip(), tag_name)

            # Element name should be of the format `{{HTMLElement("<name>")}}``
            # Grab the actual name
            if not tag_base.startswith('{{HTMLElement("'):
                print(f"!!!! SKIPPED {tag_base}", file=sys.stderr)
                continue
            assert tag_base.endswith('")}}')
            tags.append((tag_name, description))

    except StopIteration:
        pass
    return tags


def parse_markdown(lines: Iterator[str]) -> list[TagMdnInfo]:
    """
    Parse markdown from MDN

    1. Find tables
    2. If they have the columns "Element" and "Description", read each row
    3. For each row, add a tuple[str, str] for element name and element
       description

    Returns list of names and descriptions
    """
    tags = []

    try:
        while True:
            line = next(lines)

            if line == "## Obsolete and deprecated elements":
                print("Skip obsolete tags", file=sys.stderr)
                break

            if line.replace(" ", "") == "|Element|Description|":
                # Start of table
                tags.extend(parse_markdown_table(lines))

    except StopIteration:
        pass

    return tags


def scrape_html_elements() -> list[TagMdnInfo]:
    """
    Grab a list of HTML elements from MDN, and parse them into a format that
    is usable for our purposes.
    """
    text = fetch_mdn()
    parsed = parse_markdown(iter(text.splitlines()))
    return parsed


def load_tag_attrs_yaml() -> TagsYaml:
    """
    Load tags configuration
    """
    with open(TAGS_YAML) as f:
        return yaml.load(f, yaml.Loader)


def attr_entries_to_object(tags: TagsYaml, tag_name: str) -> list[Attr]:
    """
    Convert a tags yaml entry into a Attr object for use elsewhere, given its
    name.

    For items with no entries, give no attributes
    """
    if tag_name not in tags:
        return []

    tag_data = tags[tag_name]

    if "attributes" not in tag_data:
        return []

    attrs = []
    for name, value in tag_data["attributes"].items():
        if isinstance(value, str):
            doc: str | None = value
            default: str | None = None
            type = "AttributeType"
        else:
            doc = value.get("doc")
            # NOTE: This is safe, as it is only ever run at compile time
            # This code is not distributed to users' systems
            default = eval(value["default"]) if "default" in value else None
            type = value.get("type", "AttributeType")
        attrs.append(Attr(name, doc, type, default))
    return attrs


def get_tag_rename(tags: TagsYaml, tag_name: str) -> str:
    """
    Return the name that should be used for a tag. Used to rename tags that
    use reserved Python keywords
    """
    if tag_name not in tags:
        return tag_name
    tag = tags[tag_name]
    if "rename" not in tag:
        return tag_name
    else:
        return tag["rename"]


def get_tag_base_class(tags: TagsYaml, tag_name: str) -> str:
    """
    Return the base class to use for a tag
    """
    if tag_name not in tags:
        return "Tag"
    tag = tags[tag_name]
    if "base" not in tag:
        return "Tag"
    else:
        return tag["base"]


def get_tag_skip(tags: TagsYaml, tag_name: str) -> bool:
    """
    Return whether to skip this tag
    """
    if tag_name not in tags:
        return False
    tag = tags[tag_name]
    return tag.get("skip", False)


def get_tag_escape_children(tags: TagsYaml, tag_name: str) -> bool:
    """
    Return whether to skip this tag
    """
    if tag_name not in tags:
        return True
    tag = tags[tag_name]
    return tag.get("escape_children", True)


def get_tag_pre_content(tags: TagsYaml, tag_name: str) -> str | None:
    """
    Return pre-content for the tag
    """
    if tag_name not in tags:
        return None
    tag = tags[tag_name]
    return tag.get("pre_content", None)


def get_tag_render_options(
    tags: TagsYaml, tag_name: str
) -> RenderOptions | None:
    """
    Return pre-content for the tag
    """
    if tag_name not in tags:
        return None
    tag = tags[tag_name]
    if "render_options" in tag:
        return RenderOptions(**tag["render_options"])
    else:
        return None


def make_mdn_link(tag: str) -> str:
    """Generate an MDN docs link for the given tag"""
    return f"{MDN_ELEMENT_PAGE}/{tag}"


def elements_to_element_structs(
    mdn_data: list[TagMdnInfo],
    tag_attrs: TagsYaml,
) -> list[TagInfo]:
    """
    Combine all MDN tag info with our own info (where applicable)
    """
    output = []

    for name, description in mdn_data:
        # Skip tag if specified
        if get_tag_skip(tag_attrs, name):
            continue

        output.append(
            TagInfo(
                name=get_tag_rename(tag_attrs, name),
                description=description,
                base=get_tag_base_class(tag_attrs, name),
                mdn_link=make_mdn_link(name),
                escape_children=get_tag_escape_children(tag_attrs, name),
                attributes=attr_entries_to_object(tag_attrs, name),
                pre_content=get_tag_pre_content(tag_attrs, name),
                render_options=get_tag_render_options(tag_attrs, name),
            )
        )

    return output


def main():
    """
    Main logic of the scraper
    """
    mdn_elements = scrape_html_elements()
    tag_attrs = load_tag_attrs_yaml()

    return elements_to_element_structs(mdn_elements, tag_attrs)


def print_elements(parsed: list[TagInfo]):
    """
    Little helper function for printing parsed elements, used for sanity
    checking
    """
    for ele in parsed:
        print(ele.name)
        print(ele.description)
        print(ele.mdn_link)
        print()
        print(ele.attributes)
        print()
        print("------------------")
        print()


if __name__ == "__main__":
    print_elements(main())
