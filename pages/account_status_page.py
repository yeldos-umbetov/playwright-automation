from playwright.sync_api import Page
from pages.base_page import BasePage

class AccountStatusPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.account_created_header = page.get_by_text("Account created!")
        self.account_deleted_header = page.get_by_text("Account deleted!")
        self.continue_btn = page.get_by_role("link", name="Continue")

    def click_continue_btn(self):
        self.continue_btn.click()
