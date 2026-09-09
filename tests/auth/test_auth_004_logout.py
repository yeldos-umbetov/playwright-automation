import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_models import UserData

"""
Jira ticket QA-104
scenario description: logging in, then logging out
"""
@pytest.mark.jira("QA-104")
def test_logout_user(page: Page, registered_user: UserData):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.load()
    expect(home_page.features_items_header).to_be_visible()
    home_page.click_login_signup()
    login_page.login(registered_user.email, registered_user.password)
    expect(page.get_by_text(f"Logged in as {registered_user.name}")).to_be_visible()
    home_page.click_logout()
    expect(login_page.login_header).to_be_visible()