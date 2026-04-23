import allure
from playwright.sync_api import expect

from pages.CartPage import CartPage
from pages.InventoryPage import InventoryPage

@allure.feature("Cart")
@allure.story("Add item")
@allure.title("User can add item to cart")
def test_add_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    with allure.step("Add item to cart"):
        inventory_page.add_item_to_cart()

    with allure.step("Verify cart badge"):
        expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    with allure.step("Verify cart items"):
        expect(cart_page.title_span).to_have_text("Your Cart")
        expect(cart_page.cart_items).to_have_count(1)