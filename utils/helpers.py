import allure
from playwright.sync_api import Locator, expect


def assert_error_message(locator: Locator, message: str):
    with allure.step(f"Assert error message: {message}"):
        expect(locator).to_be_visible()
        expect(locator).to_contain_text(message, ignore_case=True)