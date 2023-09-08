"""
# Meta / Scrape Tags

Using the MDN documentation on HTML elements, generate all HTML element classes
including their documentation.

It also embeds suggested kwargs for some elements, using info from tags.yml.
"""
from dataclasses import dataclass
from typing import Optional, TypedDict, NotRequired
from collections.abc import Iterator
import requests
import yaml


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


TagMdnInfo = tuple[str, str]
"""Type definition for info grabbed from MDN docs"""


class TagsYmlItem(TypedDict):
    """
    A tag which has suggested keys
    """
    properties: NotRequired[dict[str, str]]
    """Mapping of properties used by the tag (name: description)"""

    base: NotRequired[str]
    """Name of the base class to derive from (eg SelfClosingTag)"""

    rename: NotRequired[str]
    """Value to rename the class to (to avoid bad keyword usage)"""


TagsYaml = dict[str, TagsYmlItem]
"""Type alias for type of tags.yml file"""


@dataclass
class Prop:
    """
    Information about a property
    """

    name: str
    """
    Name of the property
    """

    description: Optional[str]
    """
    Description of the property if applicable
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

    properties: Optional[list[Prop]]
    """
    List of properties and their documentation.
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
        tags.append((f"h{i+1}", description))

    return tags


def parse_markdown_table(lines: Iterator[str]) -> list[TagMdnInfo]:
    """
    Parse table from markdown
    """

    # Read in header row
    assert next(lines).startswith('| ---')

    # Now grab each line
    tags: list[TagMdnInfo] = []
    try:
        while (line := next(lines)).startswith('|'):
            _, tag_base, description, _ = line.split('|')

            tag_base = tag_base.strip()
            description = description.strip()

            # Header elements are yucky - we should handle them separately
            if tag_base.startswith("[`<h1>`]"):
                tags.extend(handle_header_elements(description))
                continue

            tag_name = tag_base\
                .removeprefix('{{HTMLElement("')\
                .removesuffix('")}}')

            # Element name should be of the format `{{HTMLElement("<name>")}}``
            # Grab the actual name
            if not tag_base.startswith('{{HTMLElement("'):
                print(f"!!!! SKIPPED {tag_base}")
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
                print("Skip obsolete")
                break

            if line.replace(' ', '') == '|Element|Description|':
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


def load_tag_props_yaml() -> TagsYaml:
    """
    Load tags configuration
    """
    with open(TAGS_YAML) as f:
        return yaml.load(f, yaml.Loader)


def prop_entries_to_object(
    tags: TagsYaml,
    tag_name: str,
) -> Optional[list[Prop]]:
    """
    Convert a tags yaml entry into a Prop object for use elsewhere, given its
    name.

    For items with no entries, give no properties
    """
    if tag_name not in tags:
        return None

    tag_data = tags[tag_name]

    if 'properties' not in tag_data:
        return None

    props = []
    for name, description in tag_data['properties'].items():
        props.append(Prop(name, description))
    return props


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
        return tag['rename']


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
        return tag['base']


def make_mdn_link(tag: str) -> str:
    """Generate an MDN docs link for the given tag"""
    return f"{MDN_ELEMENT_PAGE}/{tag}"


def elements_to_element_structs(
    mdn_data: list[TagMdnInfo],
    tag_props: TagsYaml,
) -> list[TagInfo]:
    """
    Combine all MDN tag info with our own info (where applicable)
    """
    output = []

    for name, description in mdn_data:
        output.append(TagInfo(
            name=get_tag_rename(tag_props, name),
            description=description,
            base=get_tag_base_class(tag_props, name),
            mdn_link=make_mdn_link(name),
            properties=prop_entries_to_object(tag_props, name),
        ))

    return output


def main():
    """
    Main logic of the scraper
    """
    mdn_elements = scrape_html_elements()
    tag_props = load_tag_props_yaml()

    return elements_to_element_structs(mdn_elements, tag_props)


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
        print(ele.properties)
        print()
        print('------------------')
        print()


if __name__ == '__main__':
    print_elements(main())
