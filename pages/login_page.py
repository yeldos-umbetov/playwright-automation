from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_header = page.get_by_role("headning", name = "New User Signup")