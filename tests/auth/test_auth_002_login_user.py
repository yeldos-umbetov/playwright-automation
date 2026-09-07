import pytest
import time
from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_status_page import AccountStatusPage
from utils.data_models import UserData
"""
Jira ticket QA-102
scenario description: logging in, then deleting that user
"""

@pytest.mark.jira("QA-102")
def test_login_user(page: Page, registered_user: UserData):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    status_page = AccountStatusPage(page)

    home_page.navigate_to("https://automationexercise.com")
    expect(home_page.features_items_header).to_be_visible()
    home_page.click_login_signup()
    expect(login_page.login_header).to_be_visible()
    login_page.login(registered_user.email, registered_user.password)
    expect(page.get_by_text(f"Logged in as {registered_user.name}")).to_be_visible()
    home_page.click_delete_account()
    expect(status_page.account_deleted_header).to_be_visible()
    status_page.click_continue_btn()
