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
    assert home_page.is_page_visible(), "Failure: Homepage canvas is not visible"
    home_page.click_login_signup()
    assert login_page.is_signup_header_visible(), "Failure: Login page is not visible"
    login_page.submit_initial_signup(name=username, email=user_email)
    assert signup_page.is_account_info_header_visible(), "Failure: Signup page is not visible"
    signup_page.fill_account_details(password="SecurePass123!", day="15", month="5", year="1995")
    signup_page.opt_in_marketing()
    address_payload = {
        "first_name": "Jameson",
        "last_name": "Taylor",
        "company": "BI Group",
        "address1": "Mangilik El av. 56",
        "address2": "block c3.5",
        "country": "United States",
        "state": "Astana City",
        "city": "Astana",
        "zipcode": "010000",
        "mobile": "+77751124212"
    }
    signup_page.fill_address_details(address_payload)
    signup_page.click_create_account()
    assert status_page.verify_account_created_header(), "Failure: Account was not created"
    status_page.click_continue_btn()
    assert f"Logged in as {username}" in home_page.get_logged_in_text(), "Failure: Signup was not successful"
    home_page.click_delete_account()
    assert status_page.verify_account_deleted_header(), "Failure: Account was not deleted"
    status_page.click_continue_btn()

