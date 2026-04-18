class BasePage:
    BASE_URL = "https://www.saucedemo.com/"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.BASE_URL)