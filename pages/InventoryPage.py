from playwright.sync_api import expect

from pages.BasePage import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = page.locator(".inventory_list")
        self.title = page.locator(".title")

    def assert_loaded(self):
        expect(self.inventory_list).to_be_visible()