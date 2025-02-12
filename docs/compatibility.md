# Compatibility with PyHTML

There are some minor usage differences compared to the original PyHTML library.

## Rendering of uninstantiated classes

Uninstantiated classes are only rendered if they are given as the child of an
instantiated element.

```py
>>> import pyhtml as p
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

## Calling tag instances

Calling an instance of a `Tag` will return a new tag containing all elements of
the original tag combined with the new attributes and children, but will not
modify the original instance, as I found the old behaviour confusing and
bug-prone.

```py
>>> span1 = p.span("Base paragraph")
>>> span2 = span1("Extra text")
>>> span2
<span>
  Base paragraph
  Extra text
</span>
>>> span1
<span>
  Base paragraph
</span>

```

## Spacing between tag instances

Certain tags have default spacing, which helps to avoid subtle rendering
annoyances such as unwanted spaces between linked text and punctuation in
paragraphs.

```py
>>> print(str(p.p(p.a(href="https://example.com")("Example website"), "!")))
<p><a href="https://example.com">Example website</a>!</p>
>>> # Notice how there is no spacing between the link and the exclamation point

```
