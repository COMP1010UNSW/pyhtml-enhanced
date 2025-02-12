"""
# Tests / Escape test

Tests for escape sequences
"""

import keyword

import pytest

from pyhtml import body, style

replacements = [
    ("&", "&amp;"),
    ("<", "&lt;"),
    (">", "&gt;"),
    ('"', "&quot;"),
    ("'", "&#x27;"),
    # ('\n', ' '),
]


@pytest.mark.parametrize(("string", "replacement"), replacements)
def test_escapes_children(string, replacement):
    assert str(
        body(
            f"Hello{string}world",
        )
    ) == "\n".join(
        [
            "<body>",
            f"  Hello{replacement}world",
            "</body>",
        ]
    )


@pytest.mark.parametrize(("string", "replacement"), replacements)
def test_escapes_attribute_values(string: str, replacement: str):
    assert (
        str(body(value=f"hello{string}world"))
        == f'<body value="hello{replacement}world"></body>'
    )


def test_attribute_names_escapes_dashes():
    """
    Since dashes can't be given as kwarg names, we need to use underscores
    instead. Are they replaced correctly
    """
    assert str(body(my_value="hi")) == '<body my-value="hi"></body>'


@pytest.mark.parametrize(
    "keyword",
    # On Python 3.9, __peg_parser__ is a reserved keyword because of an
    # easter egg (https://stackoverflow.com/q/65486981/6335363)
    # skip over it because there is no point making it work
    filter(lambda kw: kw != "__peg_parser__", keyword.kwlist),
)
def test_attribute_names_escapes_python_keywords_prefix(keyword: str):
    """
    Since Python keywords cannot be given as kwarg names, we need to use
    escaped versions (eg _for => for)
    """
    kwargs = {f"_{keyword}": "hi"}
    assert str(body(**kwargs)) == f'<body {keyword}="hi"></body>'


@pytest.mark.parametrize(
    "keyword",
    # Skip __peg_parser__ in Python 3.9 (see test above)
    filter(lambda kw: kw != "__peg_parser__", keyword.kwlist),
)
def test_attribute_names_escapes_python_keywords_suffix(keyword: str):
    """
    Since Python keywords cannot be given as kwarg names, we need to use
    escaped versions (eg for_ => for)
    """
    kwargs = {f"{keyword}_": "hi"}
    assert str(body(**kwargs)) == f'<body {keyword}="hi"></body>'


def test_style_tags_are_not_escaped():
    assert str(style("&'\"<>")) == "\n".join(
        [
            '<style type="text/css">',
            "  &'\"<>",
            "</style>",
        ]
    )
