import re

import pytest
from playwright.sync_api import expect

from data.LoginCases import LOGIN_CASES
from pages.LoginPage import LoginPage


@pytest.mark.parametrize(
    "case",
    LOGIN_CASES,
    ids=[
        "valid user",
        "wrong username",
        "wrong password",
        "empty username",
        "empty password",
        "locked user",
    ]
)
def test_login(page, case):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(case.user)

    if case.should_pass:
        expect(page).to_have_url(re.compile(r".*inventory.*"))
    else:
        login_page.assert_error_message(case.error_message)