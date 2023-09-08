class {name}({base}):
    """
    {description}

    [View full documentation]({link})
    """
    def __init__(
        self,
        {kw_only}
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
        super().__init__(**properties)

    def __call__(
        self,
        {kw_only}
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
        return super().__call__(**properties)
