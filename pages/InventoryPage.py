from enum import Enum

import allure

from pages.BasePage import BasePage

class SortValue(str, Enum):
    PRICE_ASC = "lohi"
    PRICE_DESC = "hilo"
    NAME_ASC = "az"
    NAME_DESC = "za"

class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    ITEMS_COUNT = 6 # According to current application behavior, inventory contains 6 items

    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = page.get_by_test_id("inventory-list")
        self.items = self.inventory_list.get_by_test_id("inventory-item")

        # price and name
        self.item_name_texts = self.items.get_by_test_id("inventory-item-name")
        self.item_price_texts = self.items.get_by_test_id("inventory-item-price")

        # backpack buttons
        self.add_to_cart_backpack_button = page.get_by_test_id("add-to-cart-sauce-labs-backpack")
        self.remove_from_cart_backpack_button = page.get_by_test_id("remove-sauce-labs-backpack")

        # sorting
        self.sort_dropdown = page.get_by_test_id("product-sort-container")

        self.cart_icon = page.get_by_test_id("shopping-cart-link")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")

    def open(self):
        with allure.step("Open inventory page"):
            self.page.goto(self.URL)

    def get_url(self):
        return self.page.url

    def sort_items(self, sort_by: SortValue):
        with allure.step(f"Sort items by {sort_by}"):
            self.sort_dropdown.select_option(value=sort_by)

    # ------------- Cart actions -------------
    def add_item_to_cart(self):
        with allure.step("Add item to cart"):
            self.add_to_cart_backpack_button.click()

    def open_cart(self):
        with allure.step("Open cart"):
            self.cart_icon.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()


    def get_item_prices(self) -> list[float]:
        return [float(x.replace("$", "").strip())
                for x in self.item_price_texts.all_inner_texts()]

    def get_item_names(self) -> list[str]:
        return [x.strip() for x in self.item_name_texts.all_inner_texts()]