import re

import pytest
from playwright.sync_api import expect

from data.LoginCases import LOGIN_CASES
from data.Users import Users
from pages.LoginPage import LoginPage
from utils.helpers import assert_error_message


@pytest.mark.parametrize(
    "case",
    LOGIN_CASES,
    ids=[case.name for case in LOGIN_CASES]
)
def test_login_form_validation(page, case):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(case.user)

    if case.should_pass:
        expect(page).to_have_url(re.compile(r".*inventory.*"))
    else:
        assert_error_message(login_page.error_message, case.error_message)


def test_login_form_error_button_close(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(Users.WRONG_USERNAME)

    expect(login_page.error_button).to_be_visible()

    login_page.error_button.click()
    expect(login_page.error_message).not_to_be_visible()
