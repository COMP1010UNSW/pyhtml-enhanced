# PyHTML cheatsheet

## Importing PyHTML

```py
import pyhtml as p
```

## Basic formatting

| Description | PyHTML | HTML Produced | Displayed as |
|-------------|--------|---------------|--------------|
| Paragraph | `p.p('This is a paragraph')` | `<p>This is a paragraph</p>` | This is a paragraph |
| Heading | `p.h1('Heading')` | `<h1>Heading</h1>` | <h1>Heading</h1> |
| Bold text | `p.b('Be bold!')` | `<b>Be bold!</b>` | **Be bold!** |

Other elements can be used too.
[Here's a list of all of them](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

## Tag attributes

Tag attributes are defined using Python keyword arguments. By convention, these
are added by using multiple function calls:

```py
p.element_name(
    # Add attributes
)(
    # Add child elements
)
```

### Hyperlinks

```py
# `a` is short for "anchor"
p.a(href="https://github.com/COMP1010UNSW/pyhtml-enhanced")("Take a look at the PyHTML code")
```

### Images

```py
p.img(
    alt="An image of a duck",
    src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Bucephala-albeola-010.jpg",
)
```

Make sure your images always have [alt text](https://webaim.org/techniques/alttext/#breadcrumbs),
so that they are accessible to users with vision impairments.

## Lists

You can use the `ol` element to create an ordered list (`1`, `2`, `3`, ...),
and the `ul` element to create an unordered list (`*`, `*`, `*`, ...).

### Static list (contents don't change)

```py
p.ol(
    p.li('Python'),
    p.li('HTML'),
    p.li('CSS'),
)
```

### Dynamic list (contents change)

Imagine we have a list of strings.

```py
my_favourite_games = [
    'Celeste',
    'The Legend of Zelda: Tears of the Kingdom',
    'Windows 98 Pinball',
]
```

The contents of this list may change over time (eg if I discover a new game),
therefore we can't hard-code the PyHTML. Instead, we can use a for loop to
generate each element one by one, before adding the entire list to an HTML
list.

```py
list_items = []
for game in my_favourite_games:
    list_items.append(p.li(game))

overall_list = p.ul(list_items)
```

This strategy works regardless of how long the list is, making it very
flexible.

It is often a good idea to use helper functions to keep your code simple and
organised:

```py
def string_list_to_html(items):
    html_items = []
    for item in items:
        html_items.append(p.li(item))

    return p.ul(html_items)
```

Similar techniques can be applied to other types of repeated data, such as
"drop-down menus" (`p.select` containing `p.option` elements), and tables
(`p.table` containing `p.tr` elements, each containing `p.td` elements).
