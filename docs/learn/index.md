# Learn PyHTML

This page contains the basic information on how to use PyHTML. In order to
properly understand this, it will help to understand the
[basics of HTML](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics).

## Overview

You can think of PyHTML as a collection of functions that you can use to
generate a website. After you finish creating your PyHTML object, you render it
by passing it to the Python `str` function.

## Importing PyHTML

This the standard way to import the PyHTML library:

```py
>>> import pyhtml as p

```

All of the PyHTML tags can then be accessed within an object named `p`.

## Creating elements

Every HTML tag is represented by a `class` that generates that HTML code. For
example, to create a `<br>` element, you could use:

```py
>>> line_break = p.br()
>>> print(str(line_break))
<br/>

```

Any [standard HTML tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
can be used within PyHTML.

## Adding children to elements

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

## Adding attributes to elements

Any keyword arguments to a tag are used as an attribute of the created HTML
element. For example, to create a form submit button, you could use

```py
>>> submit_button = p.input(type="submit")
>>> print(str(submit_button))
<input type="submit"/>

```

## Adding attributes and children

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

## Rendering HTML

Converting your PyHTML into HTML is as simple as stringifying it!

```py
>>> print(str(p.i("How straightforward!")))
<i>
  How straightforward!
</i>

```

## Where to from here?

* Learn about [advanced PyHTML usage](./advanced.md).
* Check out [the PyHTML cheatsheet](./cheatsheet.md).
