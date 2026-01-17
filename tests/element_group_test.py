"""
# Tests / Element group test

Test cases for the ElementGroup tag.
"""

import pyhtml as p


def test_renders_child_element():
    assert str(p.ElementGroup(p.br())) == "<br/>"


def test_renders_multiple_elements():
    html = p.ElementGroup(
        p.p("Hello"),
        p.p("World"),
    )
    assert str(html) == "\n".join(
        [
            "<p>Hello</p>",
            "<p>World</p>",
        ]
    )


def test_respects_render_options():
    html = p.ElementGroup(
        p.p("Hello"),
        p.p("World"),
        p.RenderOptions(spacing=""),
    )
    assert str(html) == "<p>Hello</p><p>World</p>"
