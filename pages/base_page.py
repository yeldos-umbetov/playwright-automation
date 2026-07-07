from playwright.sync_api import Page

class BasePage(Page):
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def get_page_title(self) -> str:
        return self.page.title()

