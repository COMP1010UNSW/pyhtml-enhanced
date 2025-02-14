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
