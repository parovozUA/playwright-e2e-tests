from playwright.sync_api import expect

from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage


def test_add_to_cart(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_item_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()

    expect(cart_page.cart_items).to_have_count(1)