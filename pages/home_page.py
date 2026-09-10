from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.slider_carousel = page.locator("#slider-carousel")
        self.features_items_header = page.get_by_role("heading", name = "AutomationExercise")

        self.login_signup_link = page.get_by_role("link", name = "Signup / Login")
        self.delete_account_link = page.get_by_role("link", name = "Delete Account")
        self.logout_link = page.get_by_role("link", name = "Logout")
        self.contact_us_link = page.get_by_role("link", name = "Contact Us")
        self.logged_in_text = page.locator("header .navbar-nav")

    def click_login_signup(self):
        self.login_signup_link.click()

    def click_delete_account(self):
        self.delete_account_link.click()

    def get_logged_in_text(self):
        return self.logged_in_text.text_content()

    def click_logout(self):
        self.logout_link.click()

    def load(self):
        self.page.goto("/")

    def click_contact_us_link(self):
        self.contact_us_link.click()