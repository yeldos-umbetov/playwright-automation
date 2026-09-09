import pytest
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_models import UserData


def test_register_user_existing_email(page: Page, registered_user: UserData):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.load()
    expect(home_page.slider_carousel).to_be_visible()
    home_page.click_login_signup()
    expect(login_page.signup_header).to_be_visible()
    login_page.submit_initial_signup(registered_user.name, registered_user.email)
    # page.pause()
    expect(login_page.invalid_signup_text).to_be_visible()