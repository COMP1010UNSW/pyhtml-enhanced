"""
# Tests / input tag test

The <input> tag has some special properties that should be tested
"""
from pyhtml import input


def test_submit_no_formaction():
    """
    Rendering an <input> with no `formaction` attribute means no `formmethod`
    is specified.
    """
    assert 'formmethod' not in str(input(type='submit'))


def test_submit_with_formaction():
    """
    Rendering an <input> with a `formaction` attribute means that the
    `formmethod` is specified to be `"POST"`.
    """
    assert 'formmethod="POST"' in str(input(type='submit', formaction='/'))


def test_submit_with_formmethod():
    """
    Rendering an input with a `formaction` and a `formmethod` uses the given
    `formmethod`, rather than `"POST"`.
    """
    assert 'formmethod="GET"' \
        in str(input(type='submit', formaction='/', formmethod='GET'))
