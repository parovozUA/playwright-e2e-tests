import allure

from pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.get_by_test_id("inventory-item")
        self.checkout_button = page.get_by_test_id("checkout")

    def is_item_present(self):
        return self.cart_items.count() > 0

    def click_checkout(self):
        with allure.step("Click checkout button"):
            self.checkout_button.click()