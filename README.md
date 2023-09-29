# PyHTML Enhanced

A library for building HTML documents with a simple and learnable syntax,
inspired by, and similar to
[the original PyHTML library](https://github.com/cenkalti/pyhtml), but with
improved documentation and type safety.

## Features

* Inline documentation and type safety for all tags. Documentation for tags
  is pulled from MDN Web Docs.

* A modern and readable codebase.

* No dependencies.

* 100% test coverage

## Usage

```py
import pyhtml as h

my_website = h.html(
    h.head(
        h.title("Hello, world!"),
        h.script(src="http://example.com/script.js"),
    ),
    h.body(
        h.h1("Hello, world!"),
        h.p("This is my amazing website rendered with PyHTML Enhanced!"),
    ),
)

# Converting it to a string is all you need to do to render it!
print(str(my_website))
```

This will produce the following HTML code:

```html
<html>
  <head>
    <title>
      Hello, world!
    </title>
    <script src="http://example.com/script.js" type="text/javascript"></script>
  </head>
  <body>
    <h1>
      Hello, world!
    </h1>
    <p>
      This is my amazing website rendered with PyHTML Enhanced!
    </p>
  </body>
</html>
```

## Differences to PyHTML

There are some minor usage differences compared to the original PyHTML library.

Uninstantiated classes are only rendered if they are given as the child of an
instantiated element.

```py
>>> br
<class 'pyhtml.__tags.generated.br'>
>>> html(body(br))
<html>
  <body>
    <br>
  </body>
</html>
```

Calling an instance of a `Tag` will return a new tag containing all elements of
the original tag combined with the new attributes and children, but will not
modify the original instance, as I found the old behaviour confusing and
bug-prone.

```py
>>> para = p("Base paragraph")
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
the significant help their hard work provided while creating this project.

### [MDN Web Docs](https://developer.mozilla.org/en-US/)

Almost all of the documentation was gathered from the MDN Web Docs. It's super
neat that all their documentation is open (licensed as
[CC-BY-SA-2.5](https://creativecommons.org/licenses/by-sa/2.5/) if you're
interested).

## License

All code in this project is licensed under the [MIT License](./LICENSE.md).

However, the documentation found in
[`pyhtml/__tags/generated.py`](./pyhtml/__tags/generated.py) was copied from
MDN Web Docs, and is licensed under
[CC-BY-SA-2.5](https://creativecommons.org/licenses/by-sa/2.5/). See
[LICENSE_DOCS.md](./LICENSE_DOCS.md) for a copy of the license.
