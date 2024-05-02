"""
# PyHTML Enhanced /  Tags / Dangerous raw HTML

Definition for the DangerousRawHtml tag.
"""
from ..__tag_base import Tag
from ..__util import increase_indent


class DangerousRawHtml(Tag):
    """
    Raw HTML as a string. This is embedded directly within the rendered output.

    ## Warning

    This will blindly accept any text as HTML, which is EXTREMELY DANGEROUS!
    (Mis)using this could result in issues ranging from broken output to major
    security vulnerabilities such as
    [cross-site scripting](https://en.wikipedia.org/wiki/XSS).

    Do not use this unless absolutely necessary.
    """
    def __init__(self, text: str) -> None:
        """
        Raw HTML as a string. This is embedded directly within the rendered
        output.

        ## Warning

        This will blindly accept any text as HTML, which is EXTREMELY
        DANGEROUS! (Mis)using this could result in issues ranging from broken
        output to major security vulnerabilities such as
        [cross-site scripting](https://en.wikipedia.org/wiki/XSS).

        Do not use this unless absolutely necessary.
        """
        self.html_data = text
        super().__init__()

    def __call__(self):
        raise TypeError('DangerousRawHtml tags are not callable')

    def _get_tag_name(self) -> str:
        # Ignore coverage since this is only implemented to satisfy inheritance
        # and is never used since we override _render
        return '!!!DANGEROUS RAW HTML!!!'  # pragma: no cover

    def _render(self, indent: int) -> list[str]:
        return increase_indent(self.html_data.splitlines(), indent)
