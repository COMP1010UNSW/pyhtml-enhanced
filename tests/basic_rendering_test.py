"""
# Tests / Basic rendering test

Basic tests for rendering HTML
"""
from pyhtml import html, head, title, body, h1, p, Comment, del_, script


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


def test_renders_properties():
    doc = html(foo="bar")

    assert str(doc) == '<html foo="bar"></html>'


def test_comment_renders():
    assert str(Comment("Hello world")) == '\n'.join([
        '<!--',
        'Hello world',
        '-->',
    ])


def test_call_adds_props():
    """Calling a tag adds additional properties"""
    # Note that order is important - elements added first should appear first
    assert str(html(foo="bar")(baz="bat")) \
        == '<html foo="bar" baz="bat"></html>'


def test_call_adds_children():
    """Calling a tag adds additional children"""
    # Note that order is important again
    assert str(html("Hello", "World")) == '\n'.join([
        '<html>',
        '  Hello',
        '  World',
        '</html>',
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
        '    <script src="http://example.com/script.js"></script>',
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
