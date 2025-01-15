from base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://example.com"

    def open(self):
        self.goto(self.url)