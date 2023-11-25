"""
# Tests / Escape test

Tests for escape sequences
"""
import pytest
import keyword
from pyhtml import html


replacements = [
    ('&', '&amp;'),
    ('<', '&lt;'),
    ('>', '&gt;'),
    ('"', '&quot;'),
    ("'", '&#x27;'),
    # ('\n', ' '),
]


@pytest.mark.parametrize(
    ('string', 'replacement'),
    replacements
)
def test_escapes_children(string, replacement):
    assert str(html(
        f"Hello{string}world",
    )) == '\n'.join([
        '<html>',
        f'  Hello{replacement}world',
        '</html>',
    ])


@pytest.mark.parametrize(
    ('string', 'replacement'),
    replacements
)
def test_escapes_attribute_values(string: str, replacement: str):
    assert str(html(value=f"hello{string}world")) \
        == f'<html value="hello{replacement}world"></html>'


def test_attribute_names_escapes_dashes():
    """
    Since dashes can't be given as kwarg names, we need to use underscores
    instead. Are they replaced correctly
    """
    assert str(html(my_value="hi")) == '<html my-value="hi"></html>'


@pytest.mark.parametrize(
    'keyword',
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
    kwargs = {f"_{keyword}": 'hi'}
    assert str(html(**kwargs)) == f'<html {keyword}="hi"></html>'


@pytest.mark.parametrize(
    'keyword',
    # Skip __peg_parser__ in Python 3.9 (see test above)
    filter(lambda kw: kw != "__peg_parser__", keyword.kwlist),
)
def test_attribute_names_escapes_python_keywords_suffix(keyword: str):
    """
    Since Python keywords cannot be given as kwarg names, we need to use
    escaped versions (eg for_ => for)
    """
    kwargs = {f"{keyword}_": 'hi'}
    assert str(html(**kwargs)) == f'<html {keyword}="hi"></html>'
