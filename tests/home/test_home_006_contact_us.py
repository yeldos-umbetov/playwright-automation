import pytest
from playwright.sync_api import expect, Page

from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from utils.data_models import ContactUsData
from pathlib import Path


@pytest.mark.jira("QA-106")
def test_contact_us_form(page: Page, contact_data: ContactUsData, sample_upload_file: Path):
    home_page = HomePage(page)
    contact_us_page = ContactUsPage(page)

    home_page.load()
    expect(home_page.slider_carousel).to_be_visible()
    home_page.click_contact_us_link()
    expect(contact_us_page.get_in_touch_text).to_be_visible()
    contact_us_page.fill_form(contact_data, file_path=str(sample_upload_file))
    contact_us_page.submit_form()
    expect(contact_us_page.success_text).to_be_visible()
    contact_us_page.home_link.click()
    expect(home_page.slider_carousel).to_be_visible()
