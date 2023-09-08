"""
# Meta

Code for building the tag definitions
"""
__all__ = ['generate_tag_data', 'build_tags']

from .scrape_tags import main as generate_tag_data
from .generate_tag_defs import main as build_tags
