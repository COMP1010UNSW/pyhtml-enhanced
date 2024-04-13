"""
# Tests / Raw HTML Test

Test cases for `DangerousRawHtml` tag
"""
import pytest
from pyhtml import DangerousRawHtml, html


def test_dangerous_raw_html():
    """
    Is raw HTML rendered correctly?
    """
    assert str(DangerousRawHtml("<script>alert(1)</script>")) \
        == "<script>alert(1)</script>"

    assert str(
        html(
            DangerousRawHtml("<script>alert(1)</script>")
        )
    ) == "\n".join([
        "<html>",
        "  <script>alert(1)</script>",
        "</html>",
    ])


def test_raw_html_not_callable():
    """
    `DangerousRawHtml` elements should not be callable.
    """
    with pytest.raises(TypeError):
        DangerousRawHtml("")()
