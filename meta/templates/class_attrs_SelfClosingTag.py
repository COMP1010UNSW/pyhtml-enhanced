class {name}({base}):
    """
    {description}

    {attr_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        {kw_only}
        {attr_args}
        **attributes: Any,
    ) -> None:
        """
        {description}

        {attr_docs_inner}

        [View full documentation]({link})
        """
        attributes |= {
            {attr_unions}
        }
        super().__init__(**attributes)

    def __call__(
        self,
        {kw_only}
        {attr_args}
        **attributes: Any,
    ):
        """
        {description}

        {attr_docs_inner}

        [View full documentation]({link})
        """
        attributes |= {
            {attr_unions}
        }
        return super().__call__(**attributes)
