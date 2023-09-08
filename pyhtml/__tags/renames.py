"""
# PyHTML Enhanced / Tags / Renamed

Some tags from the original PyHTML are named with a trailing underscore (eg
`input_` instead of `input`). This is unnecessary in modern versions of Python,
but for the sake of being (somewhat) compatible with the original PyHTML,
we still export the originals.
"""
from .generated import (  # type: ignore
    object as object_,
    input as input_,
)

__all__ = [
    'object_',
    'input_',
]
