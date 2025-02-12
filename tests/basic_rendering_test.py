"""
# Tests / Basic rendering test

Basic tests for rendering HTML
"""

import pytest

from pyhtml import (
    Comment,
    a,
    body,
    br,
    del_,
    div,
    h1,
    head,
    html,
    input,
    pre,
    script,
    span,
    title,
)


def test_renders_single_element():
    doc = body()

    assert str(doc) == "<body></body>"


def test_renders_elements_with_children():
    doc = body(
        span(),
        div(),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <span></span>",
            "  <div></div>",
            "</body>",
        ]
    )


def test_renders_deeply_nested_children():
    doc = body(
        div(
            span("Hello world"),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div>",
            "    <span>",
            "      Hello world",
            "    </span>",
            "  </div>",
            "</body>",
        ]
    )


def test_renders_attributes():
    doc = body(foo="bar")

    assert str(doc) == '<body foo="bar"></body>'


def test_comment_renders():
    assert str(Comment("Hello world")) == "\n".join(
        [
            "<!--",
            "  Hello world",
            "-->",
        ]
    )


def test_comments_not_callable():
    """Comments cannot be called"""
    with pytest.raises(TypeError):
        Comment("Hello world")()


def test_call_adds_attrs():
    """Calling a tag adds additional attributes"""
    # Note that order is important - elements added first should appear first
    assert (
        str(body(foo="bar")(baz="bat")) == '<body foo="bar" baz="bat"></body>'
    )


def test_call_adds_children():
    """Calling a tag adds additional children"""
    # Note that order is important again
    assert str(body("Hello")("World")) == "\n".join(
        [
            "<body>",
            "  Hello",
            "  World",
            "</body>",
        ]
    )


def test_call_adds_mixed_attrs_children():
    """Calling a tag adds more properties"""
    assert str(body(foo="bar")("Hello")) == "\n".join(
        [
            '<body foo="bar">',
            "  Hello",
            "</body>",
        ]
    )


def test_call_adds_mixed_attrs_children_link():
    """Calling a tag adds more properties, using an anchor tag"""
    assert str(
        a(href="https://www.youtube.com/watch?v=dQw4w9WgXcQ")("Click me")
    ) == "\n".join(
        [
            '<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">',
            "  Click me",
            "</a>",
        ]
    )


def test_call_adds_mixed_attrs_children_script():
    """Calling a tag adds more properties, using a script tag"""
    assert str(script(type="blah/blah")("// Some JS")) == "\n".join(
        [
            '<script type="blah/blah">',
            "  // Some JS",
            "</script>",
        ]
    )


def test_call_adds_mixed_attrs_children_script_2():
    """Calling a tag adds more properties, using a script tag"""
    assert str(script("// Some JS")(type="blah/blah")) == "\n".join(
        [
            '<script type="blah/blah">',
            "  // Some JS",
            "</script>",
        ]
    )


def test_tags_with_trailing_underscore_render_without():
    """
    Some tags have a trailing underscore to avoid name collisions. When
    rendering to HTML, is this removed?
    """
    assert str(del_()) == "<del></del>"


def test_larger_page():
    """Does it render a larger page in a reasonable way?"""
    my_website = html(
        head(
            title("Hello, world!"),
            script(src="http://example.com/script.js"),
        ),
        body(
            h1("Hello, world!"),
            span("This is my amazing website rendered with PyHTML Enhanced!"),
        ),
    )

    assert str(my_website) == "\n".join(
        [
            "<!DOCTYPE html>",
            "<html>",
            "  <head>",
            "    <title>",
            "      Hello, world!",
            "    </title>",
            '    <script type="text/javascript" '
            'src="http://example.com/script.js"></script>',
            "  </head>",
            "  <body>",
            "    <h1>",
            "      Hello, world!",
            "    </h1>",
            "    <span>",
            "      This is my amazing website rendered with PyHTML Enhanced!",
            "    </span>",
            "  </body>",
            "</html>",
        ]
    )


def test_format_through_repr():
    """Is HTML rendered through repr?"""
    doc = body()

    assert repr(doc) == "<body></body>"


def test_flatten_element_lists():
    """
    If a list of elements is given as a child element, each element should be
    considered as a child.
    """
    doc = body([span("Hello"), span("world")])

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <span>",
            "    Hello",
            "  </span>",
            "  <span>",
            "    world",
            "  </span>",
            "</body>",
        ]
    )


def test_flatten_element_generators():
    """
    If a generator of elements is given as a child element, each element
    yielded should be considered as a child.
    """
    doc = body(c for c in "hi")

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  h",
            "  i",
            "</body>",
        ]
    )


def test_flatten_element_other_sequence():
    """
    If a tuple of elements is given as a child element, each element should be
    considered as a child.
    """
    doc = body(("h", "i"))

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  h",
            "  i",
            "</body>",
        ]
    )


def test_classes_can_render():
    """
    Can a class by itself be rendered individually?
    """
    doc = body(br)

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <br/>",
            "</body>",
        ]
    )


def test_boolean_tag_attributes_true():
    """
    Do boolean attributes of tags render correctly
    """
    assert str(input(readonly=True)) == "<input readonly/>"


def test_boolean_tag_attributes_false():
    """
    Do boolean attributes of tags render correctly

    Attributes with value `False` are skipped
    """
    assert str(input(readonly=False)) == "<input/>"


def test_tag_with_pre_content():
    """
    Do tags with defined pre-content render correctly
    """
    assert str(html()) == "<!DOCTYPE html>\n<html></html>"


def test_whitespace_sensitive_no_content():
    """
    Do whitespace-sensitive tags render properly when they have no content?
    """
    assert str(pre()) == "<pre></pre>"


def test_whitespace_sensitive_with_content():
    """
    Do whitespace-sensitive tags render properly when they have content?
    """
    assert str(pre("hi")) == "<pre>hi</pre>"


def test_whitespace_sensitive_with_attrs():
    """
    Do whitespace-sensitive tags render properly when they have attributes?
    """
    assert str(pre(test="test")("hi")) == '<pre test="test">hi</pre>'
