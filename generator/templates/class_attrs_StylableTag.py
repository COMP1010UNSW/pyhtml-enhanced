class {name}(Tag):
    """
    {description}

    {attr_docs_outer}

    [View full documentation]({link})
    """
    def __init__(
        self,
        *children: ChildrenType,
        {attr_args}
        id: str | None = None,
        _class: str | None = None,
        style: str | None = None,
        **attributes: AttributeType,
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

    def __call__(  # type: ignore
        self,
        *children: ChildrenType,
        {attr_args}
        id: str | None = None,
        _class: str | None = None,
        style: str | None = None,
        **attributes: AttributeType,
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

    def _get_default_attributes(self, given: dict[str, AttributeType]) -> dict[str, AttributeType]:
        return {default_attrs}
