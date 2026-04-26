import re

import allure
import pytest
from playwright.sync_api import expect

from data.cases.login_cases import LOGIN_CASES
from data.models.LoginCase import LoginCase
from data.test_data.Users import Users
from pages.LoginPage import LoginPage
from utils.helpers import assert_error_message


@allure.suite("Login")
@allure.feature("Login")
class TestLogin:

    @allure.story("Login Form Validation")
    @allure.description("Verifies that the login form validation works as expected for different cases")
    @pytest.mark.parametrize(
        "case",
        LOGIN_CASES
    )
    def test_login_form_validation(self, page, case: LoginCase):
        allure.dynamic.title(f"Test login form validation for {case.name}")

        login_page = LoginPage(page)

        login_page.open()
        login_page.login(case.user)

        if case.should_pass:
            with allure.step("Verify user is logged in"):
                expect(page).to_have_url(re.compile(r".*inventory.*"))
        else:
            assert_error_message(login_page.error_message, case.error_message)

    @allure.story("Login Form Error Message")
    @allure.title("Test login form error message can be closed")
    @allure.description(
        "When the user encounters an error message during the login process, they should be able to close the message and try again. This test verifies that the error message can be closed.")
    def test_login_form_error_button_close(self, page):
        login_page = LoginPage(page)

        login_page.open()
        login_page.login(Users.WRONG_USERNAME)

        with allure.step("Verify error message is visible"):
            expect(login_page.error_button).to_be_visible()

        login_page.click_error_button()

        with allure.step("Verify error message is closed"):
            expect(login_page.error_message).not_to_be_visible()
