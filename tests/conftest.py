import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext
from pages.home_page import HomePage
from utils.data_models import AddressData, UserData

@pytest.fixture
def home_page(page: Page) -> HomePage:
    home = HomePage(page)
    home.navigate_to("https://automationexercise.com")
    return home

@pytest.fixture
def random_address() -> AddressData:
    return AddressData.generate()


@pytest.fixture
def registered_user(playwright: Playwright, random_address: AddressData) -> UserData:
    """ registers the fresh user before the test run """
    api_request_context: APIRequestContext() = playwright.request.new_context()

    user = UserData.generate()

    payload = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "title": "Mr",
        "birth_date": "15",
        "birth_month": "Jan",
        "birth_year": "1997",
        "first_name": random_address.first_name,
        "last_name": random_address.last_name,
        "company": random_address.company,
        "address1": random_address.address1,
        "address2": random_address.address2,
        "country": random_address.country,
        "zipcode": random_address.zipcode,
        "state": random_address.state,
        "city": random_address.city,
        "mobile_number": random_address.mobile
    }

    response = api_request_context.post(
        "https://automationexercise.com/api/createAccount",
        data=payload
    )
    assert response.status == 201 or response.ok, f"failed to register user: {response.text}"
    yield user
    api_request_context.dispose()

