class {name}({base}):
    """
    {description}

    {link}
    """
    def __init__(
        self,
        *children: Any,
        {prop_args}
        **properties: Any,
    ) -> None:
        properties |= {
            {prop_unions}
        }
        super().__init__(*children, **properties)
