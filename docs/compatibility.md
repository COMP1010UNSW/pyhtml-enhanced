# Compatibility with PyHTML

There are some minor usage differences compared to the original PyHTML library.

## Rendering of uninstantiated classes

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

## Calling tag instances

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
