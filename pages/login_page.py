from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.signup_header = page.get_by_role("heading", name = "New User Signup")
        self.signup_name_input = page.get_by_placeholder("Name")
        self.signup_email_input = page.locator(".signup-form input[name='email']")
        self.signup_button = page.get_by_role("button", name = "Signup")

    def is_signup_header_visible(self) -> bool:
        return self.signup_header.is_visible()

    def submit_initial_signup(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()


