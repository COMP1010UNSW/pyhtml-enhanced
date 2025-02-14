"""
# `<PyHTML/>`

A library for building HTML documents with a simple and learnable syntax,
inspired by (and similar to)
[Cenk Altı's PyHTML library](https://github.com/cenkalti/pyhtml), but
with improved documentation and type safety.

Learn more by reading [the documentation](https://comp1010unsw.github.io/pyhtml-enhanced/).

## Features

* Inline documentation and type safety for all tags.

* Editor support for many common tags (attribute suggestions).

* A modern and readable codebase.

* 100% test coverage.

## Usage

```py
>>> import pyhtml as p
>>> my_website = p.html(
...     p.head(
...         p.title("Hello, world!"),
...         p.script(src="http://example.com/script.js"),
...     ),
...     p.body(
...         p.h1("Hello, world!"),
...         p.p("This is my amazing website!"),
...     ),
... )
>>> print(str(my_website))
<!DOCTYPE html>
<html>
  <head>
    <title>
      Hello, world!
    </title>
    <script type="text/javascript" src="http://example.com/script.js"></script>
  </head>
  <body>
    <h1>
      Hello, world!
    </h1>
    <p>This is my amazing website!</p>
  </body>
</html>

```
"""

# Disable Flake8, since it really doesn't like our docstring above
# flake8: noqa
from .__tag_base import Tag, create_tag, SelfClosingTag, WhitespaceSensitiveTag

from .__tags import input_, object_
from .__render_options import RenderOptions

__all__ = [
    "Tag",
    "create_tag",
    "SelfClosingTag",
    "WhitespaceSensitiveTag",
    "DangerousRawHtml",
    "Comment",
    "input_",
    "object_",
    "RenderOptions",
    "html",
    "base",
    "head",
    "link",
    "meta",
    "style",
    "title",
    "body",
    "address",
    "article",
    "aside",
    "footer",
    "header",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hgroup",
    "main",
    "nav",
    "section",
    "search",
    "blockquote",
    "dd",
    "div",
    "dl",
    "dt",
    "figcaption",
    "figure",
    "hr",
    "li",
    "menu",
    "ol",
    "p",
    "pre",
    "ul",
    "a",
    "abbr",
    "b",
    "bdi",
    "bdo",
    "br",
    "cite",
    "code",
    "data",
    "dfn",
    "em",
    "i",
    "kbd",
    "mark",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "time",
    "u",
    "var",
    "wbr",
    "area",
    "audio",
    "img",
    "map",
    "track",
    "video",
    "embed",
    "fencedframe",
    "iframe",
    "object",
    "picture",
    "source",
    "canvas",
    "noscript",
    "script",
    "del_",
    "ins",
    "caption",
    "col",
    "colgroup",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "button",
    "datalist",
    "fieldset",
    "form",
    "input",
    "label",
    "legend",
    "meter",
    "optgroup",
    "option",
    "output",
    "progress",
    "select",
    "textarea",
    "details",
    "dialog",
    "summary",
    "slot",
    "template",
]


from .__tags import (
    DangerousRawHtml,
    Comment,
    html,
    base,
    head,
    link,
    meta,
    style,
    title,
    body,
    address,
    article,
    aside,
    footer,
    header,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hgroup,
    main,
    nav,
    section,
    search,
    blockquote,
    dd,
    div,
    dl,
    dt,
    figcaption,
    figure,
    hr,
    li,
    menu,
    ol,
    p,
    pre,
    ul,
    a,
    abbr,
    b,
    bdi,
    bdo,
    br,
    cite,
    code,
    data,
    dfn,
    em,
    i,
    kbd,
    mark,
    q,
    rp,
    rt,
    ruby,
    s,
    samp,
    small,
    span,
    strong,
    sub,
    sup,
    time,
    u,
    var,
    wbr,
    area,
    audio,
    img,
    map,
    track,
    video,
    embed,
    fencedframe,
    iframe,
    object,
    picture,
    source,
    canvas,
    noscript,
    script,
    del_,
    ins,
    caption,
    col,
    colgroup,
    table,
    tbody,
    td,
    tfoot,
    th,
    thead,
    tr,
    button,
    datalist,
    fieldset,
    form,
    input,
    label,
    legend,
    meter,
    optgroup,
    option,
    output,
    progress,
    select,
    textarea,
    details,
    dialog,
    summary,
    slot,
    template,
)
