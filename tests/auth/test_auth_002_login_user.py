import pytest
import time
from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage

"""
Jira ticket QA-102
scenario description: logging in, then deleting that user
"""

@pytest.mark.jira("QA-102")
def test_login_user(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.navigate_to("https://automationexercise.com")
    expect(home_page.features_items_header).to_be_visible()