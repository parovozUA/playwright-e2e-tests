import allure
from playwright.sync_api import expect

from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage


@allure.feature("Cart")
@allure.story("User add item to cart")
@allure.title("Test user can add item to cart")
@allure.description(
    "Verifies that a user can log in with valid credentials, add 'Sauce Labs Backpack' "
    "to the cart, navigate to the cart page, and verifies the item is present."
)
def test_add_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_item_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    with allure.step("Verify cart item presence"):
        expect(cart_page.title_span).to_have_text("Your Cart")
        expect(cart_page.cart_items).to_have_count(1)
