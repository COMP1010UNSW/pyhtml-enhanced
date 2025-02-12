"""
# Pyhtml / Tags / Input

Custom definition of the `<input>` tag, to improve type safety and implement
custom behaviour.
"""

from typing import Literal, overload

from ..__render_options import RenderOptions
from ..__tag_base import SelfClosingTag
from ..__types import AttributeType

InputTypes = Literal[
    "button",
    "checkbox",
    "color",
    "date",
    "datetime-local",
    "email",
    "file",
    "hidden",
    "image",
    "month",
    "number",
    "password",
    "radio",
    "range",
    "reset",
    "search",
    "submit",
    "tel",
    "text",
    "time",
    "url",
    "week",
]


class input(SelfClosingTag):
    """
    Used to create interactive controls for web-based forms to accept data
    from the user; a wide variety of types of input data and control
    widgets are available, depending on the device and user agent. The
    `<input>` element is one of the most powerful and complex in all of
    HTML due to the sheer number of combinations of input types and
    attributes.

    Common input types:

    * [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/submit): a button that submits the form to the server

    * [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text): a single-line text field

    * [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/button): a button that can be accessed using JavaScript

    * [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox): a checkbox

    * [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email): an email address

    * [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file): a file upload

    * [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number): a number

    * [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password): a password

    * [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio): a radio button

    * [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/reset): a button that resets the form to the default values

    * And others: [view the full list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input#input_types)

    Common attributes are:

    * `type`: Kind of input control to use (checkbox, radio, date,
        password, text, etc)

    * `name`: Name of the field. Submitted with the form as part of a
        name/value pair

    * `value`: Initial value of the control

    * `placeholder`: Placeholder text to use for text inputs. If the field
        is empty, the placeholder is shown.

    * `readonly`: Include if field is read-only, meaning contents cannot be
        edited (defaults to `False`)

    * `disabled`: Include if field is disabled, meaning contents cannot be
        edited, and it will not be included in the form submission (defaults
        to `False`)

    * `required`: Include if field is required (defaults to `False`)

    * `formmethod`: The HTTP request method to use on click if this input
        is a submit button. Generally, it is preferred to set the `method`
        attribute on the `<form>` element instead of this.

    * `formaction`: The URL to request to on click if this input is a
        submit button. Generally, it is preferred to set the `action`
        attribute on the `<form>` element instead of this.

    * `autofocus`: whether the element should automatically be selected
      when the page is loaded.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
    """

    # Form submission
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["submit"] = "submit",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Text box
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["text"] = "text",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        spellcheck: Literal["true", "false", ""] | None = None,
        disabled: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # JS button
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["button"] = "button",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Checkbox
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["checkbox"] = "checkbox",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        checked: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Email address
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["email"] = "email",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # File upload
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["file"] = "file",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        accept: str | None = None,
        multiple: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Number
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["number"] = "number",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        min: str | None = None,
        max: str | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Password
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["password"] = "password",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Radio button
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["radio"] = "radio",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        checked: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Range
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: Literal["range"] = "range",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        min: str | None = None,
        max: str | None = None,
        step: str | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # default, suggesting types
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: InputTypes | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        placeholder: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # default, allowing all arguments
    @overload
    def __init__(
        self,
        *options: RenderOptions,
        type: str | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        placeholder: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    def __init__(
        self,
        *options: RenderOptions,
        type: str | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Used to create interactive controls for web-based forms to accept data
        from the user; a wide variety of types of input data and control
        widgets are available, depending on the device and user agent. The
        `<input>` element is one of the most powerful and complex in all of
        HTML due to the sheer number of combinations of input types and
        attributes.

        Common input types:

        * [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/submit): a button that submits the form to the server

        * [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text): a single-line text field

        * [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/button): a button that can be accessed using JavaScript

        * [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox): a checkbox

        * [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email): an email address

        * [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file): a file upload

        * [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number): a number

        * [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password): a password

        * [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio): a radio button

        * [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/reset): a button that resets the form to the default values

        * And others: [view the full list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input#input_types)

        Common attributes are:

        * `type`: Kind of input control to use (checkbox, radio, date,
          password, text, etc)

        * `name`: Name of the field. Submitted with the form as part of a
          name/value pair

        * `value`: Initial value of the control

        * `placeholder`: Placeholder text to use for text inputs. If the field
          is empty, the placeholder is shown.

        * `readonly`: Include if field is read-only, meaning contents cannot be
          edited (defaults to `False`)

        * `disabled`: Include if field is disabled, meaning contents cannot be
          edited, and it will not be included in the form submission (defaults
          to `False`)

        * `required`: Include if field is required (defaults to `False`)

        * `formmethod`: The HTTP request method to use on click if this input
          is a submit button. Generally, it is preferred to set the `method`
          attribute on the `<form>` element instead of this.

        * `formaction`: The URL to request to on click if this input is a
          submit button. Generally, it is preferred to set the `action`
          attribute on the `<form>` element instead of this.

        * `autofocus`: whether the element should automatically be selected
          when the page is loaded.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            "id": id,
            "name": name,
            "value": value,
            "type": type,
        }
        super().__init__(*options, **attributes)

    # Form submission
    @overload  # type: ignore
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["submit"] = "submit",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Text box
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["text"] = "text",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        spellcheck: Literal["true", "false", ""] | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # JS button
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["button"] = "button",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Checkbox
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["checkbox"] = "checkbox",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        checked: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Email address
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["email"] = "email",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # File upload
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["file"] = "file",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        required: bool | None = None,
        accept: str | None = None,
        multiple: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Number
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["number"] = "number",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        required: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        min: str | None = None,
        max: str | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Password
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["password"] = "password",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        placeholder: str | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Radio button
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["radio"] = "radio",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        checked: bool | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # Range
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: Literal["range"] = "range",
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        required: bool | None = None,
        min: str | None = None,
        max: str | None = None,
        step: str | None = None,
        placeholder: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # default, suggesting types
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: InputTypes | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        placeholder: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    # default, allowing all arguments
    @overload
    def __call__(
        self,
        *options: RenderOptions,
        type: str | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        placeholder: str | None = None,
        disabled: bool | None = None,
        readonly: bool | None = None,
        required: bool | None = None,
        autofocus: bool | None = None,
        **attributes: AttributeType,
    ) -> None: ...

    def __call__(  # type: ignore
        self,
        *options: RenderOptions,
        type: str | None = None,
        id: str | None = None,
        name: str | None = None,
        value: str | None = None,
        **attributes: AttributeType,
    ):
        """
        Used to create interactive controls for web-based forms to accept data
        from the user; a wide variety of types of input data and control
        widgets are available, depending on the device and user agent. The
        `<input>` element is one of the most powerful and complex in all of
        HTML due to the sheer number of combinations of input types and
        attributes.

        Common input types:

        * [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/submit): a button that submits the form to the server

        * [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text): a single-line text field

        * [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/button): a button that can be accessed using JavaScript

        * [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox): a checkbox

        * [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/email): an email address

        * [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file): a file upload

        * [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/number): a number

        * [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/password): a password

        * [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/radio): a radio button

        * [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/reset): a button that resets the form to the default values

        * And others: [view the full list](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Input#input_types)

        Common attributes are:

        * `type`: Kind of input control to use (checkbox, radio, date,
          password, text, etc)

        * `name`: Name of the field. Submitted with the form as part of a
          name/value pair

        * `value`: Initial value of the control

        * `placeholder`: Placeholder text to use for text inputs. If the field
          is empty, the placeholder is shown.

        * `readonly`: Include if field is read-only, meaning contents cannot be
          edited (defaults to `False`)

        * `disabled`: Include if field is disabled, meaning contents cannot be
          edited, and it will not be included in the form submission (defaults
          to `False`)

        * `required`: Include if field is required (defaults to `False`)

        * `formmethod`: The HTTP request method to use on click if this input
          is a submit button. Generally, it is preferred to set the `method`
          attribute on the `<form>` element instead of this.

        * `formaction`: The URL to request to on click if this input is a
          submit button. Generally, it is preferred to set the `action`
          attribute on the `<form>` element instead of this.

        * `autofocus`: whether the element should automatically be selected
          when the page is loaded. This only applies to the first element on
          the page.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            "id": id,
            "name": name,
            "value": value,
            "type": type,
        }
        return super().__call__(*options, **attributes)

    def _get_default_attributes(
        self,
        given: dict[str, AttributeType],
    ) -> dict[str, AttributeType]:
        if (
            given.get("formaction") is not None
            and given.get("formmethod") is None
        ):
            formmethod = "POST"
        else:
            formmethod = None
        return {
            "type": None,
            "name": None,
            "value": None,
            "placeholder": None,
            "readonly": False,
            "required": False,
            "formmethod": formmethod,
            "formaction": None,
        }
