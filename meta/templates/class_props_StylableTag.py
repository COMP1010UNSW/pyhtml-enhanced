class {name}({base}):
    """
    {description}

    {prop_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *children,
        {prop_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ) -> None:
        """
        {description}

        {prop_docs_inner}

        [View full documentation]({link})
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            {prop_unions}
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children,
        {prop_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        {description}

        {prop_docs_inner}

        [View full documentation]({link})
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            {prop_unions}
        }
        return super().__call__(*children, **properties)
