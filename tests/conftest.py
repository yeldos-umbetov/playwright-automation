import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext
from pages.home_page import HomePage
from utils.data_models import AddressData, UserData

@pytest.fixture
def home_page(page: Page) -> HomePage:
    home = HomePage(page)
    home.load()
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
        "firstname": random_address.first_name,
        "lastname": random_address.last_name,
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
        form=payload
    )
    response_json = response.json()

    assert response_json.get("responseCode") == 201, f"failed to register user: {response_json}"
    yield user
    api_request_context.dispose()

@pytest.fixture(scope="session", autouse=True)
def configure_test_id_attribute(playwright: Playwright):
    playwright.selectors.set_test_id_attribute("data-qa")
