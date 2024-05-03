"""
# Pyhtml / Tags / Input

Custom definition of the `<input>` tag, to improve type safety and implement
custom behaviour.
"""
from ..__tag_base import SelfClosingTag
from ..__types import AttributeType
from typing import Literal, Optional, overload


InputTypes = Literal[
    'button',
    'checkbox',
    'color',
    'date',
    'datetime-local',
    'email',
    'file',
    'hidden',
    'image',
    'month',
    'number',
    'password',
    'radio',
    'range',
    'reset',
    'search',
    'submit',
    'tel',
    'text',
    'time',
    'url',
    'week',
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
        *,
        type: Literal['submit'] = 'submit',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Text box
    @overload
    def __init__(
        self,
        *,
        type: Literal['text'] = 'text',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        spellcheck: Optional[Literal["true", "false", ""]] = None,
        disabled: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # JS button
    @overload
    def __init__(
        self,
        *,
        type: Literal['button'] = 'button',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Checkbox
    @overload
    def __init__(
        self,
        *,
        type: Literal['checkbox'] = 'checkbox',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        checked: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Email address
    @overload
    def __init__(
        self,
        *,
        type: Literal['email'] = 'email',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # File upload
    @overload
    def __init__(
        self,
        *,
        type: Literal['file'] = 'file',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        accept: Optional[str] = None,
        multiple: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Number
    @overload
    def __init__(
        self,
        *,
        type: Literal['number'] = 'number',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        min: Optional[str] = None,
        max: Optional[str] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Password
    @overload
    def __init__(
        self,
        *,
        type: Literal['password'] = 'password',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Radio button
    @overload
    def __init__(
        self,
        *,
        type: Literal['radio'] = 'radio',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        checked: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Range
    @overload
    def __init__(
        self,
        *,
        type: Literal['range'] = 'range',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        min: Optional[str] = None,
        max: Optional[str] = None,
        step: Optional[str] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # default, suggesting types
    @overload
    def __init__(
        self,
        *,
        type: Optional[InputTypes] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # default, allowing all arguments
    @overload
    def __init__(
        self,
        *,
        type: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
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
            'id': id,
            'name': name,
            'value': value,
            'type': type,
        }
        super().__init__(**attributes)

    # Form submission
    @overload  # type: ignore
    def __call__(
        self,
        *,
        type: Literal['submit'] = 'submit',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Text box
    @overload
    def __call__(
        self,
        *,
        type: Literal['text'] = 'text',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        spellcheck: Optional[Literal["true", "false", ""]] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # JS button
    @overload
    def __call__(
        self,
        *,
        type: Literal['button'] = 'button',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Checkbox
    @overload
    def __call__(
        self,
        *,
        type: Literal['checkbox'] = 'checkbox',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        checked: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Email address
    @overload
    def __call__(
        self,
        *,
        type: Literal['email'] = 'email',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # File upload
    @overload
    def __call__(
        self,
        *,
        type: Literal['file'] = 'file',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        required: Optional[bool] = None,
        accept: Optional[str] = None,
        multiple: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Number
    @overload
    def __call__(
        self,
        *,
        type: Literal['number'] = 'number',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        required: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        min: Optional[str] = None,
        max: Optional[str] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Password
    @overload
    def __call__(
        self,
        *,
        type: Literal['password'] = 'password',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        placeholder: Optional[str] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Radio button
    @overload
    def __call__(
        self,
        *,
        type: Literal['radio'] = 'radio',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        checked: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # Range
    @overload
    def __call__(
        self,
        *,
        type: Literal['range'] = 'range',
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        required: Optional[bool] = None,
        min: Optional[str] = None,
        max: Optional[str] = None,
        step: Optional[str] = None,
        placeholder: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # default, suggesting types
    @overload
    def __call__(
        self,
        *,
        type: Optional[InputTypes] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    # default, allowing all arguments
    @overload
    def __call__(
        self,
        *,
        type: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        autofocus: Optional[bool] = None,
        **attributes: AttributeType,
    ) -> None:
        ...

    def __call__(  # type: ignore
        self,
        *,
        type: Optional[str] = None,
        id: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
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
            'id': id,
            'name': name,
            'value': value,
            'type': type,
        }
        return super().__call__(**attributes)

    def _get_default_attributes(
        self,
        given: dict[str, AttributeType],
    ) -> dict[str, AttributeType]:
        if (
            given.get('formaction') is not None
            and given.get('formmethod') is None
        ):
            formmethod = 'POST'
        else:
            formmethod = None
        return {
            'type': None,
            'name': None,
            'value': None,
            'placeholder': None,
            'readonly': False,
            'required': False,
            'formmethod': formmethod,
            'formaction': None,
        }
