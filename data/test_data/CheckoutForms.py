from data.models.CheckoutForm import CheckoutForm


class CheckoutForms:
    VALID = CheckoutForm("John", "Doe", "12345")

    EMPTY_FIRST_NAME = CheckoutForm("", "Doe", "12345")
    EMPTY_LAST_NAME = CheckoutForm("John", "", "12345")
    EMPTY_POSTAL = CheckoutForm("John", "Doe", "")

    ALL_EMPTY = CheckoutForm("", "", "")

    SPACES = CheckoutForm("   ", "   ", "   ")

    LONG_VALUES = CheckoutForm(
        "J" * 100,
        "D" * 100,
        "1" * 20
    )
