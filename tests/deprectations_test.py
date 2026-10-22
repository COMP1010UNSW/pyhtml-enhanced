"""
# Tests / Deprecations test

Tests for deprecated tags and features.
"""

import pytest

import pyhtml as p

deprecated_tags = [p.fencedframe]


@pytest.mark.parametrize("tag", deprecated_tags)
def test_produces_deprecation_warning(tag: p.Tag):
    with pytest.deprecated_call():
        tag()
