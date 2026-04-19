from playwright.sync_api import expect

from pages.InventoryPage import InventoryPage
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

