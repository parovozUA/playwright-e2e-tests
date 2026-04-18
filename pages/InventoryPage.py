from playwright.sync_api import expect

from pages.BasePage import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = page.locator(".inventory_list")
        self.title = page.locator(".title")

        # новый элемент
        self.add_to_cart_button = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def open(self): self.page.goto(self.URL)

    def get_url(self):
        return self.page.url

    def assert_loaded(self):
        return expect(self.inventory_list).to_be_visible()

    def add_item_to_cart(self):
        self.add_to_cart_button.click()

    def open_cart(self):
        self.cart_icon.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()