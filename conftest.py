"""
# conftest.py

Global pytest configuration. We need to skip doctests on Python versions < 3.14
as the documentation uses new Python syntax.
"""

import sys
from pathlib import Path


def pytest_ignore_collect(collection_path: Path):
    if str(collection_path).endswith(".md") and sys.version_info < (
        3,
        14,
    ):  # pragma: no cover
        return True
