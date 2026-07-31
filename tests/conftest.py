import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from utils.data_models import AddressData

@pytest.fixture
def home_page(page: Page) -> HomePage:
    home = HomePage(page)
    home.navigate_to("https://automationexercise.com")
    return home

@pytest.fixture
def random_address():
    return AddressData.generate()

