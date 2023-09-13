# type: ignore
# flake8: noqa
"""
# PyHTML Enhanced / Tags / Generated

Tags generated using documentation from MDN. See code in meta/ in the repo.

Note that all documentation is licensed as CC-BY-SA-2.5

https://creativecommons.org/licenses/by-sa/2.5/
"""
from typing import Any
from ..__tag_base import Tag, SelfClosingTag, StylableTag

class html(Tag):
    """
    Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents the root (top-level element) of an HTML document, so it is also referred to as the _root element_. All other elements must be descendants of this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class base(SelfClosingTag):
    """
    Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
    """
    def __init__(
        self,
        *,
        href: Any = None,
        target: Any = None,
        **properties: Any,
    ) -> None:
        """
        Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
        """
        properties |= {
            'href': href,
            'target': target,
        }
        super().__init__(**properties)

    def __call__(
        self,
        *,
        href: Any = None,
        target: Any = None,
        **properties: Any,
    ):
        """
        Specifies the base URL to use for all relative URLs in a document. There can be only one such element in a document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base)
        """
        properties |= {
            'href': href,
            'target': target,
        }
        return super().__call__(**properties)


class head(Tag):
    """
    Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Contains machine-readable information (metadata) about the document, like its [title](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title), [scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), and [style sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class link(SelfClosingTag):
    """
    Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
    """
    def __init__(
        self,
        *,
        href: Any = None,
        rel: Any = None,
        **properties: Any,
    ) -> None:
        """
        Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
        """
        properties |= {
            'href': href,
            'rel': rel,
        }
        super().__init__(**properties)

    def __call__(
        self,
        *,
        href: Any = None,
        rel: Any = None,
        **properties: Any,
    ):
        """
        Specifies relationships between the current document and an external resource. This element is most commonly used to link to CSS but is also used to establish site icons (both "favicon" style icons and icons for the home screen and apps on mobile devices) among other things.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link)
        """
        properties |= {
            'href': href,
            'rel': rel,
        }
        return super().__call__(**properties)


class meta(Tag):
    """
    Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents [metadata](https://developer.mozilla.org/en-US/docs/Glossary/Metadata) that cannot be represented by other HTML meta-related elements, like [`<base>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base), [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link), [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script), [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style) and [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class style(Tag):
    """
    Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Contains style information for a document or part of a document. It contains CSS, which is applied to the contents of the document containing this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class title(Tag):
    """
    Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines the document's title that is shown in a [ browser](https://developer.mozilla.org/en-US/docs/Glossary/Browser)'s title bar or a page's tab. It only contains text; tags within the element are ignored.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class body(Tag):
    """
    represents the content of an HTML document. There can be only one such element in a document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        represents the content of an HTML document. There can be only one such element in a document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        represents the content of an HTML document. There can be only one such element in a document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class address(Tag):
    """
    Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Indicates that the enclosed HTML provides contact information for a person or people, or for an organization.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class article(Tag):
    """
    Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a self-contained composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., in syndication). Examples include a forum post, a magazine or newspaper article, a blog entry, a product card, a user-submitted comment, an interactive widget or gadget, or any other independent item of content.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class aside(Tag):
    """
    Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a portion of a document whose content is only indirectly related to the document's main content. Asides are frequently presented as sidebars or call-out boxes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class footer(Tag):
    """
    Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a footer for its nearest ancestor [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Content_categories#sectioning_content) or [sectioning root](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element. A `<footer>` typically contains information about the author of the section, copyright data, or links to related documents.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class header(Tag):
    """
    Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents introductory content, typically a group of introductory or navigational aids. It may contain some heading elements but also a logo, a search form, an author name, and other elements.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h1)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h2)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h3)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h4)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h5)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
         Represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest.                                                                                                                                                                                                                                                                       

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


class hgroup(Tag):
    """
    Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a heading grouped with any secondary content, such as subheadings, an alternative title, or a tagline.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class main(Tag):
    """
    Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents the dominant content of the body of a document. The main content area consists of content that is directly related to or expands upon the central topic of a document, or the central functionality of an application.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class nav(Tag):
    """
    Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a section of a page whose purpose is to provide navigation links, either within the current document or to other documents. Common examples of navigation sections are menus, tables of contents, and indexes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class section(Tag):
    """
    Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a generic standalone section of a document, which doesn't have a more specific semantic element to represent it. Sections should always have a heading, with very few exceptions.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class search(Tag):
    """
    Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a part that contains a set of form controls or other content related to performing a search or filtering operation.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class blockquote(Tag):
    """
    Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Indicates that the enclosed text is an extended quotation. Usually, this is rendered visually by indentation. A URL for the source of the quotation may be given using the `cite` attribute, while a text representation of the source can be given using the [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class dd(Tag):
    """
    Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Provides the description, definition, or value for the preceding term ([`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)) in a description list ([`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class div(Tag):
    """
    The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        The generic container for flow content. It has no effect on the content or layout until styled in some way using CSS (e.g., styling is directly applied to it, or some kind of layout model like [ flexbox](https://developer.mozilla.org/en-US/docs/Glossary/Flexbox) is applied to its parent element).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class dl(Tag):
    """
    Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt) element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class dt(Tag):
    """
    Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies a term in a description or definition list, and as such must be used inside a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl) element. It is usually followed by a [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element; however, multiple `<dt>` elements in a row indicate several terms that are all defined by the immediate next [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class figcaption(Tag):
    """
    Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a caption or legend describing the rest of the contents of its parent [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class figure(Tag):
    """
    Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption) element. The figure, its caption, and its contents are referenced as a single unit.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class hr(Tag):
    """
    Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a thematic break between paragraph-level elements: for example, a change of scene in a story, or a shift of topic within a section.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class li(Tag):
    """
    Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents an item in a list. It must be contained in a parent element: an ordered list ([`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)), an unordered list ([`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)), or a menu ([`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)). In menus and unordered lists, list items are usually displayed using bullet points. In ordered lists, they are usually displayed with an ascending counter on the left, such as a number or letter.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class menu(Tag):
    """
    A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        A semantic alternative to [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul), but treated by browsers (and exposed through the accessibility tree) as no different than [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul). It represents an unordered list of items (which are represented by [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li) elements).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class ol(Tag):
    """
    Represents an ordered list of items — typically rendered as a numbered list.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents an ordered list of items — typically rendered as a numbered list.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
        Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


class pre(Tag):
    """
    Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents preformatted text which is to be presented exactly as written in the HTML file. The text is typically rendered using a non-proportional, or [monospaced](https://en.wikipedia.org/wiki/Monospaced_font), font. Whitespace inside this element is displayed as written.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class ul(Tag):
    """
    Represents an unordered list of items, typically rendered as a bulleted list.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents an unordered list of items, typically rendered as a bulleted list.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class a(StylableTag):
    """
    Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
    """
    def __init__(
        self,
        *children,
        href: Any = None,
        target: Any = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ) -> None:
        """
        Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            'href': href,
            'target': target,
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        href: Any = None,
        target: Any = None,
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Together with its `href` attribute, creates a hyperlink to web pages, files, email addresses, locations within the current page, or anything else a URL can address.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            'href': href,
            'target': target,
        }
        return super().__call__(*children, **properties)


class abbr(Tag):
    """
    Represents an abbreviation or acronym.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents an abbreviation or acronym.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents an abbreviation or acronym.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
        Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Used to draw the reader's attention to the element's contents, which are not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use `<b>` for styling text or granting importance. If you wish to create boldface text, you should use the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property. If you wish to indicate an element is of special importance, you should use the strong element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


class bdi(Tag):
    """
    Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Tells the browser's bidirectional algorithm to treat the text it contains in isolation from its surrounding text. It's particularly useful when a website dynamically inserts some text and doesn't know the directionality of the text being inserted.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class bdo(Tag):
    """
    Overrides the current directionality of text, so that the text within is rendered in a different direction.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Overrides the current directionality of text, so that the text within is rendered in a different direction.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class br(SelfClosingTag):
    """
    Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
    """
    def __init__(
        self,
        
        
        **properties: Any,
    ) -> None:
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        properties |= {
            
        }
        super().__init__(**properties)

    def __call__(
        self,
        
        
        **properties: Any,
    ):
        """
        Produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br)
        """
        properties |= {
            
        }
        return super().__call__(**properties)


class cite(Tag):
    """
    Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to mark up the title of a cited creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class code(Tag):
    """
    Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Displays its contents styled in a fashion intended to indicate that the text is a short fragment of computer code. By default, the content text is displayed using the user agent's default monospace font.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class data(Tag):
    """
    Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Links a given piece of content with a machine-readable translation. If the content is time- or date-related, the`<time>` element must be used.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class dfn(Tag):
    """
    Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to indicate the term being defined within the context of a definition phrase or sentence. The ancestor [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p) element, the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt)/[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd) pairing, or the nearest section ancestor of the `<dfn>` element, is considered to be the definition of the term.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
        Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Marks text that has stress emphasis. The `<em>` element can be nested, with each nesting level indicating a greater degree of emphasis.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
        Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, and taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


class kbd(Tag):
    """
    Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a span of inline text denoting textual user input from a keyboard, voice input, or any other text entry device. By convention, the user agent defaults to rendering the contents of a `<kbd>` element using its default monospace font, although this is not mandated by the HTML standard.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class mark(Tag):
    """
    Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents text which is marked or highlighted for reference or notation purposes due to the marked passage's relevance in the enclosing context.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class q(Tag):
    """
    Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Indicates that the enclosed text is a short inline quotation. Most modern browsers implement this by surrounding the text in quotation marks. This element is intended for short quotations that don't require paragraph breaks; for long quotations use the [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class rp(Tag):
    """
    Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to provide fall-back parentheses for browsers that do not support the display of ruby annotations using the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element. One `<rp>` element should enclose each of the opening and closing parentheses that wrap the [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt) element that contains the annotation's text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class rt(Tag):
    """
    Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies the ruby text component of a ruby annotation, which is used to provide pronunciation, translation, or transliteration information for East Asian typography. The `<rt>` element must always be contained within a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class ruby(Tag):
    """
    Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class s(Tag):
    """
    Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Renders text with a strikethrough, or a line through it. Use the `<s>` element to represent things that are no longer relevant or no longer accurate. However, `<s>` is not appropriate when indicating document edits; for that, use the del and ins elements, as appropriate.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class samp(Tag):
    """
    Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to enclose inline text which represents sample (or quoted) output from a computer program. Its contents are typically rendered using the browser's default monospaced font (such as [Courier](<https://en.wikipedia.org/wiki/Courier_(typeface)>) or Lucida Console).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class small(Tag):
    """
    Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font size smaller, such as from `small` to `x-small`.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class span(Tag):
    """
    A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        A generic inline container for phrasing content, which does not inherently represent anything. It can be used to group elements for styling purposes (using the `class` or `id` attributes), or because they share attribute values, such as `lang`. It should be used only when no other semantic element is appropriate. `<span>` is very much like a div element, but div is a [block-level element](/en-US/docs/Glossary/Block-level_content) whereas a `<span>` is an [inline-level element](/en-US/docs/Glossary/Inline-level_content).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
        **properties: Any,
    ) -> None:
        """
        Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong)
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            
        }
        return super().__call__(*children, **properties)


class sub(Tag):
    """
    Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class sup(Tag):
    """
    Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class time(Tag):
    """
    Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a specific period in time. It may include the `datetime` attribute to translate dates into machine-readable format, allowing for better search engine results or custom features such as reminders.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class u(Tag):
    """
    Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a span of inline text which should be rendered in a way that indicates that it has a non-textual annotation. This is rendered by default as a simple solid underline but may be altered using CSS.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class var(Tag):
    """
    Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class wbr(Tag):
    """
    Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class area(Tag):
    """
    Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines an area inside an image map that has predefined clickable areas. An _image map_ allows geometric areas on an image to be associated with [ hyperlink](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class audio(Tag):
    """
    Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to embed sound content in documents. It may contain one or more audio sources, represented using the `src` attribute or the source element: the browser will choose the most suitable one. It can also be the destination for streamed media, using a [MediaStream](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class img(Tag):
    """
    Embeds an image into the document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
    """
    def __init__(
        self,
        *children: Any,
        src: Any = None,
        alt: Any = None,
        **properties: Any,
    ) -> None:
        """
        Embeds an image into the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        properties |= {
            'src': src,
            'alt': alt,
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        src: Any = None,
        alt: Any = None,
        **properties: Any,
    ):
        """
        Embeds an image into the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img)
        """
        properties |= {
            'src': src,
            'alt': alt,
        }
        return super().__call__(*children, **properties)


class map(Tag):
    """
    Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements to define an image map (a clickable link area).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class track(Tag):
    """
    Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used as a child of the media elements, audio and video. It lets you specify timed text tracks (or time-based data), for example to automatically handle subtitles. The tracks are formatted in [WebVTT format](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API) (`.vtt` files)—Web Video Text Tracks.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class video(Tag):
    """
    Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Embeds a media player which supports video playback into the document. You can also use `<video>` for audio content, but the audio element may provide a more appropriate user experience.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class embed(Tag):
    """
    Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Embeds external content at the specified point in the document. This content is provided by an external application or other source of interactive content such as a browser plug-in.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class iframe(Tag):
    """
    Represents a nested browsing context, embedding another HTML page into the current one.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a nested browsing context, embedding another HTML page into the current one.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class object(Tag):
    """
    Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class picture(Tag):
    """
    Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Contains zero or more [`<source>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) elements and one [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) element to offer alternative versions of an image for different display/device scenarios.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class portal(Tag):
    """
    Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Enables the embedding of another HTML page into the current one to enable smoother navigation into new pages.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class source(Tag):
    """
    Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies multiple media resources for the picture, the audio element, or the video element. It is a void element, meaning that it has no content and does not have a closing tag. It is commonly used to offer the same media content in multiple file formats in order to provide compatibility with a broad range of browsers given their differing support for [image file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) and [media file formats](https://developer.mozilla.org/en-US/docs/Web/Media/Formats).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class canvas(Tag):
    """
    Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Container element to use with either the [canvas scripting API](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or the [WebGL API](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) to draw graphics and animations.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class noscript(Tag):
    """
    Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class script(Tag):
    """
    Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages, such as [WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API)'s GLSL shader programming language and [JSON](/en-US/docs/Glossary/JSON).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class del_(Tag):
    """
    Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a range of text that has been deleted from a document. This can be used when rendering "track changes" or source code diff information, for example. The `<ins>` element can be used for the opposite purpose: to indicate text that has been added to the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class ins(Tag):
    """
    Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a range of text that has been added to a document. You can use the `<del>` element to similarly represent a range of text that has been deleted from the document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class caption(Tag):
    """
    Specifies the caption (or title) of a table.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies the caption (or title) of a table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies the caption (or title) of a table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class col(Tag):
    """
    Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a column within a table and is used for defining common semantics on all common cells. It is generally found within a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class colgroup(Tag):
    """
    Defines a group of columns within a table.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a group of columns within a table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a group of columns within a table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class table(Tag):
    """
    Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents tabular data — that is, information presented in a two-dimensional table comprised of rows and columns of cells containing data.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class tbody(Tag):
    """
    Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Encapsulates a set of table rows ([`<tr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr) elements), indicating that they comprise the body of the table ([`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table)).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class td(Tag):
    """
    Defines a cell of a table that contains data. It participates in the _table model_.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a cell of a table that contains data. It participates in the _table model_.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a cell of a table that contains data. It participates in the _table model_.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class tfoot(Tag):
    """
    Defines a set of rows summarizing the columns of the table.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a set of rows summarizing the columns of the table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a set of rows summarizing the columns of the table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class th(Tag):
    """
    Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a cell as a header of a group of table cells. The exact nature of this group is defined by the `scope` and `headers` attributes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class thead(Tag):
    """
    Defines a set of rows defining the head of the columns of the table.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a set of rows defining the head of the columns of the table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a set of rows defining the head of the columns of the table.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class tr(Tag):
    """
    Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Defines a row of cells in a table. The row's cells can then be established using a mix of [`<td>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td) (data cell) and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th) (header cell) elements.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class button(Tag):
    """
    An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        An interactive element activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology. Once activated, it performs an action, such as submitting a [form](/en-US/docs/Learn/Forms) or opening a dialog.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class datalist(Tag):
    """
    Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Contains a set of [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option) elements that represent the permissible or recommended options available to choose from within other controls.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class fieldset(Tag):
    """
    Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)) within a web form.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class form(Tag):
    """
    Represents a document section containing interactive controls for submitting information.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a document section containing interactive controls for submitting information.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a document section containing interactive controls for submitting information.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class input(Tag):
    """
    Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to create interactive controls for web-based forms to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and user agent. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class label(Tag):
    """
    Represents a caption for an item in a user interface.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a caption for an item in a user interface.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a caption for an item in a user interface.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class legend(Tag):
    """
    Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a caption for the content of its parent [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset).

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class meter(Tag):
    """
    Represents either a scalar value within a known range or a fractional value.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents either a scalar value within a known range or a fractional value.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents either a scalar value within a known range or a fractional value.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class optgroup(Tag):
    """
    Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Creates a grouping of options within a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class option(Tag):
    """
    Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Used to define an item contained in a select, an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup), or a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist) element. As such, `<option>` can represent menu items in popups and other lists of items in an HTML document.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class output(Tag):
    """
    Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Container element into which a site or app can inject the results of a calculation or the outcome of a user action.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class progress(Tag):
    """
    Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class select(Tag):
    """
    Represents a control that provides a menu of options.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a control that provides a menu of options.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a control that provides a menu of options.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class textarea(Tag):
    """
    Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a multi-line plain-text editing control, useful when you want to allow users to enter a sizeable amount of free-form text, for example, a comment on a review or feedback form.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class details(Tag):
    """
    Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Creates a disclosure widget in which information is visible only when the widget is toggled into an "open" state. A summary or label must be provided using the [`<summary>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary) element.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class dialog(Tag):
    """
    Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Represents a dialog box or other interactive component, such as a dismissible alert, inspector, or subwindow.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class summary(Tag):
    """
    Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Specifies a summary, caption, or legend for a details element's disclosure box. Clicking the `<summary>` element toggles the state of the parent [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) element open and closed.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class slot(Tag):
    """
    Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        Part of the [Web Components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components) technology suite, this element is a placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


class template(Tag):
    """
    A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
    """
    def __init__(
        self,
        *children: Any,
        
        **properties: Any,
    ) -> None:
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        properties |= {
            
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        
        **properties: Any,
    ):
        """
        A mechanism for holding HTML that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime using JavaScript.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template)
        """
        properties |= {
            
        }
        return super().__call__(*children, **properties)


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
