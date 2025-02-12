"""
# Tests / render options test

Test cases for specifying rendering options
"""

import pyhtml as p


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
