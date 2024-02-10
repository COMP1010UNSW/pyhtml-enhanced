"""
# Pyhtml / Tags / Input

Custom definition of the `<input>` tag, to improve type safety and implement
custom behaviour.
"""
from ..__tag_base import SelfClosingTag
from ..__types import AttributeType
from typing import Optional, Any


class input(SelfClosingTag):
    """
    Used to create interactive controls for web-based forms to accept data from
    the user; a wide variety of types of input data and control widgets are
    available, depending on the device and user agent. The `<input>` element is
    one of the most powerful and complex in all of HTML due to the sheer number
    of combinations of input types and attributes.

    * `type`: Kind of input control to use (checkbox, radio, date, password,
      text, etc)
    * `name`: Name of the field. Submitted with the form as part of a
      name/value pair
    * `value`: Initial value of the control
    * `placeholder`: Placeholder text to use for text inputs. If the field is
      empty, the placeholder is shown.
    * `readonly`: Include if field is read-only (defaults to `False`)
    * `required`: Include if field is required (defaults to `False`)
    * `formmethod`: The HTTP request method to use on click if this input is a
      submit button. Generally, it is preferred to set the `method` attribute
      on the `<form>` element instead of this.
    * `formaction`: The URL to request to on click if this input is a submit
      button. Generally, it is preferred to set the `action` attribute on the
      `<form>` element instead of this.

    [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
    """
    def __init__(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        formmethod: Optional[str] = None,
        formaction: Optional[str] = None,
        **attributes: AttributeType,
    ) -> None:
        """
        Used to create interactive controls for web-based forms to accept data
        from the user; a wide variety of types of input data and control
        widgets are available, depending on the device and user agent. The
        `<input>` element is one of the most powerful and complex in all of
        HTML due to the sheer number of combinations of input types and
        attributes.

        * `type`: Kind of input control to use (checkbox, radio, date,
          password, text, etc)
        * `name`: Name of the field. Submitted with the form as part of a
          name/value pair
        * `value`: Initial value of the control
        * `placeholder`: Placeholder text to use for text inputs. If the field
          is empty, the placeholder is shown.
        * `readonly`: Include if field is read-only (defaults to `False`)
        * `required`: Include if field is required (defaults to `False`)
        * `formmethod`: The HTTP request method to use on click if this input
          is a submit button. Generally, it is preferred to set the `method`
          attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click if this input is a
          submit button. Generally, it is preferred to set the `action`
          attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            'type': type,
            'name': name,
            'value': value,
            'placeholder': placeholder,
            'readonly': readonly,
            'required': required,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        super().__init__(**attributes)

    def __call__(  # type: ignore
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        readonly: Optional[bool] = None,
        required: Optional[bool] = None,
        formmethod: Optional[str] = None,
        formaction: Optional[str] = None,
        **attributes: AttributeType,
    ):
        """
        Used to create interactive controls for web-based forms to accept data
        from the user; a wide variety of types of input data and control
        widgets are available, depending on the device and user agent. The
        `<input>` element is one of the most powerful and complex in all of
        HTML due to the sheer number of combinations of input types and
        attributes.

        * `type`: Kind of input control to use (checkbox, radio, date,
          password, text, etc)
        * `name`: Name of the field. Submitted with the form as part of a
          name/value pair
        * `value`: Initial value of the control
        * `placeholder`: Placeholder text to use for text inputs. If the field
          is empty, the placeholder is shown.
        * `readonly`: Include if field is read-only (defaults to `False`)
        * `required`: Include if field is required (defaults to `False`)
        * `formmethod`: The HTTP request method to use on click if this input
          is a submit button. Generally, it is preferred to set the `method`
          attribute on the `<form>` element instead of this.
        * `formaction`: The URL to request to on click if this input is a
          submit button. Generally, it is preferred to set the `action`
          attribute on the `<form>` element instead of this.

        [View full documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)
        """
        attributes |= {
            'type': type,
            'name': name,
            'value': value,
            'placeholder': placeholder,
            'readonly': readonly,
            'required': required,
            'formmethod': formmethod,
            'formaction': formaction,
        }
        return super().__call__(**attributes)

    def _get_default_attributes(self, given: dict[str, Any]) -> dict[str, Any]:
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
