# Advanced PyHTML

This page documents more-advanced PyHTML features, as well as strategies for
using PyHTML effectively.

## Creating components

It is often a good idea to break websites into reusable components. This allows
you to create consistent interfaces across many pages. In PyHTML, this is
easiest to do using Python functions.

Let's imagine we want to make a card to display information about a COMP1010
staff member. We could construct a component for this using the following code:

```py
import pyhtml as p

def course_staff_to_html(name, position, classes):
    """
    Given information about a COMP1010 staff member, generate some HTML.

    Args:
        name (str): name of the staff member
        position (str): role in course staff
        classes (list[str]): classes they teach
    """
    # Make HTML list of classes
    classes_html = []
    for class_taught in classes:
        classes_html.append(p.li(class_taught))

    return p.div(
        p.h2(name),
        p.p(p.i(position)),
        p.p('Classes taught:'),
        p.ul(classes_html),
    )

```

Now we can easily generate this complex component many times with a single
function call:

```py
staff_members = [
    { 'name': 'Sim', 'position': 'Lecturer', 'classes': [] },
    { 'name': 'Maddy', 'position': 'Admin', 'classes': ['M13A'] },
    { 'name': 'Ethan', 'position': 'Tutor', 'classes': ['T15A'] },
    { 'name': 'Shan', 'position': 'Tutor', 'classes': ['T12A'] },
]

staff_html = []
for person in staff_members:
    staff_html.append(course_staff_to_html(
        person['name'],
        person['position'],
        person['classes'],
    ))
```

## Rendering options

If you need more control over how PyHTML renders your output HTML, you can use
the [`p.RenderOptions`][pyhtml.RenderOptions] class to specify these.

For example, if you don't want any whitespace between your HTML components,
you can use `p.RenderOptions(spacing="")` to remove it.

```py
>>> import pyhtml as p
>>> print(str(p.div(p.RenderOptions(spacing=""))(
... p.i("No"),
... p.b("spaces"),
... p.u("here!")
... )))
<div><i>No</i><b>spaces</b><u>here!</u></div>

```

For more information about the specific allowed properties, view
[this documentation][pyhtml.RenderOptions].

## HTML comments

You can add comments to HTML by using the `Comment` tag. These will be included
in the output HTML, which can be useful for debugging your server from your web
browser.

```py
>>> import pyhtml as p
>>> comment = p.Comment("This is an HTML comment")
>>> print(str(comment))
<!--
  This is an HTML comment
-->

```

## Embedding raw HTML

By default, PyHTML [escapes certain characters](https://www.w3schools.com/html/html_entities.asp)
within strings passed to tags. This is done to prevent user content from taking
control of your webpages in what is called a
[cross-site scripting (XSS) attack](https://owasp.org/www-community/attacks/xss/).

Sometimes, you may wish to embed an existing HTML string inside of PyHTML. You
can do this using the `p.DangerousRawHtml` tag.

```py
>>> import pyhtml as p
>>> raw = p.DangerousRawHtml("<p>Scary!</p>")
>>> print(str(raw))
<p>Scary!</p>

```

***Be careful though!*** PyHTML escapes these sequences for good reason, so
don't use `DangerousRawHtml` unless you have a *very good reason*, and are
certain that the text you are passing it is trusted.

## Custom tags

Since this library includes all modern HTML tags, it is very unlikely that
you'll need to do create a custom tag. However if you really need to, you can
use the `create_tag` function.

```py
>>> import pyhtml as p
>>> fancy = p.create_tag('fancy')

```

This tag can be used like any other PyHTML tag:

```py
>>> print(fancy())
<fancy></fancy>

```

### Tag base classes

The `create_tag` function also allows you to specify a rendering strategy.

* `p.Tag`: default rendering.

* `p.SelfClosingTag`: tag is self-closing, meaning that no child elements are
  accepted.

* `p.WhitespaceSensitiveTag`: tag is whitespace-sensitive, meaning that its
  child elements are not indented.

For example, to create a self-closing tag, you can use:

```py
>>> import pyhtml as p
>>> closure = p.create_tag('closure', p.SelfClosingTag)
>>> closure()
<closure/>

```

## Advanced custom tags

Note that this is advanced functionality, which is far beyond the abilities
expected of COMP1010 students.

Custom tags can also be created by defining classes that inherit from `p.Tag`.
For example, the `<fancy>` tag from above can be defined as:

```py
import pyhtml as p

class fancy(p.Tag):
    pass
```

For documentation on the attributes and methods of `Tag`, see the
[API documentation](../api.md).
