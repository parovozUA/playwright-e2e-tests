import re

import pytest
from playwright.sync_api import expect

from data.Users import Users
from pages.LoginPage import LoginPage


@pytest.mark.parametrize(
    "user, should_pass",
    [
        (Users.VALID, True),
        (Users.WRONG_USERNAME, False),
        (Users.WRONG_PASSWORD, False),
        (Users.EMPTY_USERNAME, False),
        (Users.EMPTY_PASSWORD, False),
        (Users.LOCKED, False),
    ],
    ids=[
        "valid user",
        "wrong username",
        "wrong password",
        "empty username",
        "empty password",
        "locked user",
    ]
)
def test_login(page, user, should_pass):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(user)

    if should_pass:
        expect(page).to_have_url(re.compile(r".*inventory.*"))
    else:
        expect(login_page.error_message).to_be_visible()