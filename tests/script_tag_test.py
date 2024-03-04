"""
# Tests / script tag test

Test cases for the script tag
"""
from pyhtml import script


def test_script_not_escaped():
    """
    Contents of script are not escaped.
    """
    assert str(script("<>'\";&")) == "\n".join([
        "<script type=\"text/javascript\">",
        "  <>'\";&",
        "</script>",
    ])
