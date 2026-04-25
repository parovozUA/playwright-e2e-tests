import allure

from data.models.CheckoutForm import CheckoutForm
from pages.BasePage import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = page.locator('#first-name')
        self.last_name_input = page.locator('#last-name')
        self.postal_code_input = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.finish_button = page.locator('#finish')
        self.back_to_home_button = page.locator('#back-to-products')

        self.error_button = page.get_by_test_id('error-button')
        self.error_message = page.get_by_test_id('error')

    def fill_first_name(self, first_name):
        with allure.step(f"Fill first name with '{first_name}'"):
            self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name):
        with allure.step(f"Fill last name with '{last_name}'"):
            self.last_name_input.fill(last_name)

    def fill_postal_code(self, postal_code):
        with allure.step(f"Fill postal code with '{postal_code}'"):
            self.postal_code_input.fill(postal_code)

    def fill_checkout_form(self, checkout_form: CheckoutForm):
        self.fill_first_name(checkout_form.first_name)
        self.fill_last_name(checkout_form.last_name)
        self.fill_postal_code(checkout_form.postal_code)

    def click_continue(self):
        with allure.step("Click continue button"):
            self.continue_button.click()

    def click_finish(self):
        with allure.step("Click finish button"):
            self.finish_button.click()

    def click_error_button(self):
        with allure.step("Click error button"):
            self.error_button.click()