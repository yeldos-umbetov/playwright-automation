from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.slider_carousel = page.locator("#slider-carousel")
        self.features_items_header = page.get_by_role("heading", name = "AutomationExercise")

        self.login_signup_link = page.get_by_role("link", name = "Signup / Login")
        self.delete_account_link = page.get_by_role("link", name = "Delete Account")
        self.logged_in_text = page.locator("header .navbar-nav")

    def is_page_visible(self) -> bool:
        return self.slider_carousel.is_visible() and self.features_items_header.is_visible()

    def click_login_signup(self):
        self.login_signup_link.click()

    def click_delete_account(self):
        self.delete_account_link.click()

    def get_logged_in_text(self):
        return self.logged_in_text.text_content()

