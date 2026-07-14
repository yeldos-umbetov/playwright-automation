from playwright.sync_api import Page
from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.account_info_header = page.get_by_text("Enter Account Information")
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.mr_radio = page.locator("#id_gender1")
        self.password_input = page.locator("#password")
        self.days_select = page.locator("#days")
        self.month_select = page.locator("#months")
        self.year_select = page.locator("#years")

        # address details locators
        self.first_name_input = page.locator("#first_name")
        self.last_name_input = page.locator("#last_name")
        self.company_input = page.locator("#company")
        self.address1_input = page.locator("#address1")
        self.address2_input = page.locator("#address2")
        self.country_input = page.locator("#country")
        self.state_input = page.locator("#state")
        self.city_input = page.locator("#city")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_input = page.locator("#mobile_number")

        self.create_account_btn = page.get_by_role("button", name="Create Account")

    def is_account_info_header_visible(self) -> bool:
        return self.account_info_header.is_visible()

    def opt_in_marketing(self):
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()

    def fill_account_details(self, password: str, day: str, month: str, year: str):
        self.mr_radio.click()
        self.password_input.fill(password)
        self.days_select.select_option(day)
        self.month_select.select_option(month)
        self.year_select.select_option(year)

    def fill_address_details(self, details: dict):
        self.first_name_input.fill(details["first_name"])
        self.last_name_input.fill(details["last_name"])
        self.company_input.fill(details["company"])
        self.address1_input.fill(details["address1"])
        self.address2_input.fill(details["address2"])
        self.country_input.select_option(details["country"])
        self.state_input.fill(details["state"])
        self.city_input.fill(details["city"])
        self.zipcode_input.fill(details["zipcode"])
        self.mobile_input.fill(details["mobile"])

    def click_create_account(self):
        self.create_account_btn.click()
