from data.models.CheckoutCase import CheckoutCase
from data.test_data.CheckoutForms import CheckoutForms

CHECKOUT_CASES = [
    CheckoutCase(
        name="valid form",
        form=CheckoutForms.VALID,
        should_pass=True
    ),
    CheckoutCase(
        name="empty first name",
        form=CheckoutForms.EMPTY_FIRST_NAME,
        should_pass=False,
        error_message="First name is required"
    ),
    CheckoutCase(
        name="empty last name",
        form=CheckoutForms.EMPTY_LAST_NAME,
        should_pass=False,
        error_message="Last name is required"
    ),
    CheckoutCase(
        name="empty postal code",
        form=CheckoutForms.EMPTY_POSTAL,
        should_pass=False,
        error_message="Postal code is required"
    ),
    CheckoutCase(
        name="all fields empty",
        form=CheckoutForms.ALL_EMPTY,
        should_pass=False,
        error_message="First Name is required"
    ),
    CheckoutCase(
        name="all fields spaces",
        form=CheckoutForms.SPACES,
        should_pass=False,
        error_message="All fields are required",
        xfail_reason="Form does not trim spaces",
    ),
    CheckoutCase(
        name="long values",
        form=CheckoutForms.LONG_VALUES,
        should_pass=False,
        error_message="too long",
        xfail_reason="Form does not validate long values",
    ),
]
