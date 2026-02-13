"""
# Meta / Generate Tag Defs

Code for generating tag definitions
"""

import sys
from io import StringIO
from pathlib import Path
from typing import TextIO

from .scrape_tags import TagInfo
from .scrape_tags import main as generate_tag_data

TEMPLATES_FOLDER = Path("./generator/templates")

NO_ESCAPE_CHILDREN = """
    def _escape_children(self) -> bool:
        return False
"""

GET_PRE_CONTENT = """
    def _get_tag_pre_content(self) -> str | None:
        return {}
"""

GET_DEFAULT_RENDER_OPTIONS = """
    def _get_default_render_options(self) -> RenderOptions:
        return {}
"""


def increase_indent(text: list[str], indent: str) -> list[str]:
    """
    Increase the indentation of all lines in a string list

    This is copied from the original library so that the generator won't fail
    if the library itself is busted.
    """
    return list(map(lambda line: indent + line, text))


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
    attr_docs_outer = "\n".join(increase_indent(attr_docs_gen, "    ")).strip()
    attr_docs_inner = "\n".join(
        increase_indent(attr_docs_gen, "        ")
    ).strip()

    description = tag.description
    if tag.experimental:
        description += "\n\n        This tag is [experimental](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental). Use with caution."

    # Determine whether the class should mandate keyword-only args
    # If there are no named attributes, we set it to '' to avoid a syntax error
    # Otherwise, we add a `*,` to prevent kwargs from being used as positional
    # args in self-closing tags
    kw_only = "*," if len(tag.attributes) else ""

    # Now we just need to replace in all of the templated attributes
    text = (
        text.replace("{name}", tag.name)
        .replace("{base}", tag.base)
        .replace("{description}", description)
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

    # Add render options function if needed
    if tag.render_options is not None:
        print(
            GET_DEFAULT_RENDER_OPTIONS.replace("{}", f"{tag.render_options}"),
            file=output,
        )

    # And a nice trailing newline to make flake8 happy
    print(file=output)


# Additional tags to export from pyhtml/tags/__init__.py
additional_tags = [
    "Comment",
    "DangerousRawHtml",
    "ElementGroup",
    "input",
    "input_",
    "object_",
]
# Start of pyhtml/tags/__init__.py
TAGS_INIT = '''
"""
# PyHTML Enhanced / Tags

Definitions for tags
"""
# This file is auto-generated. See `meta/generate_tag_defs.py` to modify it

from .comment import Comment  # noqa: I001
from .dangerous_raw_html import DangerousRawHtml
from .element_group import ElementGroup
from .input_tag import input
from .renames import input_, object_

'''.lstrip()

# Additional items to export from pyhtml/__init__.py
additional_exports = [
    "Tag",
    "create_tag",
    "SelfClosingTag",
    "WhitespaceSensitiveTag",
    "RenderOptions",
]
# pyhtml/__init__.py, except for the docstring, tag imports and exports
PYHTML_INIT = """
# This file is auto-generated. See `meta/generate_tag_defs.py` to modify it

# Disable Flake8, since it really doesn't like our docstring above
# flake8: noqa

from .__tag_base import (  # noqa: I001
    Tag,
    create_tag,
    SelfClosingTag,
    WhitespaceSensitiveTag,
)
from .__render_options import RenderOptions

"""


def main(generated_tags: TextIO, tags_init: TextIO, pyhtml_init: TextIO):
    """
    Generate the tag definitions Python file
    """
    tags = generate_tag_data()

    with open(TEMPLATES_FOLDER.joinpath("main.py")) as f:
        print(f.read(), file=generated_tags)
        print(file=generated_tags)

    for tag in tags:
        # Generate the tag
        generate_tag_class(generated_tags, tag)

    # And now generate an __all__ to make sure they are all exported
    print("__all__ = [", file=generated_tags)
    for tag in tags:
        print(f"    '{tag.name}',", file=generated_tags)
    print("]", file=generated_tags)

    # Also print out things to copy across to various files
    # Into pyhtml/__tags/__init__.py
    print(TAGS_INIT, file=tags_init)

    # Generated tag imports
    print("from .generated import (", file=tags_init)
    for tag in tags:
        print(f"    {tag.name},", file=tags_init)
    print(")\n\n", file=tags_init)

    print("__all__ = [", file=tags_init)
    for tag in tags:
        print(f'    "{tag.name}",', file=tags_init)
    for tag in additional_tags:
        print(f'    "{tag}",', file=tags_init)
    print("]", file=tags_init)

    # ------------------------------------------------

    # pyhtml/__init__.py

    # Insert readme as docstring
    print('"""', file=pyhtml_init)
    with open("README.md") as readme:
        print(readme.read().strip(), file=pyhtml_init)
    print('"""\n', file=pyhtml_init)
    print(PYHTML_INIT, file=pyhtml_init)

    # Import generated tags
    print("from .__tags import (", file=pyhtml_init)
    for tag in tags:
        print(f"    {tag.name},", file=pyhtml_init)
    for tag in additional_tags:
        print(f"    {tag},", file=pyhtml_init)
    print(")\n\n", file=pyhtml_init)

    print("__all__ = [", file=pyhtml_init)
    for tag in tags:
        print(f'    "{tag.name}",', file=pyhtml_init)
    for tag in additional_tags:
        print(f'    "{tag}",', file=pyhtml_init)
    for export in additional_exports:
        print(f'    "{export}",', file=pyhtml_init)
    print("]", file=pyhtml_init)


if __name__ == "__main__":
    generated = StringIO()
    tags_init = StringIO()
    pyhtml_init = StringIO()
    main(generated, tags_init, pyhtml_init)

    generated.seek(0)
    tags_init.seek(0)
    pyhtml_init.seek(0)

    print("=== Generated ===")
    print(generated.read())
    print()
    print("=== Tags init ===")
    print(tags_init.read())
    print()
    print("=== PyHTML init ===")
    print(pyhtml_init.read())
