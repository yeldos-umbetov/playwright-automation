from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # signup locators
        self.signup_header = page.get_by_role("heading", name = "New User Signup")
        self.signup_name_input = page.get_by_placeholder("Name")
        self.signup_email_input = page.locator(".signup-form input[name='email']")
        self.signup_button = page.get_by_role("button", name = "Signup")
        # login locators
        self.login_header = page.get_by_role("heading", name = "Login to your account")
        self.login_email_input = page.get_by_test_id("login-email")
        self.login_password_input = page.get_by_test_id("login-password")
        self.login_button = page.get_by_role("button", name = "Login")

        self.invalid_login_text = page.get_by_text("Your email or password is incorrect!")
    def submit_initial_signup(self, name: str, email: str):
        self.signup_name_input.fill(name)
        self.signup_email_input.fill(email)
        self.signup_button.click()

    def login(self, email: str, password: str):
        self.login_email_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()

