import pytest
from playwright.sync_api import expect

from pages.InventoryPage import InventoryPage, SortValue
from utils.constants import NON_EMPTY_TEXT


def test_inventory_page_open(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.open()

    expect(inventory_page.inventory_list).to_be_visible()


def test_inventory_items_load(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.items).to_have_count(InventoryPage.ITEMS_COUNT)


def test_all_inventory_items_have_names(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.items).to_have_count(InventoryPage.ITEMS_COUNT)
    expect(inventory_page.item_name_texts).to_have_text([NON_EMPTY_TEXT] * inventory_page.ITEMS_COUNT)


def test_all_inventory_items_have_prices(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    expect(inventory_page.items).to_have_count(InventoryPage.ITEMS_COUNT)
    expect(inventory_page.item_price_texts).to_have_text([NON_EMPTY_TEXT] * inventory_page.ITEMS_COUNT)


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
def test_inventory_items_sorting(logged_in_page, sort_value, get_items, reverse):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_dropdown.select_option(value=sort_value)
    values = get_items(inventory_page)
    assert values == sorted(values, reverse=reverse)