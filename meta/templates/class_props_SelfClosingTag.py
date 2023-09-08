class {name}({base}):
    """
    {description}

    {link}
    """
    def __init__(
        self,
        {prop_args}
        **properties: Any,
    ) -> None:
        properties |= {
            {prop_unions}
        }
        super().__init__(**properties)
