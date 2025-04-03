"""
# Test / Whitespace Sensitive Test

Tests for rendering whitespace sensitive tags.
"""
import pyhtml as p


def test_pre():
    assert str(p.pre("hello\nworld")) == '\n'.join([
        "<pre>hello",
        "world</pre>",
    ])


def test_textarea():
    assert str(p.textarea("hello\nworld")) == '\n'.join([
        "<textarea>hello",
        "world</textarea>",
    ])


def test_indentation_ignored():
    doc = p.body(p.pre("hello\nworld"))
    assert str(doc) == '\n'.join([
        "<body>",
        "  <pre>hello",
        "world</pre>",
        "</body>",
    ])
