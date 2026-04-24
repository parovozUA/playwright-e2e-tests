import pytest
from playwright.sync_api import expect

from data.cases.checkout_cases import CHECKOUT_CASES, CheckoutCase
from data.test_data.CheckoutForms import CheckoutForms
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from utils.helpers import assert_error_message


@pytest.mark.parametrize(
    "case",
    CHECKOUT_CASES
)
def test_checkout_form_validation(logged_in_page, case: CheckoutCase):
    if case.xfail_reason:
        pytest.xfail(case.xfail_reason)

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

    checkout_page.fill_checkout_form(case.form)
    checkout_page.continue_button.click()

    if case.should_pass:
        expect(checkout_page.title_span).to_have_text("Checkout: Overview")
    else:
        assert_error_message(checkout_page.error_message, case.error_message)


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
    expect(checkout_page.error_message).to_be_visible()

    checkout_page.error_button.click()
    expect(checkout_page.error_message).not_to_be_visible()
