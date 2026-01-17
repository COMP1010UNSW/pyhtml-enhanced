"""
# Tests / T-string test

Test cases for rendering of t-strings.

We need to create the `Template` objects manually, as otherwise even attempting
to import this test file would cause a SyntaxError before Pytest has the
opportunity to skip the test cases.
"""

import sys

import pytest

import pyhtml as p

if sys.version_info >= (3, 14):
    from string.templatelib import Interpolation, Template
else:  # pragma: no cover
    pytest.skip(
        "T-strings only exist in Python >= 3.14",
        allow_module_level=True,
    )


def test_renders_child_element():
    t = Template("Hello, ", Interpolation(p.b("world!")))
    assert str(p.p(t)) == "<p>Hello, <b>world!</b></p>"


def test_interpolates_other_values():
    t = Template(
        "At age ", Interpolation(100), " you will get a message from the king."
    )
    assert (
        str(p.p(t))
        == "<p>At age 100 you will get a message from the king.</p>"
    )


def test_renders_uninstantiated_tag_type():
    """Even tags that aren't instantiated, eg `p.br` should still render"""
    t = Template("Hello,", Interpolation(p.br), "world!")
    assert str(p.p(t)) == "<p>Hello,<br/>world!</p>"


def test_nested_templates():
    """Nested template strings still render correctly"""
    inner = Template("be ", Interpolation(p.b("bold")), "!")
    outer = Template(
        "Do not ",
        Interpolation(p.i("forget")),
        " to ",
        Interpolation(p.span(inner)),
    )
    assert (
        str(p.p(outer))
        == "<p>Do not <i>forget</i> to <span>be <b>bold</b>!</span></p>"
    )
