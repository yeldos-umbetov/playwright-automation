import pytest
import time
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_status_page import AccountStatusPage

"""
Jira ticket QA-101
scenario description: signing up a user by entering all the necessary information, then deleting that user
"""

@pytest.mark.jira("QA-101")
def test_register_user(page: Page):
    # initializing page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    status_page = AccountStatusPage(page)

    # generating unique user data
    unique_timestamp = int(time.time())
    username = f"AutomationUser_{unique_timestamp}"
    user_email = f"qa_engineer_{unique_timestamp}@testlabs.com"

    home_page.navigate_to("https://automationexercise.com")
    assert home_page.is_visible(), "Failure: Homepage canvas is not visible"
    home_page.click_login_signup()
