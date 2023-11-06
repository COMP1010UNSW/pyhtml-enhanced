# type: ignore
# flake8: noqa
"""
# PyHTML Enhanced / Tags / Generated

Tags generated using documentation from MDN. See code in meta/ in the repo.

Note that all documentation is licensed as CC-BY-SA-2.5

https://creativecommons.org/licenses/by-sa/2.5/
"""
from typing import Any, Optional
from ..__tag_base import Tag, SelfClosingTag, StylableTag

class html(Tag):
    """
    Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


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
        href: Optional[Any] = None,
        target: Optional[Any] = None,
        **attributes: Any,
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

    def __call__(
        self,
        *,
        href: Optional[Any] = None,
        target: Optional[Any] = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'href': None, 'target': None}


class head(Tag):
    """
    Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
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
        href: Optional[Any] = None,
        rel: Optional[Any] = None,
        **attributes: Any,
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

    def __call__(
        self,
        *,
        href: Optional[Any] = None,
        rel: Optional[Any] = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'href': None, 'rel': None}


class meta(Tag):
    """
    Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class style(Tag):
    """
    Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

    * `type`: Type of style to use (defaults to `'text/css'`)

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
    """
    def __init__(
        self,
        *children: Any,
        type: Optional[Any] = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children: Any,
        type: Optional[Any] = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'type': 'text/css'}


class title(Tag):
    """
    Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class body(Tag):
    """
    represents the content of an HTML document. There can be only one such element in a document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        represents the content of an HTML document. There can be only one such element in a document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        represents the content of an HTML document. There can be only one such element in a document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class address(Tag):
    """
    Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class article(Tag):
    """
    Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class aside(Tag):
    """
    Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class footer(Tag):
    """
    Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class header(Tag):
    """
    Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h1(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h2(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h3(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h4(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h5(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class h6(StylableTag):
    """
     Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class hgroup(Tag):
    """
    Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class main(Tag):
    """
    Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class nav(Tag):
    """
    Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class section(Tag):
    """
    Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class search(Tag):
    """
    Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class blockquote(Tag):
    """
    Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class dd(Tag):
    """
    Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class div(Tag):
    """
    The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class dl(Tag):
    """
    Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class dt(Tag):
    """
    Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class figcaption(Tag):
    """
    Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class figure(Tag):
    """
    Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class hr(Tag):
    """
    Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class li(Tag):
    """
    Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class menu(Tag):
    """
    A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class ol(Tag):
    """
    Represents an ordered list of items — typically rendered as a numbered list.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class p(StylableTag):
    """
    Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class pre(Tag):
    """
    Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class ul(Tag):
    """
    Represents an unordered list of items, typically rendered as a bulleted list.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class a(StylableTag):
    """
    Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

    * `href`: URL of page to link to
    * `target`: Use "_blank" to open in a new tab

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
    """
    def __init__(
        self,
        *children,
        href: Optional[Any] = None,
        target: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        href: Optional[Any] = None,
        target: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'href': None, 'target': None}


class abbr(Tag):
    """
    Represents an abbreviation or acronym.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents an abbreviation or acronym.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents an abbreviation or acronym.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class b(StylableTag):
    """
    Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class bdi(Tag):
    """
    Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class bdo(Tag):
    """
    Overrides the current directionality of text, so that the text within is rendered in a different direction.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class br(SelfClosingTag):
    """
    Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
    """
    def __init__(
        self,
        
        
        **attributes: Any,
    ) -> None:
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        attributes |= {
            
        }
        super().__init__(**attributes)

    def __call__(
        self,
        
        
        **attributes: Any,
    ):
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        attributes |= {
            
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class cite(Tag):
    """
    Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class code(Tag):
    """
    Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class data(Tag):
    """
    Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class dfn(Tag):
    """
    Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class em(StylableTag):
    """
    Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class i(StylableTag):
    """
    Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class kbd(Tag):
    """
    Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class mark(Tag):
    """
    Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class q(Tag):
    """
    Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class rp(Tag):
    """
    Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class rt(Tag):
    """
    Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class ruby(Tag):
    """
    Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class s(Tag):
    """
    Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class samp(Tag):
    """
    Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class small(Tag):
    """
    Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class span(Tag):
    """
    A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class strong(StylableTag):
    """
    Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class sub(Tag):
    """
    Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class sup(Tag):
    """
    Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class time(Tag):
    """
    Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class u(Tag):
    """
    Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class var(Tag):
    """
    Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class wbr(Tag):
    """
    Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class area(Tag):
    """
    Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class audio(Tag):
    """
    Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class img(Tag):
    """
    Embeds an image into the document.

    * `src`: Source of the image
    * `alt`: Alt text of the image

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
    """
    def __init__(
        self,
        *children: Any,
        src: Optional[Any] = None,
        alt: Optional[Any] = None,
        **attributes: Any,
    ) -> None:
        """
        Embeds an image into the document.

        * `src`: Source of the image
        * `alt`: Alt text of the image

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        attributes |= {
            'src': src,
            'alt': alt,
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        src: Optional[Any] = None,
        alt: Optional[Any] = None,
        **attributes: Any,
    ):
        """
        Embeds an image into the document.

        * `src`: Source of the image
        * `alt`: Alt text of the image

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        attributes |= {
            'src': src,
            'alt': alt,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'src': None, 'alt': None}


class map(Tag):
    """
    Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class track(Tag):
    """
    Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class video(Tag):
    """
    Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class embed(Tag):
    """
    Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class iframe(Tag):
    """
    Represents a nested browsing context, embedding another HTML page into the current one.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class object(Tag):
    """
    Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class picture(Tag):
    """
    Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class portal(Tag):
    """
    Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class source(Tag):
    """
    Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class canvas(Tag):
    """
    Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class noscript(Tag):
    """
    Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class script(Tag):
    """
    Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

    * `type`: Type of script to use (defaults to `'text/javascript'`)

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
    """
    def __init__(
        self,
        *children: Any,
        type: Optional[Any] = None,
        **attributes: Any,
    ) -> None:
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        * `type`: Type of script to use (defaults to `'text/javascript'`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        attributes |= {
            'type': type,
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        type: Optional[Any] = None,
        **attributes: Any,
    ):
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        * `type`: Type of script to use (defaults to `'text/javascript'`)

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        attributes |= {
            'type': type,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'type': 'text/javascript'}


class del_(Tag):
    """
    Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class ins(Tag):
    """
    Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class caption(Tag):
    """
    Specifies the caption (or title) of a table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies the caption (or title) of a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies the caption (or title) of a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class col(Tag):
    """
    Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class colgroup(Tag):
    """
    Defines a group of columns within a table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a group of columns within a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a group of columns within a table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class table(StylableTag):
    """
    Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
    """
    def __init__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ) -> None:
        """
        Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ):
        """
        Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class tbody(Tag):
    """
    Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class td(StylableTag):
    """
    Defines a cell of a table that contains data. It participates in the _table model_.

    * `colspan`: The number of columns in the table that this cell spans.
    * `rowspan`: The number of rows in the table that this cell spans.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
    """
    def __init__(
        self,
        *children,
        colspan: Optional[Any] = None,
        rowspan: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ) -> None:
        """
        Defines a cell of a table that contains data. It participates in the _table model_.

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

    def __call__(
        self,
        *children,
        colspan: Optional[Any] = None,
        rowspan: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ):
        """
        Defines a cell of a table that contains data. It participates in the _table model_.

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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'colspan': None, 'rowspan': None}


class tfoot(Tag):
    """
    Defines a set of rows summarizing the columns of the table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a set of rows summarizing the columns of the table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a set of rows summarizing the columns of the table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class th(StylableTag):
    """
    Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

    * `scope`: The area of the table that this heading applies to. Allowed values: `"col"`, `"row"`, `"colgroup"`, `"rowgroup"`
    * `colspan`: The number of columns in the table that this heading spans.
    * `rowspan`: The number of rows in the table that this heading spans.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
    """
    def __init__(
        self,
        *children,
        scope: Optional[Any] = None,
        colspan: Optional[Any] = None,
        rowspan: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ) -> None:
        """
        Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

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

    def __call__(
        self,
        *children,
        scope: Optional[Any] = None,
        colspan: Optional[Any] = None,
        rowspan: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ):
        """
        Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'scope': None, 'colspan': None, 'rowspan': None}


class thead(Tag):
    """
    Defines a set of rows defining the head of the columns of the table.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a set of rows defining the head of the columns of the table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a set of rows defining the head of the columns of the table.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class tr(Tag):
    """
    Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class button(StylableTag):
    """
    An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

    * `formmethod`: The HTTP request method to use on click. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
    * `formaction`: The URL to request to on click. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
    """
    def __init__(
        self,
        *children,
        formmethod: Optional[Any] = None,
        formaction: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children,
        formmethod: Optional[Any] = None,
        formaction: Optional[Any] = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'formmethod': None, 'formaction': None}


class datalist(Tag):
    """
    Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class fieldset(Tag):
    """
    Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class form(Tag):
    """
    Represents a document section containing interactive controls for submitting information.

    * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'POST'`)
    * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
    """
    def __init__(
        self,
        *children: Any,
        method: Optional[Any] = None,
        action: Optional[Any] = None,
        **attributes: Any,
    ) -> None:
        """
        Represents a document section containing interactive controls for submitting information.

        * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'POST'`)
        * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        attributes |= {
            'method': method,
            'action': action,
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        method: Optional[Any] = None,
        action: Optional[Any] = None,
        **attributes: Any,
    ):
        """
        Represents a document section containing interactive controls for submitting information.

        * `method`: The HTTP request method to use when submitting this form. In almost all cases, you'll want this to be POST. (defaults to `'POST'`)
        * `action`: The URL to request to when submitting this form. By default, requests will be sent to the same URL as the current page.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        attributes |= {
            'method': method,
            'action': action,
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'method': 'POST', 'action': None}


class input(SelfClosingTag):
    """
    Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

    * `type`: Kind of input control to use (checkbox, radio, date, password, text, etc)
    * `name`: Name of the field. Submitted with the form as part of a name/value pair
    * `value`: Initial value of the control
    * `placeholder`: Placeholder text to use for text inputs. If the field is empty, the placeholder is shown.
    * `readonly`: Include if field is read-only (defaults to `False`)
    * `required`: Include if field is required (defaults to `False`)
    * `formmethod`: The HTTP request method to use on click if this input is a submit button. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
    * `formaction`: The URL to request to on click if this input is a submit button. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
    """
    def __init__(
        self,
        *,
        type: Optional[Any] = None,
        name: Optional[Any] = None,
        value: Optional[Any] = None,
        placeholder: Optional[Any] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        formmethod: Optional[Any] = None,
        formaction: Optional[Any] = None,
        **attributes: Any,
    ) -> None:
        """
        Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

        * `type`: Kind of input control to use (checkbox, radio, date, password, text, etc)
        * `name`: Name of the field. Submitted with the form as part of a name/value pair
        * `value`: Initial value of the control
        * `placeholder`: Placeholder text to use for text inputs. If the field is empty, the placeholder is shown.
        * `readonly`: Include if field is read-only (defaults to `False`)
        * `required`: Include if field is required (defaults to `False`)
        * `formmethod`: The HTTP request method to use on click if this input is a submit button. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click if this input is a submit button. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            'type': type,
            'name': name,
            'value': value,
            'placeholder': placeholder,
            'readonly': readonly,
            'required': required,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        super().__init__(**attributes)

    def __call__(
        self,
        *,
        type: Optional[Any] = None,
        name: Optional[Any] = None,
        value: Optional[Any] = None,
        placeholder: Optional[Any] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        formmethod: Optional[Any] = None,
        formaction: Optional[Any] = None,
        **attributes: Any,
    ):
        """
        Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

        * `type`: Kind of input control to use (checkbox, radio, date, password, text, etc)
        * `name`: Name of the field. Submitted with the form as part of a name/value pair
        * `value`: Initial value of the control
        * `placeholder`: Placeholder text to use for text inputs. If the field is empty, the placeholder is shown.
        * `readonly`: Include if field is read-only (defaults to `False`)
        * `required`: Include if field is required (defaults to `False`)
        * `formmethod`: The HTTP request method to use on click if this input is a submit button. Generally, it is preferred to set the `method` attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click if this input is a submit button. Generally, it is preferred to set the `action` attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            'type': type,
            'name': name,
            'value': value,
            'placeholder': placeholder,
            'readonly': readonly,
            'required': required,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'type': None, 'name': None, 'value': None, 'placeholder': None, 'readonly': False, 'required': False, 'formmethod': None, 'formaction': None}


class label(Tag):
    """
    Represents a caption for an item in a user interface.

    * `for_`: ID of input field to associate this label with

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
    """
    def __init__(
        self,
        *children: Any,
        for_: Optional[Any] = None,
        **attributes: Any,
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

    def __call__(
        self,
        *children: Any,
        for_: Optional[Any] = None,
        **attributes: Any,
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

    def _get_default_attributes(self) -> dict[str, Any]:
        return {'for_': None}


class legend(Tag):
    """
    Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class meter(Tag):
    """
    Represents either a scalar value within a known range or a fractional value.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents either a scalar value within a known range or a fractional value.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents either a scalar value within a known range or a fractional value.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class optgroup(Tag):
    """
    Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class option(Tag):
    """
    Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class output(Tag):
    """
    Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class progress(Tag):
    """
    Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class select(Tag):
    """
    Represents a control that provides a menu of options.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a control that provides a menu of options.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a control that provides a menu of options.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class textarea(Tag):
    """
    Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class details(Tag):
    """
    Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class dialog(Tag):
    """
    Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class summary(Tag):
    """
    Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class slot(Tag):
    """
    Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {}


class template(Tag):
    """
    A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

    

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
    """
    def __init__(
        self,
        *children: Any,
        
        **attributes: Any,
    ) -> None:
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        attributes |= {
            
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
        
        **attributes: Any,
    ):
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        attributes |= {
            
        }
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
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
    'input',
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
