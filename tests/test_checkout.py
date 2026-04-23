from playwright.sync_api import expect

from data.CheckoutForm import CheckoutForms
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InventoryPage import InventoryPage


def test_checkout(logged_in_page):
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