class {name}({base}):
    """
    {description}

    {attr_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *children,
        {attr_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ) -> None:
        """
        {description}

        {attr_docs_inner}

        [View full documentation]({link})
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            {attr_unions}
        }
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children,
        {attr_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **attributes: Any,
    ):
        """
        {description}

        {attr_docs_inner}

        [View full documentation]({link})
        """
        attributes |= {
            '_class': _class,
            'id': id,
            'style': style,
            {attr_unions}
        }
        return super().__call__(*children, **attributes)
