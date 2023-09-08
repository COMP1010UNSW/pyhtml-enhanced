"""
# Tests / Basic rendering test

Basic tests for rendering HTML
"""
from pyhtml import html, head, body, p


def test_renders_single_element():
    doc = html()

    assert str(doc) == "<html/>"


def test_renders_elements_with_children():
    doc = html(
        head(),
        body(),
    )

    assert str(doc) == '\n'.join([
        '<html>',
        '  <head/>',
        '  <body/>',
        '</html>',
    ])


def test_renders_deeply_nested_children():
    doc = html(
        body(
            p("Hello world"),
        ),
    )

    assert str(doc) == '\n'.join([
        '<html>',
        '  <body>',
        '    <p>',
        '      Hello world',
        '    </p>',
        '  </body>',
        '</html>',
    ])


def test_renders_properties():
    doc = html(foo="bar")

    assert str(doc) == '<html foo="bar"/>'
