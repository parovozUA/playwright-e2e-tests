import re

import pytest
from playwright.sync_api import expect

from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage


@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "secret_sauce"),
        ("standard_user", "wrong_pass"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
    ids=[
        "wrong username",
        "wrong password",
        "empty username",
        "empty password",
    ]
)
def test_login_invalid(page, username, password):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(re.compile(r".*inventory.*"))

def test_inventory_loaded(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    inventory_page.assert_loaded()