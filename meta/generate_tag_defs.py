"""
# Meta / Generate Tag Defs

Code for generating tag definitions
"""
from pathlib import Path
import sys
from typing import TextIO
from .scrape_tags import main as generate_tag_data, TagInfo


TEMPLATES_FOLDER = Path('./meta/templates')


def get_template_class_no_props():
    """
    Returns the template for when there are no properties
    """
    return open(TEMPLATES_FOLDER.joinpath('class_no_props.py')).read()


def get_template_class(name: str):
    try:
        return open(TEMPLATES_FOLDER.joinpath(f"class_props_{name}.py")).read()
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

    # Generate property arguments and unions
    # To get a better idea of these, look inside the template files to see
    # what would be replaced
    prop_args_gen = []
    prop_unions_gen = []
    for prop in tag.properties:
        # Yucky hard-coded spaces, I can't be bothered to fix this
        prop_args_gen.append(f"        {prop.name}: Any = None,")
        prop_unions_gen.append(f"            '{prop.name}': {prop.name},")

    prop_args = '\n'.join(prop_args_gen).strip()
    prop_unions = '\n'.join(prop_unions_gen).strip()

    # Determine whether the class should mandate keyword-only args
    # If there are no named properties, we set it to '' to avoid a syntax error
    # Otherwise, we add a `*,` to prevent kwargs from being used as positional
    # args in self-closing tags
    if len(tag.properties):
        kw_only = '*,'
    else:
        kw_only = ''

    # Now we just need to replace in all of the templated properties
    text = text\
        .replace("{name}", tag.name)\
        .replace("{base}", tag.base)\
        .replace("{description}", tag.description)\
        .replace("{link}", tag.mdn_link)\
        .replace("{prop_args}", prop_args)\
        .replace("{prop_unions}", prop_unions)\
        .replace("{kw_only}", kw_only)

    print(text, file=output)
    # And a nice trailing newline to make flake8 happy
    print(file=output)


def main(output: TextIO):
    """
    Generate the tag definitions Python file
    """
    tags = generate_tag_data()

    with open(TEMPLATES_FOLDER.joinpath('main.py')) as f:
        print(f.read(), file=output)

    for tag in tags:
        # Generate the tag
        generate_tag_class(output, tag)

    # Also print out things to copy across to various files
    print("# Copy this into pyhtml/__tags/__init__.py")
    print("__all__ = [")
    for tag in tags:
        print(f"    '{tag.name}',")
    print("]")
    print()
    print()
    print("from .generated import (")
    for tag in tags:
        print(f"    {tag.name},")
    print(")")

    print()
    print("------------------------------------------------")
    print()

    print("# Copy this into pyhtml/__init__.py")
    print("__all__ = [")
    for tag in tags:
        print(f"    '{tag.name}',")
    print("    # TODO: Modify to contain other named exports as required")
    print("]")
    print()
    print()
    print("from .__tags import (")
    for tag in tags:
        print(f"    {tag.name},")
    print("    # TODO: Add other tags as required")
    print(")")


if __name__ == '__main__':
    main(output=sys.stdout)
