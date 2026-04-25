import allure
import pytest

from data.test_data.Users import Users
from pages.LoginPage import LoginPage


@pytest.fixture
@allure.title("Login with valid user")
def logged_in_page(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(Users.VALID)
    return page
