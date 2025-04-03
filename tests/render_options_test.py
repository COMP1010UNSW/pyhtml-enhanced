"""
# Tests / render options test

Test cases for specifying rendering options
"""

import pyhtml as p


def test_repr_render_options():
    assert repr(p.RenderOptions(spacing="")) == "RenderOptions(spacing='')"


def test_indent():
    doc = p.body(
        p.RenderOptions(indent="\t"),
        p.span(),
        p.div(),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "\t<span></span>",
            "\t<div></div>",
            "</body>",
        ]
    )


def test_mixed_indent():
    doc = p.body(
        p.div(
            p.RenderOptions(indent="\t"),
            p.div(),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div>",
            "  \t<div></div>",
            "  </div>",
            "</body>",
        ]
    )


def test_spacing():
    doc = p.body(
        p.RenderOptions(spacing=" "),
        p.div(),
    )

    assert str(doc) == "\n".join(
        [
            "<body> <div></div> </body>",
        ]
    )


def test_mixed_spacing():
    doc = p.body(
        p.div(
            p.RenderOptions(spacing=" "),
            p.div(),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div> <div></div> </div>",
            "</body>",
        ]
    )


def test_spacing_str():
    doc = p.body(
        p.div(
            p.RenderOptions(spacing=" "),
            p.span(p.RenderOptions(spacing="\n"), "hi"),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div> <span>",
            "    hi",
            "  </span> </div>",
            "</body>",
        ]
    )


def test_spacing_inner_newline():
    doc = p.body(
        p.div(
            p.RenderOptions(spacing=" "),
            p.div(
                p.RenderOptions(spacing="\n"),
                p.div(),
            ),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div> <div>",
            "    <div></div>",
            "  </div> </div>",
            "</body>",
        ]
    )


def test_indent_and_spacing_inner_newline():
    doc = p.body(
        p.div(
            p.RenderOptions(spacing=" "),
            p.div(
                p.RenderOptions(spacing="\n", indent="\t"),
                p.div(),
            ),
        ),
    )

    assert str(doc) == "\n".join(
        [
            "<body>",
            "  <div> <div>",
            "  \t<div></div>",
            "  </div> </div>",
            "</body>",
        ]
    )


def test_default_render_options_paragraph():
    doc = p.p("Paragraph")
    assert str(doc) == "<p>Paragraph</p>"


def test_extra_space_is_respected_in_paragraphs():
    doc = p.p(" Paragraph ")
    assert str(doc) == "<p> Paragraph </p>"
