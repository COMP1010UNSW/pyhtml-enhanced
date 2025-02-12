class {name}({base}):
    """
    {description}

    {attr_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *options: Options,
        {attr_args}
        **attributes: AttributeType,
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

    def __call__(  # type: ignore
        self,
        *options: Options,
        {attr_args}
        **attributes: AttributeType,
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

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {default_attrs}
