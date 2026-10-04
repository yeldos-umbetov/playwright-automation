from playwright.sync_api import Page
from pages.base_page import BasePage


class TestCasesPage(BasePage):
    __test__ = False
    def __init__(self, page):
        super().__init__(page)

        self.page_header = page.get_by_role("heading", name="Test Cases", level=2)
