from pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def is_item_present(self):
        return self.cart_items.count() > 0