from dataclasses import dataclass

from data.CheckoutForm import CheckoutForm, CheckoutForms


@dataclass
class CheckoutCase:
    name: str
    form: CheckoutForm
    should_pass: bool
    error_message: str | None = None
    xfail_reason: str | None = None


CHECKOUT_CASES = [
    CheckoutCase("valid form", CheckoutForms.VALID, True),
    CheckoutCase("empty first name", CheckoutForms.EMPTY_FIRST_NAME, False, "First name is required"),
    CheckoutCase("empty last name", CheckoutForms.EMPTY_LAST_NAME, False, "Last name is required"),
    CheckoutCase("empty postal code", CheckoutForms.EMPTY_POSTAL, False, "Postal code is required"),
    CheckoutCase("all fields empty", CheckoutForms.ALL_EMPTY, False, "First Name is required"),
    CheckoutCase("all fields spaces", CheckoutForms.SPACES, False, "All fields are required", "Form does not trim spaces"),
    CheckoutCase("long values", CheckoutForms.LONG_VALUES, False, "too long", "Form does not validate long values"),
]
