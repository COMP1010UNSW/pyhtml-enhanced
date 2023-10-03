class {name}({base}):
    """
    {description}

    {attr_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *children: Any,
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
        super().__init__(*children, **attributes)

    def __call__(
        self,
        *children: Any,
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
        return super().__call__(*children, **attributes)

    def _get_default_attributes(self) -> dict[str, Any]:
        return {default_attrs}
