"""
# PyHTML Enhanced

A library for building HTML documents with a simple and learnable syntax,
inspired by (and similar to)
[Cenk Altı's PyHTML library](https://github.com/cenkalti/pyhtml), but
with improved documentation and type safety.

## Features

* Inline documentation and type safety for all tags.

* Editor support for many common tags (attribute suggestions).

* A modern and readable codebase.

* No dependencies.

* 100% test coverage

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
    <p>
      This is my amazing website!
    </p>
  </body>
</html>

```

### Creating elements

Every HTML tag is represented by a `class` that generates that HTML code. For
example, to create a `<br>` element, you could use:

```py
>>> line_break = p.br()
>>> print(str(line_break))
<br/>

```

### Adding children to elements

Any arguments to a tag are used as a child element to the created HTML element.
For example, to create a heading with the text `"My awesome website"`, you
could use

```py
>>> heading = p.h1("My awesome website")
>>> print(str(heading))
<h1>
  My awesome website
</h1>

```

### Adding attributes to elements

Any keyword arguments to a tag are used as an attribute of the created HTML
element. For example, to create a form submit button, you could use

```py
>>> submit_button = p.input(type="submit")
>>> print(str(submit_button))
<input type="submit"/>

```

### Adding attributes and children

In HTML, attributes are specified within the opening tag. Contrastingly, Python
requires keyword arguments (attributes) to be specified after regular arguments
(children). To maintain similarity to writing regular HTML, you can call an
element in order to add more attributes and children. For example, to create
a link to PyHTML's GitHub page, you could use

```py
>>> my_link = p.a(href="https://github.com/COMP1010UNSW/pyhtml-enhanced")("Take a look at the code")
>>> print(str(my_link))
<a href="https://github.com/COMP1010UNSW/pyhtml-enhanced">
  Take a look at the code
</a>

```

### HTML comments

You can add comments to HTML (useful for debugging) by using the `Comment` tag.

```py
>>> comment = p.Comment("This is an HTML comment")
>>> print(str(comment))
<!--
  This is an HTML comment
-->

```

### Rendering HTML

Converting your PyHTML into HTML is as simple as stringifying it!

```py
>>> print(str(p.i("How straightforward!")))
<i>
  How straightforward!
</i>

```

### Custom tags

Since this library includes all modern HTML tags, it is very unlikely that
you'll need to do create a custom tag. However if you really need to, you can
create a class deriving from `Tag`.

```py
>>> class fancytag(p.Tag):
...    ...
>>> print(fancytag())
<fancytag></fancytag>

```

#### Tag base classes

You can derive from various other classes to get more control over how your tag
is rendered:

* `Tag`: default rendering.

* `SelfClosingTag`: tag is self-closing, meaning that no child elements are
  accepted.

* `WhitespaceSensitiveTag`: tag is whitespace-sensitive, meaning that its
  child elements are not indented.

#### Class properties

* `children`: child elements
* `attributes`: element attributes

#### Rendering control functions

You can also override various functions to control the existing rendering.

* `_get_tag_name`: return the name to use for the tag. For example returning
  `"foo"` would produce `<foo>`.

* `_get_default_attributes`: return the default values for attributes.

* `_get_tag_pre_content`: return the pre-content for the tag. For example, the
  `<html>` tag uses this to add the `<!DOCTYPE html>` before the opening tag.

* `_escape_children`: return whether the string child elements should be
  escaped to prevent HTML injection.

* `_render`: render the element and its children, returning the list of lines
  to use for the output. Overriding this should be a last resort, as it is easy
  to subtly break the rendering process if you aren't careful.

Refer to the documentation for `Tag` for more information.

## Differences to PyHTML

There are some minor usage differences compared to the original PyHTML library.

Uninstantiated classes are only rendered if they are given as the child of an
instantiated element.

```py
>>> p.br
<class 'pyhtml.__tags.generated.br'>
>>> print(str(p.html(p.body(p.br))))
<!DOCTYPE html>
<html>
  <body>
    <br/>
  </body>
</html>

```

Calling an instance of a `Tag` will return a new tag containing all elements of
the original tag combined with the new attributes and children, but will not
modify the original instance, as I found the old behaviour confusing and
bug-prone.

```py
>>> para = p.p("Base paragraph")
>>> para2 = para("Extra text")
>>> para2
<p>
  Base paragraph
  Extra text
</p>
>>> para
<p>
  Base paragraph
</p>

```

## Known issues

There are a couple of things I haven't gotten round to sorting out yet

* [ ] Add default attributes to more tags
* [ ] Some tags (eg `<pre>`, `<script>`) currently aren't properly implemented
      and escape their contents.

## How it works

Since there are so many HTML tags, it would be extremely tedious to document
them all manually. In the `meta` directory, you will find code that solves this
problem with the following steps:

1. Download the Markdown source for
   [MDN's documentation of all HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

2. Parse the markdown to gather all tag names and descriptions, discarding
   garbage data and obsolete tags.

3. Use data from a YAML configuration file ([`meta/tags.yml`](meta/tags.yml))
   to gather information on suggested attributes and base classes to use for
   each tag.

4. Generate Python code to represent all of these tags, including their
   documentation.

## Credits

### [Cenkalti/PyHTML](https://github.com/cenkalti/pyhtml)

Cenk Altı's work was used as a source of inspiration and reference. Although
all the code in `pyhtml-enhanced` was written by me, I want to thank them for
the significant help their hard work provided while creating this project,
going as far as to give design advice on request.

### [MDN Web Docs](https://developer.mozilla.org/en-US/)

Almost all of the documentation was gathered from the MDN Web Docs. It's super
neat that all their documentation is open (licensed as
[CC-BY-SA-2.5](https://creativecommons.org/licenses/by-sa/2.5/) if you're
interested).

### COMP1010 students and staff

COMP1010's students and staff members have uncovered and helped to resolve many
bugs, and have suggested many improvements. I'd like to thank them for all of
their help!

## License

### Source code

Copyright (c) 2023 Maddy Guthridge, COMP1010 UNSW

Source code for the library is open source, using the
[MIT license](https://choosealicense.com/licenses/mit/). A copy of the license
text is available in [LICENSE.md](https://github.com/COMP1010UNSW/pyhtml-enhanced/blob/main/LICENSE.md)

### Documentation

Documentation is copied from MDN Web Docs, and is license under
[CC-BY-SA-2.5](https://creativecommons.org/licenses/by-sa/2.5/). A copy of the
license text is available in [LICENSE_DOCS.md](https://github.com/COMP1010UNSW/pyhtml-enhanced/blob/main/LICENSE_DOCS.md)
"""
# Disable Flake8, since it really doesn't like our docstring above
# flake8: noqa
from .__tag_base import Tag, create_tag, SelfClosingTag, WhitespaceSensitiveTag

from .__tags import input_, object_

__all__ = [
    'Tag',
    'create_tag',
    'SelfClosingTag',
    'WhitespaceSensitiveTag',
    'DangerousRawHtml',
    'Comment',
    'input_',
    'object_',
    'html',
    'base',
    'head',
    'link',
    'meta',
    'style',
    'title',
    'body',
    'address',
    'article',
    'aside',
    'footer',
    'header',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'hgroup',
    'main',
    'nav',
    'section',
    'search',
    'blockquote',
    'dd',
    'div',
    'dl',
    'dt',
    'figcaption',
    'figure',
    'hr',
    'li',
    'menu',
    'ol',
    'p',
    'pre',
    'ul',
    'a',
    'abbr',
    'b',
    'bdi',
    'bdo',
    'br',
    'cite',
    'code',
    'data',
    'dfn',
    'em',
    'i',
    'kbd',
    'mark',
    'q',
    'rp',
    'rt',
    'ruby',
    's',
    'samp',
    'small',
    'span',
    'strong',
    'sub',
    'sup',
    'time',
    'u',
    'var',
    'wbr',
    'area',
    'audio',
    'img',
    'map',
    'track',
    'video',
    'embed',
    'iframe',
    'object',
    'picture',
    'portal',
    'source',
    'canvas',
    'noscript',
    'script',
    'del_',
    'ins',
    'caption',
    'col',
    'colgroup',
    'table',
    'tbody',
    'td',
    'tfoot',
    'th',
    'thead',
    'tr',
    'button',
    'datalist',
    'fieldset',
    'form',
    'input',
    'label',
    'legend',
    'meter',
    'optgroup',
    'option',
    'output',
    'progress',
    'select',
    'textarea',
    'details',
    'dialog',
    'summary',
    'slot',
    'template',
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
    iframe,
    object,
    picture,
    portal,
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
