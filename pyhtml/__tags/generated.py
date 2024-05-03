"""
# PyHTML Enhanced / Tags / Generated

Tags generated using documentation from MDN. See code in meta/ in the repo.

Note that all documentation is licensed as CC-BY-SA-2.5

https://creativecommons.org/licenses/by-sa/2.5/
"""
from typing import Any, Optional, Union, Literal
from ..__tag_base import Tag, SelfClosingTag, WhitespaceSensitiveTag
from ..__types import AttributeType, ChildrenType

class html(Tag):
    """
    Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

    * `lang`: Language used by the document

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
    """
    def __init__(
        self,
        *children: ChildrenType,
        lang: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        * `lang`: Language used by the document

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        attributes |= {
            'lang': lang,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        lang: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        * `lang`: Language used by the document

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        attributes |= {
            'lang': lang,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'lang': None}


    def _get_tag_pre_content(self) -> Optional[str]:
        return '<!DOCTYPE html>'


class base(SelfClosingTag):
    """
    Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

    * `href`: Base URL to use in the document
    * `target`: Default target to use in the document

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
    """
    def __init__(
        self,
        *,
        href: AttributeType = None,
        target: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

        * `href`: Base URL to use in the document
        * `target`: Default target to use in the document

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
        """
        attributes |= {
            'href': href,
            'target': target,
        }
        super().__init__(**attributes)

    def __call__(  # type: ignore
        self,
        *,
        href: AttributeType = None,
        target: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

        * `href`: Base URL to use in the document
        * `target`: Default target to use in the document

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
        """
        attributes |= {
            'href': href,
            'target': target,
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'href': None, 'target': None}


class head(Tag):
    """
    Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class link(SelfClosingTag):
    """
    Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

    * `href`: Location of the file being linked to
    * `rel`: Kind of file being loaded (eg `"stylesheet"`)

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
    """
    def __init__(
        self,
        *,
        href: Optional[str] = None,
        rel: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

        * `href`: Location of the file being linked to
        * `rel`: Kind of file being loaded (eg `"stylesheet"`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
        """
        attributes |= {
            'href': href,
            'rel': rel,
        }
        super().__init__(**attributes)

    def __call__(  # type: ignore
        self,
        *,
        href: Optional[str] = None,
        rel: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

        * `href`: Location of the file being linked to
        * `rel`: Kind of file being loaded (eg `"stylesheet"`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
        """
        attributes |= {
            'href': href,
            'rel': rel,
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'href': None, 'rel': None}


class meta(Tag):
    """
    Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [<base>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [<link>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [<script>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [<style>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [<title>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [<base>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [<link>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [<script>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [<style>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [<title>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [<base>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [<link>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [<script>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [<style>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [<title>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class style(Tag):
    """
    Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

    * `type`: Type of style to use (defaults to `'text/css'`)

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
    """
    def __init__(
        self,
        *children: ChildrenType,
        type: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

        * `type`: Type of style to use (defaults to `'text/css'`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
        """
        attributes |= {
            'type': type,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        type: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

        * `type`: Type of style to use (defaults to `'text/css'`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
        """
        attributes |= {
            'type': type,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'type': 'text/css'}


    def _escape_children(self) -> bool:
        return False


class title(Tag):
    """
    Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class body(Tag):
    """
    represents the content of an HTML document. There can be only one such element in a document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        represents the content of an HTML document. There can be only one such element in a document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        represents the content of an HTML document. There can be only one such element in a document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class address(Tag):
    """
    Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class article(Tag):
    """
    Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class aside(Tag):
    """
    Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class footer(Tag):
    """
    Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class header(Tag):
    """
    Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h1(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h2(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h3(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h4(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h5(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class h6(Tag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class hgroup(Tag):
    """
    Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class main(Tag):
    """
    Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class nav(Tag):
    """
    Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class section(Tag):
    """
    Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class search(Tag):
    """
    Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class blockquote(Tag):
    """
    Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [<cite>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [<cite>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [<cite>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class dd(Tag):
    """
    Provides the description, definition, or value for the preceding term ([<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Provides the description, definition, or value for the preceding term ([<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Provides the description, definition, or value for the preceding term ([<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class div(Tag):
    """
    The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class dl(Tag):
    """
    Represents a description list. The element encloses a list of groups of terms (specified using the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class dt(Tag):
    """
    Specifies a term in a description or definition list, and as such must be used inside a [<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies a term in a description or definition list, and as such must be used inside a [<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies a term in a description or definition list, and as such must be used inside a [<dl>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class figcaption(Tag):
    """
    Represents a caption or legend describing the rest of the contents of its parent [<figure>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a caption or legend describing the rest of the contents of its parent [<figure>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a caption or legend describing the rest of the contents of its parent [<figure>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class figure(Tag):
    """
    Represents self-contained content, potentially with an optional caption, which is specified using the [<figcaption>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [<figcaption>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [<figcaption>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class hr(Tag):
    """
    Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class li(Tag):
    """
    Represents an item in a list. It must be contained in a parent element: an ordered list ([<ol>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([<menu>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([<ol>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([<menu>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([<ol>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([<menu>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class menu(Tag):
    """
    A semantic alternative to [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [<li>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        A semantic alternative to [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [<li>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        A semantic alternative to [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [<ul>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [<li>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class ol(Tag):
    """
    Represents an ordered list of items — typically rendered as a numbered list.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class p(Tag):
    """
    Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class pre(WhitespaceSensitiveTag):
    """
    Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class ul(Tag):
    """
    Represents an unordered list of items, typically rendered as a bulleted list.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class a(Tag):
    """
    Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

    * `href`: URL of page to link to
    * `target`: Use "_blank" to open in a new tab

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
    """
    def __init__(
        self,
        *children: ChildrenType,
        href: Optional[str] = None,
        target: Union[Literal['_self', '_blank', '_parent', '_top'], str, None] = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

        * `href`: URL of page to link to
        * `target`: Use "_blank" to open in a new tab

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'href': href,
            'target': target,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        href: Optional[str] = None,
        target: Union[Literal['_self', '_blank', '_parent', '_top'], str, None] = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

        * `href`: URL of page to link to
        * `target`: Use "_blank" to open in a new tab

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'href': href,
            'target': target,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'href': None, 'target': None}


class abbr(Tag):
    """
    Represents an abbreviation or acronym.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents an abbreviation or acronym.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents an abbreviation or acronym.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class b(Tag):
    """
    Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class bdi(Tag):
    """
    Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class bdo(Tag):
    """
    Overrides the current directionality of text, so that the text within is rendered in a different direction.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class br(SelfClosingTag):
    """
    Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
    """
    def __init__(
        self,
        
        
        **attributes: AttributeType,
    ) -> None:
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        attributes |= {
            
        }
        super().__init__(**attributes)

    def __call__(  # type: ignore
        self,
        
        
        **attributes: AttributeType,
    ):
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        attributes |= {
            
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class cite(Tag):
    """
    Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class code(Tag):
    """
    Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class data(Tag):
    """
    Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class dfn(Tag):
    """
    Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [<p>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [<p>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [<p>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [<dt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[<dd>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class em(Tag):
    """
    Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class i(Tag):
    """
    Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class kbd(Tag):
    """
    Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class mark(Tag):
    """
    Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class q(Tag):
    """
    Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [<blockquote>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [<blockquote>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [<blockquote>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class rp(Tag):
    """
    Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [<rt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [<rt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [<rt>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class rt(Tag):
    """
    Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [<ruby>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class ruby(Tag):
    """
    Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class s(Tag):
    """
    Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the [<del>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del) and [<ins>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins) elements, as appropriate.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the [<del>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del) and [<ins>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins) elements, as appropriate.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the [<del>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del) and [<ins>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins) elements, as appropriate.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class samp(Tag):
    """
    Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class small(Tag):
    """
    Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class span(Tag):
    """
    A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class strong(Tag):
    """
    Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class sub(Tag):
    """
    Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class sup(Tag):
    """
    Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class time(Tag):
    """
    Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class u(Tag):
    """
    Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class var(Tag):
    """
    Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class wbr(Tag):
    """
    Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class area(Tag):
    """
    Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class audio(Tag):
    """
    Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class img(Tag):
    """
    Embeds an image into the document.

    * `src`: Source URL of the image.
    * `alt`: Alt text for the image.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
    """
    def __init__(
        self,
        *children: ChildrenType,
        src: AttributeType = None,
        alt: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Embeds an image into the document.

        * `src`: Source URL of the image.
        * `alt`: Alt text for the image.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        attributes |= {
            'src': src,
            'alt': alt,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        src: AttributeType = None,
        alt: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Embeds an image into the document.

        * `src`: Source URL of the image.
        * `alt`: Alt text for the image.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        attributes |= {
            'src': src,
            'alt': alt,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'src': None, 'alt': None}


class map(Tag):
    """
    Used with [<area>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used with [<area>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used with [<area>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class track(Tag):
    """
    Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class video(Tag):
    """
    Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class embed(Tag):
    """
    Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class iframe(Tag):
    """
    Represents a nested browsing context, embedding another HTML page into the current one.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class object(Tag):
    """
    Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class picture(Tag):
    """
    Contains zero or more [<source>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [<img>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Contains zero or more [<source>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [<img>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Contains zero or more [<source>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [<img>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class portal(Tag):
    """
    Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class source(Tag):
    """
    Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class canvas(Tag):
    """
    Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class noscript(Tag):
    """
    Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class script(Tag):
    """
    Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

    * `type`: Type of script to use (defaults to `'text/javascript'`)
    * `src`: The location from which to load the script. If present, this will be used rather than the contents of the element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
    """
    def __init__(
        self,
        *children: ChildrenType,
        type: Optional[str] = None,
        src: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        * `type`: Type of script to use (defaults to `'text/javascript'`)
        * `src`: The location from which to load the script. If present, this will be used rather than the contents of the element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        attributes |= {
            'type': type,
            'src': src,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        type: Optional[str] = None,
        src: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        * `type`: Type of script to use (defaults to `'text/javascript'`)
        * `src`: The location from which to load the script. If present, this will be used rather than the contents of the element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        attributes |= {
            'type': type,
            'src': src,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'type': 'text/javascript', 'src': None}


    def _escape_children(self) -> bool:
        return False


class del_(Tag):
    """
    Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class ins(Tag):
    """
    Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class caption(Tag):
    """
    Specifies the caption (or title) of a table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies the caption (or title) of a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies the caption (or title) of a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class col(Tag):
    """
    Defines one or more columns in a column group represented by its implicit or explicit parent [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element. The `<col>` element is only valid as a child of a [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element that has no [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup#span) attribute defined.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines one or more columns in a column group represented by its implicit or explicit parent [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element. The `<col>` element is only valid as a child of a [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element that has no [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup#span) attribute defined.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines one or more columns in a column group represented by its implicit or explicit parent [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element. The `<col>` element is only valid as a child of a [<colgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element that has no [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup#span) attribute defined.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class colgroup(Tag):
    """
    Defines a group of columns within a table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines a group of columns within a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines a group of columns within a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class table(Tag):
    """
    Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Represents tabular data—that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class tbody(Tag):
    """
    Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of a table's (main) data.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of a table's (main) data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of a table's (main) data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class td(Tag):
    """
    A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell of a table that contains data.

    * `colspan`: The number of columns in the table that this cell spans.
    * `rowspan`: The number of rows in the table that this cell spans.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
    """
    def __init__(
        self,
        *children: ChildrenType,
        colspan: AttributeType = None,
        rowspan: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell of a table that contains data.

        * `colspan`: The number of columns in the table that this cell spans.
        * `rowspan`: The number of rows in the table that this cell spans.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'colspan': colspan,
            'rowspan': rowspan,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        colspan: AttributeType = None,
        rowspan: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell of a table that contains data.

        * `colspan`: The number of columns in the table that this cell spans.
        * `rowspan`: The number of rows in the table that this cell spans.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'colspan': colspan,
            'rowspan': rowspan,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'colspan': None, 'rowspan': None}


class tfoot(Tag):
    """
    Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the foot of a table with information about the table's columns. This is usually a summary of the columns, e.g., a sum of the given numbers in a column.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class th(Tag):
    """
    A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#scope) and [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#headers) attributes.

    * `scope`: The area of the table that this heading applies to. Allowed values: `"col"`, `"row"`, `"colgroup"`, `"rowgroup"`
    * `colspan`: The number of columns in the table that this heading spans.
    * `rowspan`: The number of rows in the table that this heading spans.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
    """
    def __init__(
        self,
        *children: ChildrenType,
        scope: Optional[Literal['col', 'row', 'colgroup', 'rowgroup']] = None,
        colspan: AttributeType = None,
        rowspan: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#scope) and [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#headers) attributes.

        * `scope`: The area of the table that this heading applies to. Allowed values: `"col"`, `"row"`, `"colgroup"`, `"rowgroup"`
        * `colspan`: The number of columns in the table that this heading spans.
        * `rowspan`: The number of rows in the table that this heading spans.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'scope': scope,
            'colspan': colspan,
            'rowspan': rowspan,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        scope: Optional[Literal['col', 'row', 'colgroup', 'rowgroup']] = None,
        colspan: AttributeType = None,
        rowspan: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        A child of the [<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) element, it defines a cell as the header of a group of table cells. The nature of this group can be explicitly defined by the [`scope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#scope) and [`headers`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th#headers) attributes.

        * `scope`: The area of the table that this heading applies to. Allowed values: `"col"`, `"row"`, `"colgroup"`, `"rowgroup"`
        * `colspan`: The number of columns in the table that this heading spans.
        * `rowspan`: The number of rows in the table that this heading spans.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'scope': scope,
            'colspan': colspan,
            'rowspan': rowspan,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'scope': None, 'colspan': None, 'rowspan': None}


class thead(Tag):
    """
    Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers ([<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) elements).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers ([<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Encapsulates a set of table rows ([<tr>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the head of a table with information about the table's columns. This is usually in the form of column headers ([<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class tr(Tag):
    """
    Defines a row of cells in a table. The row's cells can then be established using a mix of [<td>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [<td>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [<td>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [<th>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class button(Tag):
    """
    An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

    * `formmethod`: The HTTP request method to use on click. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
    * `formaction`: The URL to request to on click. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
    """
    def __init__(
        self,
        *children: ChildrenType,
        formmethod: AttributeType = None,
        formaction: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

        * `formmethod`: The HTTP request method to use on click. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        formmethod: AttributeType = None,
        formaction: AttributeType = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

        * `formmethod`: The HTTP request method to use on click. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'formmethod': None, 'formaction': None}


class datalist(Tag):
    """
    Contains a set of [<option>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Contains a set of [<option>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Contains a set of [<option>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class fieldset(Tag):
    """
    Used to group several controls as well as labels ([<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Used to group several controls as well as labels ([<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Used to group several controls as well as labels ([<label>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class form(Tag):
    """
    Represents a document section containing interactive controls for submitting information.

    * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'post'`)
    * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
    """
    def __init__(
        self,
        *children: ChildrenType,
        method: Optional[Literal['post', 'get']] = None,
        action: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a document section containing interactive controls for submitting information.

        * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'post'`)
        * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        attributes |= {
            'method': method,
            'action': action,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        method: Optional[Literal['post', 'get']] = None,
        action: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Represents a document section containing interactive controls for submitting information.

        * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'post'`)
        * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        attributes |= {
            'method': method,
            'action': action,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'method': 'post', 'action': None}


class label(Tag):
    """
    Represents a caption for an item in a user interface.

    * `for_`: ID of input field to associate this label with

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
    """
    def __init__(
        self,
        *children: ChildrenType,
        for_: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a caption for an item in a user interface.

        * `for_`: ID of input field to associate this label with

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
        """
        attributes |= {
            'for_': for_,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        for_: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Represents a caption for an item in a user interface.

        * `for_`: ID of input field to associate this label with

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
        """
        attributes |= {
            'for_': for_,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'for_': None}


class legend(Tag):
    """
    Represents a caption for the content of its parent [<fieldset>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a caption for the content of its parent [<fieldset>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a caption for the content of its parent [<fieldset>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class meter(Tag):
    """
    Represents either a scalar value within a known range or a fractional value.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents either a scalar value within a known range or a fractional value.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents either a scalar value within a known range or a fractional value.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class optgroup(Tag):
    """
    Creates a grouping of options within a [<select>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Creates a grouping of options within a [<select>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Creates a grouping of options within a [<select>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class option(Tag):
    """
    Used to define an item contained in a select, an [<optgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [<datalist>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

    * `selected`: Whether this option is the default selection within the `select` element
    * `disabled`: Whether this option is disabled, meaning it cannot be selected.
    * `value`: The value to use if this option is selected when submitting the form

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
    """
    def __init__(
        self,
        *children: ChildrenType,
        selected: Optional[bool] = None,
        disabled: Optional[bool] = None,
        value: AttributeType = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Used to define an item contained in a select, an [<optgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [<datalist>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        * `selected`: Whether this option is the default selection within the `select` element
        * `disabled`: Whether this option is disabled, meaning it cannot be selected.
        * `value`: The value to use if this option is selected when submitting the form

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        attributes |= {
            'selected': selected,
            'disabled': disabled,
            'value': value,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        selected: Optional[bool] = None,
        disabled: Optional[bool] = None,
        value: AttributeType = None,
        **attributes: AttributeType,
    ):
        """
        Used to define an item contained in a select, an [<optgroup>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [<datalist>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        * `selected`: Whether this option is the default selection within the `select` element
        * `disabled`: Whether this option is disabled, meaning it cannot be selected.
        * `value`: The value to use if this option is selected when submitting the form

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        attributes |= {
            'selected': selected,
            'disabled': disabled,
            'value': value,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'selected': None, 'disabled': None, 'value': None}


class output(Tag):
    """
    Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class progress(Tag):
    """
    Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class select(Tag):
    """
    Represents a control that provides a menu of options.

    * `required`: Whether the input is required to submit the form it is contained within.
    * `name`: The name to use for this value when submitting the form.
    * `disabled`: Whether this form element is disabled, meaning it cannot be selected, and will not be submitted with the form.
    * `multiple`: Whether multiple options can be simultaneously selected.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
    """
    def __init__(
        self,
        *children: ChildrenType,
        required: Optional[bool] = None,
        name: AttributeType = None,
        disabled: Optional[bool] = None,
        multiple: Optional[bool] = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a control that provides a menu of options.

        * `required`: Whether the input is required to submit the form it is contained within.
        * `name`: The name to use for this value when submitting the form.
        * `disabled`: Whether this form element is disabled, meaning it cannot be selected, and will not be submitted with the form.
        * `multiple`: Whether multiple options can be simultaneously selected.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'required': required,
            'name': name,
            'disabled': disabled,
            'multiple': multiple,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        required: Optional[bool] = None,
        name: AttributeType = None,
        disabled: Optional[bool] = None,
        multiple: Optional[bool] = None,
        id: Optional[str] = None,
        _class: Optional[str] = None,
        style: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Represents a control that provides a menu of options.

        * `required`: Whether the input is required to submit the form it is contained within.
        * `name`: The name to use for this value when submitting the form.
        * `disabled`: Whether this form element is disabled, meaning it cannot be selected, and will not be submitted with the form.
        * `multiple`: Whether multiple options can be simultaneously selected.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            'required': required,
            'name': name,
            'disabled': disabled,
            'multiple': multiple,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'required': None, 'name': None, 'disabled': None, 'multiple': None}


class textarea(WhitespaceSensitiveTag):
    """
    Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

    * `required`: Whether the input is required to submit the form it is contained within.
    * `name`: The name to use for this value when submitting the form.
    * `rows`: The number of rows (lines) to use in the text area. Value should be an integer, but given as type `str`.
    * `cols`: The number of columns (length of each line) to use in the text area. Value should be an integer, but given as type `str`.
    * `placeholder`: Placeholder text to use when the field is empty.
    * `disabled`: Whether this option is disabled, meaning it cannot be selected, and will not be submitted with the form.
    * `maxlength`: The maximum number of characters permitted in the textarea
    * `wrap`: How to perform word wrapping ("hard" or "soft")
    * `readonly`: Whether this option is read-only, meaning it cannot be modified

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
    """
    def __init__(
        self,
        *children: ChildrenType,
        required: Optional[bool] = None,
        name: AttributeType = None,
        rows: Optional[str] = None,
        cols: Optional[str] = None,
        placeholder: AttributeType = None,
        disabled: Optional[bool] = None,
        maxlength: AttributeType = None,
        wrap: Union[Literal['hard', 'soft'], None] = None,
        readonly: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        * `required`: Whether the input is required to submit the form it is contained within.
        * `name`: The name to use for this value when submitting the form.
        * `rows`: The number of rows (lines) to use in the text area. Value should be an integer, but given as type `str`.
        * `cols`: The number of columns (length of each line) to use in the text area. Value should be an integer, but given as type `str`.
        * `placeholder`: Placeholder text to use when the field is empty.
        * `disabled`: Whether this option is disabled, meaning it cannot be selected, and will not be submitted with the form.
        * `maxlength`: The maximum number of characters permitted in the textarea
        * `wrap`: How to perform word wrapping ("hard" or "soft")
        * `readonly`: Whether this option is read-only, meaning it cannot be modified

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        attributes |= {
            'required': required,
            'name': name,
            'rows': rows,
            'cols': cols,
            'placeholder': placeholder,
            'disabled': disabled,
            'maxlength': maxlength,
            'wrap': wrap,
            'readonly': readonly,
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        required: Optional[bool] = None,
        name: AttributeType = None,
        rows: Optional[str] = None,
        cols: Optional[str] = None,
        placeholder: AttributeType = None,
        disabled: Optional[bool] = None,
        maxlength: AttributeType = None,
        wrap: Union[Literal['hard', 'soft'], None] = None,
        readonly: Optional[bool] = None,
        **attributes: AttributeType,
    ):
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        * `required`: Whether the input is required to submit the form it is contained within.
        * `name`: The name to use for this value when submitting the form.
        * `rows`: The number of rows (lines) to use in the text area. Value should be an integer, but given as type `str`.
        * `cols`: The number of columns (length of each line) to use in the text area. Value should be an integer, but given as type `str`.
        * `placeholder`: Placeholder text to use when the field is empty.
        * `disabled`: Whether this option is disabled, meaning it cannot be selected, and will not be submitted with the form.
        * `maxlength`: The maximum number of characters permitted in the textarea
        * `wrap`: How to perform word wrapping ("hard" or "soft")
        * `readonly`: Whether this option is read-only, meaning it cannot be modified

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        attributes |= {
            'required': required,
            'name': name,
            'rows': rows,
            'cols': cols,
            'placeholder': placeholder,
            'disabled': disabled,
            'maxlength': maxlength,
            'wrap': wrap,
            'readonly': readonly,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {'required': None, 'name': None, 'rows': None, 'cols': None, 'placeholder': None, 'disabled': None, 'maxlength': None, 'wrap': None, 'readonly': None}


class details(Tag):
    """
    Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [<summary>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [<summary>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [<summary>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class dialog(Tag):
    """
    Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class summary(Tag):
    """
    Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [<details>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [<details>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [<details>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class slot(Tag):
    """
    Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


class template(Tag):
    """
    A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
    """
    def __init__(
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ) -> None:
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        
        **attributes: AttributeType,
    ):
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {}


__all__ = [
    'html',
    'base',
    'head',
    'link',
    'meta',
    'style',
    'title',
    'body',
    'address',
    'article',
    'aside',
    'footer',
    'header',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'hgroup',
    'main',
    'nav',
    'section',
    'search',
    'blockquote',
    'dd',
    'div',
    'dl',
    'dt',
    'figcaption',
    'figure',
    'hr',
    'li',
    'menu',
    'ol',
    'p',
    'pre',
    'ul',
    'a',
    'abbr',
    'b',
    'bdi',
    'bdo',
    'br',
    'cite',
    'code',
    'data',
    'dfn',
    'em',
    'i',
    'kbd',
    'mark',
    'q',
    'rp',
    'rt',
    'ruby',
    's',
    'samp',
    'small',
    'span',
    'strong',
    'sub',
    'sup',
    'time',
    'u',
    'var',
    'wbr',
    'area',
    'audio',
    'img',
    'map',
    'track',
    'video',
    'embed',
    'iframe',
    'object',
    'picture',
    'portal',
    'source',
    'canvas',
    'noscript',
    'script',
    'del_',
    'ins',
    'caption',
    'col',
    'colgroup',
    'table',
    'tbody',
    'td',
    'tfoot',
    'th',
    'thead',
    'tr',
    'button',
    'datalist',
    'fieldset',
    'form',
    'label',
    'legend',
    'meter',
    'optgroup',
    'option',
    'output',
    'progress',
    'select',
    'textarea',
    'details',
    'dialog',
    'summary',
    'slot',
    'template',
]
