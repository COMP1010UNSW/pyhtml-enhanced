"""
# PyHTML Enhanced

A drop-in replacement for PyHTML with improved editor support and
documentation.
"""
from .__tag_base import Tag, Comment

from .__tags import (
    html,
    base,
    head,
    link,
    meta,
    style,
    title,
    body,
    address,
    article,
    aside,
    footer,
    header,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    hgroup,
    main,
    nav,
    section,
    search,
    blockquote,
    dd,
    div,
    dl,
    dt,
    figcaption,
    figure,
    hr,
    li,
    menu,
    ol,
    p,
    pre,
    ul,
    a,
    abbr,
    b,
    bdi,
    bdo,
    br,
    cite,
    code,
    data,
    dfn,
    em,
    i,
    kbd,
    mark,
    q,
    rp,
    rt,
    ruby,
    s,
    samp,
    small,
    span,
    strong,
    sub,
    sup,
    time,
    u,
    var,
    wbr,
    area,
    audio,
    img,
    map,
    track,
    video,
    embed,
    iframe,
    object,
    picture,
    portal,
    source,
    canvas,
    noscript,
    script,
    del_,
    ins,
    caption,
    col,
    colgroup,
    table,
    tbody,
    td,
    tfoot,
    th,
    thead,
    tr,
    button,
    datalist,
    fieldset,
    form,
    input,
    label,
    legend,
    meter,
    optgroup,
    option,
    output,
    progress,
    select,
    textarea,
    details,
    dialog,
    summary,
    slot,
    template,
    # TODO: Add other tags as required
    input_,
    object_,
)


__all__ = [
    'Comment',
    'Tag',
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
    'input_',
    'object_',
]