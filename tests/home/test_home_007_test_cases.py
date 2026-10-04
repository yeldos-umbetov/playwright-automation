import pytest
from playwright.sync_api import expect, Page

from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage

@pytest.mark.jira("QA-107")
def test_test_cases_page(page: Page):
    home_page = HomePage(page)
    test_cases_page = TestCasesPage(page)

    home_page.load()
    expect(home_page.slider_carousel).to_be_visible()
    home_page.test_cases_link.click()
    expect(test_cases_page.page_header).to_be_visible()
