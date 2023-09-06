"""
# Tests / Basic rendering test

Basic tests for rendering HTML
"""
from pyhtml_enhanced import html, head, body


def test_renders_single_element():
    doc = html()

    assert str(doc) == "<html />"


def test_renders_elements_with_children():
    doc = html(
        head(),
        body(),
    )

    assert str(doc) == '\n'.join([
        '<html>',
        '  <head />',
        '  <body />',
        '</html>',
    ])
