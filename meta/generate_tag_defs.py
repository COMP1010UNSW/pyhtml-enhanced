"""
# Meta / Generate Tag Defs

Code for generating tag definitions
"""

import sys
from pathlib import Path
from typing import TextIO

from pyhtml.__util import increase_indent

from .scrape_tags import TagInfo
from .scrape_tags import main as generate_tag_data

TEMPLATES_FOLDER = Path("./meta/templates")

NO_ESCAPE_CHILDREN = """
    def _escape_children(self) -> bool:
        return False
"""

GET_PRE_CONTENT = """
    def _get_tag_pre_content(self) -> Optional[str]:
        return {}
"""


def get_template_class(name: str):
    try:
        return open(TEMPLATES_FOLDER.joinpath(f"class_attrs_{name}.py")).read()
    except FileNotFoundError:
        print(
            f"Failed to find template file using base class {name}!",
            file=sys.stderr,
        )
        exit(1)


def generate_tag_class(output: TextIO, tag: TagInfo):
    """
    Generate the code for a tag
    """
    text = get_template_class(tag.base)

    # Generate default attributes dictionary
    default_attrs = repr({attr.name: attr.default for attr in tag.attributes})

    # Generate attribute arguments, unions and documentation
    # To get a better idea of these, look inside the template files to see
    # what would be replaced
    attr_args_gen = []
    attr_unions_gen = []
    attr_docs_gen = []
    for attr in tag.attributes:
        attr_args_gen.append(
            # Yucky hard-coded spaces, I can't be bothered to fix this
            # Also making everything optional for the sake of users always
            # being able to remove an attribute
            f"        {attr.name}: {attr.type} = None,"
        )
        attr_unions_gen.append(f"            '{attr.name}': {attr.name},")
        # Also mention default value if applicable
        if attr.default is not None:
            attr_docs_gen.append(
                f"* `{attr.name}`: {attr.doc} (defaults to `{attr.default!r}`)"
            )
        else:
            attr_docs_gen.append(f"* `{attr.name}`: {attr.doc}")

    attr_args = "\n".join(attr_args_gen).strip()
    attr_unions = "\n".join(attr_unions_gen).strip()
    attr_docs_outer = "\n".join(increase_indent(attr_docs_gen, 4)).strip()
    attr_docs_inner = "\n".join(increase_indent(attr_docs_gen, 8)).strip()

    # Determine whether the class should mandate keyword-only args
    # If there are no named attributes, we set it to '' to avoid a syntax error
    # Otherwise, we add a `*,` to prevent kwargs from being used as positional
    # args in self-closing tags
    kw_only = "*," if len(tag.attributes) else ""

    # Now we just need to replace in all of the templated attributes
    text = (
        text.replace("{name}", tag.name)
        .replace("{base}", tag.base)
        .replace("{description}", tag.description)
        .replace("{link}", tag.mdn_link)
        .replace("{attr_args}", attr_args)
        .replace("{attr_unions}", attr_unions)
        .replace("{attr_docs_outer}", attr_docs_outer)
        .replace("{attr_docs_inner}", attr_docs_inner)
        .replace("{kw_only}", kw_only)
        .replace("{default_attrs}", default_attrs)
    )

    print(text, file=output)

    # And add the no escape children function if needed
    if not tag.escape_children:
        print(NO_ESCAPE_CHILDREN, file=output)

    # Add pre-content declaration if needed
    if tag.pre_content is not None:
        print(
            GET_PRE_CONTENT.replace("{}", f"'{tag.pre_content}'"),
            file=output,
        )

    # And a nice trailing newline to make flake8 happy
    print(file=output)


def main(output: TextIO):
    """
    Generate the tag definitions Python file
    """
    tags = generate_tag_data()

    with open(TEMPLATES_FOLDER.joinpath("main.py")) as f:
        print(f.read(), file=output)

    for tag in tags:
        # Generate the tag
        generate_tag_class(output, tag)

    # And now generate an __all__ to make sure they are all exported
    print("__all__ = [", file=output)
    for tag in tags:
        print(f"    '{tag.name}',", file=output)
    print("]", file=output)

    # Also print out things to copy across to various files
    print("# Copy this into pyhtml/__tags/__init__.py")
    print("__all__ = [")
    print("    # TODO: Modify to contain other named exports as required")
    for tag in tags:
        print(f"    '{tag.name}',")
    print("]")
    print()
    print()
    # Need a type ignore or mypy freaks out
    print("from .generated import (  # type: ignore")
    for tag in tags:
        print(f"    {tag.name},")
    print(")")

    print()
    print("------------------------------------------------")
    print()

    print("# Copy this into pyhtml/__init__.py")
    print("__all__ = [")
    print("    # TODO: Modify to contain other named exports as required")
    for tag in tags:
        print(f"    '{tag.name}',")
    print("]")
    print()
    print()
    print("from .__tags import (")
    for tag in tags:
        print(f"    {tag.name},")
    print(")")


if __name__ == "__main__":
    main(output=sys.stdout)
