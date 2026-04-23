import re

import pytest
from playwright.sync_api import expect

from data.Users import Users
from pages.LoginPage import LoginPage


@pytest.mark.parametrize(
    "user",
    [
        Users.WRONG_USERNAME,
        Users.WRONG_PASSWORD,
        Users.EMPTY_USERNAME,
        Users.EMPTY_PASSWORD,
        Users.LOCKED,
    ],
    ids=[
        "wrong username",
        "wrong password",
        "empty username",
        "empty password",
        "locked user",
    ]
)
def test_login_invalid(page, user):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(user)

    expect(login_page.error_message).to_be_visible()

def test_login_success(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(Users.VALID)

    expect(page).to_have_url(re.compile(r".*inventory.*"))