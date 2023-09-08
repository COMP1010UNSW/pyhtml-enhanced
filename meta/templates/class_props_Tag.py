class {name}({base}):
    """
    {description}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *children: Any,
        {prop_args}
        **properties: Any,
    ) -> None:
        """
        {description}

        [View full documentation]({link})
        """
        properties |= {
            {prop_unions}
        }
        super().__init__(*children, **properties)

    def __call__(
        self,
        *children: Any,
        {prop_args}
        **properties: Any,
    ):
        """
        {description}

        [View full documentation]({link})
        """
        properties |= {
            {prop_unions}
        }
        return super().__call__(*children, **properties)
