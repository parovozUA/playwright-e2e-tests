import allure
import pytest
from playwright.sync_api import expect

from pages.InventoryPage import InventoryPage, SortValue
from utils.constants import NON_EMPTY_TEXT


@allure.suite("Inventory")
@allure.feature("Inventory")
class TestInventory:

    @allure.story("User can see inventory items")
    @allure.title("Test user can see inventory items")
    @allure.description("Verifies that the user can see the inventory items on the page.")
    def test_inventory_page_open(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.open()

        with allure.step("Verify inventory page is visible"):
            expect(inventory_page.inventory_list).to_be_visible()

    @allure.story("Constant items load")
    @allure.title("Test inventory items load")
    @allure.description("Verifies that the inventory items desired count are loaded on the page.")
    def test_inventory_items_load(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.open()

        with allure.step("Verify inventory items count"):
            expect(inventory_page.items).to_have_count(InventoryPage.ITEMS_COUNT)

    @allure.story("Items have names")
    @allure.title("Test inventory items have names")
    @allure.description("Verifies that the inventory items have names")
    def test_all_inventory_items_have_names(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.open()

        with allure.step("Verify inventory items names"):
            expect(inventory_page.item_name_texts).to_have_text([NON_EMPTY_TEXT] * inventory_page.ITEMS_COUNT)

    @allure.story("Items have prices")
    @allure.title("Test inventory items have prices")
    @allure.description("Verifies that the inventory items have prices")
    def test_all_inventory_items_have_prices(self, logged_in_page):
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.open()

        with allure.step("Verify inventory items prices"):
            expect(inventory_page.item_price_texts).to_have_text([NON_EMPTY_TEXT] * inventory_page.ITEMS_COUNT)

    @allure.title("Test inventory items can be sorted")
    @allure.description("Verifies that the inventory items can be sorted by name and price")
    @pytest.mark.parametrize(
        "sort_value, get_items, reverse",
        [
            (SortValue.NAME_ASC, InventoryPage.get_item_names, False),
            (SortValue.NAME_DESC, InventoryPage.get_item_names, True),
            (SortValue.PRICE_ASC, InventoryPage.get_item_prices, False),
            (SortValue.PRICE_DESC, InventoryPage.get_item_prices, True),
        ],
        ids=["Names ascending", "Names descending", "Prices ascending", "Prices descending"],
    )
    def test_inventory_items_sorting(self, logged_in_page, sort_value, get_items, reverse):
        allure.dynamic.parameter("get_items", "hidden")
        allure.dynamic.title(f"Test inventory items sorting by {sort_value.name}")
        inventory_page = InventoryPage(logged_in_page)
        inventory_page.open()

        inventory_page.sort_items(sort_by=sort_value)
        values = get_items(inventory_page)

        with allure.step(f"Verify inventory items sorted by {sort_value.name}"):
            assert values == sorted(values, reverse=reverse)
