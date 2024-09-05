# `<PyHTML/>`

Build HTML documents in Python with a simple and learnable syntax.

## Usage

* [Learn PyHTML](./learn/index.md)
* [View the cheatsheet](./learn/cheatsheet.md)

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
