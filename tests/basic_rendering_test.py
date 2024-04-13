"""
# Tests / Basic rendering test

Basic tests for rendering HTML
"""
import pytest
from pyhtml import (
    html,
    head,
    title,
    body,
    h1,
    p,
    Comment,
    del_,
    script,
    br,
    input,
    a,
)


def test_renders_single_element():
    doc = html()

    assert str(doc) == "<html></html>"


def test_renders_elements_with_children():
    doc = html(
        head(),
        body(),
    )

    assert str(doc) == '\n'.join([
        '<html>',
        '  <head></head>',
        '  <body></body>',
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


def test_renders_attributes():
    doc = html(foo="bar")

    assert str(doc) == '<html foo="bar"></html>'


def test_comment_renders():
    assert str(Comment("Hello world")) == '\n'.join([
        '<!--',
        '  Hello world',
        '-->',
    ])


def test_comments_not_callable():
    """Comments cannot be called"""
    with pytest.raises(TypeError):
        Comment("Hello world")()


def test_call_adds_attrs():
    """Calling a tag adds additional attributes"""
    # Note that order is important - elements added first should appear first
    assert str(html(foo="bar")(baz="bat")) \
        == '<html foo="bar" baz="bat"></html>'


def test_call_adds_children():
    """Calling a tag adds additional children"""
    # Note that order is important again
    assert str(html("Hello")("World")) == '\n'.join([
        '<html>',
        '  Hello',
        '  World',
        '</html>',
    ])


def test_call_adds_mixed_attrs_children():
    """Calling a tag adds more properties"""
    assert str(html(foo="bar")("Hello")) == "\n".join([
        '<html foo="bar">',
        '  Hello',
        '</html>',
    ])


def test_call_adds_mixed_attrs_children_link():
    """Calling a tag adds more properties, using an anchor tag"""
    assert str(
        a(href="https://www.youtube.com/watch?v=dQw4w9WgXcQ")("Click me")
    ) == "\n".join([
        '<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">',
        '  Click me',
        '</a>',
    ])


def test_call_adds_mixed_attrs_children_script():
    """Calling a tag adds more properties, using a script tag"""
    assert str(
        script(type="blah/blah")("// Some JS")
    ) == "\n".join([
        '<script type="blah/blah">',
        '  // Some JS',
        '</script>',
    ])


def test_call_adds_mixed_attrs_children_script_2():
    """Calling a tag adds more properties, using a script tag"""
    assert str(
        script("// Some JS")(type="blah/blah")
    ) == "\n".join([
        '<script type="blah/blah">',
        '  // Some JS',
        '</script>',
    ])


def test_tags_with_trailing_undercore_render_without():
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
            p("This is my amazing website rendered with PyHTML Enhanced!"),
        ),
    )

    assert str(my_website) == '\n'.join([
        '<html>',
        '  <head>',
        '    <title>',
        '      Hello, world!',
        '    </title>',
        '    <script type="text/javascript" '
        'src="http://example.com/script.js"></script>',
        '  </head>',
        '  <body>',
        '    <h1>',
        '      Hello, world!',
        '    </h1>',
        '    <p>',
        '      This is my amazing website rendered with PyHTML Enhanced!',
        '    </p>',
        '  </body>',
        '</html>',
    ])


def test_format_through_repr():
    """Is HTML rendered through repr?"""
    doc = html()

    assert repr(doc) == "<html></html>"


def test_flatten_element_lists():
    """
    If a list of elements is given as a child element, each element should be
    considered as a child.
    """
    doc = html([p("Hello"), p("world")])

    assert str(doc) == "\n".join([
        "<html>",
        "  <p>",
        "    Hello",
        "  </p>",
        "  <p>",
        "    world",
        "  </p>",
        "</html>",
    ])


def test_flatten_element_generators():
    """
    If a list of elements is given as a child element, each element should be
    considered as a child.
    """
    doc = html(c for c in "hi")

    assert str(doc) == "\n".join([
        "<html>",
        "  h",
        "  i",
        "</html>",
    ])


def test_classes_can_render():
    """
    Can a class by itself be rendered individually?
    """
    doc = html(br)

    assert str(doc) == "\n".join([
        "<html>",
        "  <br/>",
        "</html>",
    ])


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
