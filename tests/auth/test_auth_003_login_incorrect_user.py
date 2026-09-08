import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_models import UserData
"""
JIRA Ticket #103
logging in with incorrect login and password
"""

def test_login_with_incorrect_login_password(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    invalid_user = UserData.generate()
    home_page.navigate_to("https://automationexercise.com")
    expect(home_page.slider_carousel).to_be_visible()
    home_page.click_login_signup()
    expect(login_page.login_header).to_be_visible()
    login_page.login(email=invalid_user.email, password=invalid_user.password)
    expect(login_page.invalid_login_text).to_be_visible()