from playwright.sync_api import Page

class BasePage(Page):
    def __init__(self, page: Page):
        self.page = page

    def get_page_title(self) -> str:
        return self.page.title()

