# How it works

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

## Code generation

See the `meta` directory in the code.

## Rendering

See the `render` function of the `Tag` class.
