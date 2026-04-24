from data.models.User import User
from pages.BasePage import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_button = page.get_by_test_id("error-button")
        self.error_message = page.get_by_test_id("error")

    def open(self): self.page.goto(self.URL)

    def login(self, user: User):
        self.username_input.fill(user.username)
        self.password_input.fill(user.password)
        self.login_button.click()
