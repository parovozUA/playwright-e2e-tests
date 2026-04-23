import pytest
from playwright.sync_api import expect

from data.CheckoutForm import CheckoutForms, CheckoutForm
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage


@pytest.mark.parametrize(
    "form, should_pass",
    [
        (CheckoutForms.VALID, True),
        (CheckoutForms.EMPTY_FIRST_NAME, False),
        (CheckoutForms.EMPTY_LAST_NAME, False),
        (CheckoutForms.EMPTY_POSTAL, False),
        (CheckoutForms.ALL_EMPTY, False),
        (CheckoutForms.SPACES, False),
        (CheckoutForms.LONG_VALUES, True),
    ],
    ids=[
        "valid",
        "empty first name",
        "empty last name",
        "empty postal",
        "all empty",
        "spaces only",
        "long values"
    ]
)
def test_checkout_form_validation(logged_in_page, form: CheckoutForm, should_pass: bool):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(checkout_page.title_span).to_have_text("Your Cart")

    cart_page.checkout_button.click()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(form)
    checkout_page.continue_button.click()

    if should_pass:
        expect(checkout_page.title_span).to_have_text("Checkout: Overview")
    else:
        expect(checkout_page.error_message_container).to_be_visible()

def test_checkout_successful_flow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(checkout_page.title_span).to_have_text("Your Cart")

    cart_page.checkout_button.click()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(CheckoutForms.VALID)
    checkout_page.continue_button.click()
    expect(checkout_page.title_span).to_have_text("Checkout: Overview")

    checkout_page.finish_button.click()
    expect(checkout_page.title_span).to_have_text("Checkout: Complete!")


def test_checkout_error_message_can_be_closed(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(checkout_page.title_span).to_have_text("Your Cart")

    cart_page.checkout_button.click()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(CheckoutForms.EMPTY_FIRST_NAME)
    checkout_page.continue_button.click()
    expect(checkout_page.error_message_container).to_be_visible()

    checkout_page.error_button.click()
    expect(checkout_page.error_message_container).not_to_be_visible()
