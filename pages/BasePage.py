class BasePage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page
        self.title = page.get_by_test_id("title")

    def open(self):
        self.page.goto(self.BASE_URL)