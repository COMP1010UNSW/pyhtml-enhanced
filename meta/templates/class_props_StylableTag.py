class {name}({base}):
    """
    {description}

    [View full documentation]({link})
    """
    def __init__(
        self,
        {prop_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ) -> None:
        """
        {description}

        [View full documentation]({link})
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            {prop_unions}
        }
        super().__init__(**properties)

    def __call__(
        self,
        {prop_args}
        id: Any = None,
        _class: Any = None,
        style: Any = None,
        **properties: Any,
    ):
        """
        {description}

        [View full documentation]({link})
        """
        properties |= {
            '_class': _class,
            'id': id,
            'style': style,
            {prop_unions}
        }
        return super().__call__(**properties)
