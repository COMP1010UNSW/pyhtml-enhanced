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
def test_escapes_property_values(string, replacement):
    assert str(html(value=f"hello{string}world")) \
        == f'<html value="hello{replacement}world"/>'


def test_property_names_escapes_dashes():
    """
    Since dashes can't be given as kwarg names, we need to use underscores
    instead. Are they replaced correctly
    """
    assert str(html(my_value="hi")) == '<html my-value="hi"/>'


@pytest.mark.parametrize(
    'keyword',
    keyword.kwlist,
)
def test_property_names_escapes_python_keywords(keyword):
    """
    Since Python keywords cannot be given as kwarg names, we need to use
    escaped versions (eg _for => for)
    """
    kwargs = {f"_{keyword}": 'hi'}
    assert str(html(**kwargs)) == f'<html {keyword}="hi"/>'
