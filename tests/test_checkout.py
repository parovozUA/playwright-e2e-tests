import allure
import pytest
from playwright.sync_api import expect

from data.cases.checkout_cases import CHECKOUT_CASES, CheckoutCase
from data.test_data.CheckoutForms import CheckoutForms
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage
from utils.helpers import assert_error_message

@allure.suite("Checkout")
@allure.feature("Checkout")
@allure.story("Checkout Form Validation")
@allure.description("Verify checkout form validation for all possible cases.")
@pytest.mark.parametrize(
    "case",
    CHECKOUT_CASES
)
def test_checkout_form_validation(logged_in_page, case: CheckoutCase):
    allure.dynamic.title(f"Test checkout form validation: {case.name}")

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

    cart_page.click_checkout()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(case.form)
    checkout_page.click_continue()

    if case.should_pass:
        expect(checkout_page.title_span).to_have_text("Checkout: Overview")
    else:
        assert_error_message(checkout_page.error_message, case.error_message)

@allure.suite("Checkout")
@allure.feature("Checkout")
@allure.story("Checkout Success Flow")
@allure.title("Test checkout happy path flow")
@allure.description("In order to complete the checkout process, the user must provide valid information and proceed through the checkout steps. This test verifies that the checkout flow works as expected for a valid checkout form.")
def test_checkout_success_flow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(checkout_page.title_span).to_have_text("Your Cart")

    cart_page.click_checkout()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(CheckoutForms.VALID)
    checkout_page.click_continue()
    expect(checkout_page.title_span).to_have_text("Checkout: Overview")

    checkout_page.click_finish()
    with allure.step("Verify checkout success message"):
        expect(checkout_page.title_span).to_have_text("Checkout: Complete!")

@allure.suite("Checkout")
@allure.feature("Checkout")
@allure.story("Checkout Error Message")
@allure.title("Test checkout form error message can be closed")
@allure.description("When the user encounters an error message during the checkout process, they should be able to close the message and continue with the checkout flow. This test verifies that the error message can be closed and the checkout process can continue.")
def test_checkout_error_message_can_be_closed(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_item_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)
    expect(checkout_page.title_span).to_have_text("Your Cart")

    cart_page.click_checkout()
    expect(checkout_page.title_span).to_have_text("Checkout: Your Information")

    checkout_page.fill_checkout_form(CheckoutForms.EMPTY_FIRST_NAME)
    checkout_page.click_continue()
    expect(checkout_page.error_message).to_be_visible()

    checkout_page.click_error_button()
    with allure.step("Verify error message is closed"):
        expect(checkout_page.error_message).not_to_be_visible()
