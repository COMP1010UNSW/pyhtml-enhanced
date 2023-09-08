"""
# Tests / Code gen test

Tests for code generation

These don't regenerate the code, but rather test code that has been generated
"""
import pytest
import pyhtml
from pyhtml import Tag, Comment


all_tags = [
    getattr(pyhtml, i)
    for i in dir(pyhtml)
    if (
        # Ignore __dunder__ items
        not i.startswith('__')
        # Only look at classes
        and type(getattr(pyhtml, i)) == type
        # That are a kind of Tag
        and issubclass(getattr(pyhtml, i), Tag)
        # And aren't a comment (since comments require named args)
        and not issubclass(getattr(pyhtml, i), Comment)
    )
]


def test_num_exported_members():
    """
    We don't want regenerating the code to produce any more (or fewer) members
    """
    # Just update the number if you're expecting it to change
    assert len(all_tags) == 116


@pytest.mark.parametrize(
    'tag',
    all_tags
)
def test_tag_renders(tag: type[Tag]):
    """
    Test that each tag correctly renders
    """
    assert str(tag()) == f"<{tag()._get_tag_name()}/>"


@pytest.mark.parametrize(
    'tag',
    all_tags
)
def test_tag_callable(tag: type[Tag]):
    """
    Test that each tag correctly renders after calling itself
    """
    assert str(tag()()) == f"<{tag()._get_tag_name()}/>"
