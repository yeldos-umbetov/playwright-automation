import pytest
import time
from playwright.sync_api import Page
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.account_status_page import AccountStatusPage
from utils.data_models import AddressData

"""
Jira ticket QA-101
scenario description: signing up a user by entering all the necessary information, then deleting that user
"""

@pytest.mark.jira("QA-101")
def test_register_user(page: Page, random_address: AddressData):
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
    expect(home_page.slider_carousel).to_be_visible(timeout=5000)
    expect(home_page.features_items_header).to_be_visible(timeout=5000)
    home_page.click_login_signup()
    expect(login_page.signup_header).to_be_visible(timeout=5000)
    login_page.submit_initial_signup(name=username, email=user_email)
    expect(signup_page.account_info_header).to_be_visible(timeout=5000)
    signup_page.fill_account_details(password="SecurePass123!", day="15", month="5", year="1995")
    signup_page.opt_in_marketing()
    signup_page.fill_address_details(random_address.to_dict())
    signup_page.click_create_account()
    expect(status_page.account_created_header).to_be_visible()
    status_page.click_continue_btn()
    assert f"Logged in as {username}" in home_page.get_logged_in_text(), "Failure: Signup was not successful"
    home_page.click_delete_account()
    expect(status_page.account_deleted_header).to_be_visible()
    status_page.click_continue_btn()

