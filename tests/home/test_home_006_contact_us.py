import pytest
from playwright.sync_api import expect, Page

from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage

@pytest.mark.jira("QA-106")
def test_contact_us_form(page: Page):
    home_page = HomePage(page)
    contact_us_page = ContactUsPage(home_page)

    home_page.load()
    expect(home_page.slider_carousel).to_be_visible()
    home_page.click_contact_us_link()
    expect(contact_us_page.get_in_touch_text).to_be_visible()
