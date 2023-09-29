class {name}({base}):
    """
    {description}

    {prop_docs_outer}

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

        {prop_docs_inner}

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

        {prop_docs_inner}

        [View full documentation]({link})
        """
        properties |= {
            {prop_unions}
        }
        return super().__call__(*children, **properties)
