from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.data_models import ContactUsData


class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # form input locators
        self.get_in_touch_text =  page.get_by_role("heading", name="Get In Touch")
        self.name_input = page.get_by_test_id("name")
        self.email_input = page.get_by_test_id("email")
        self.subject_input = page.get_by_test_id("subject")
        self.message_input = page.get_by_test_id("message")
        self.upload_file_input = page.locator("input[name='upload_file']")
        self.submit_btn = page.get_by_test_id("submit-button")
        self.success_text = page.get_by_text("Success! Your details have been submitted successfully.")
        self.home_link = page.get_by_role("link", name="Home")

    def fill_form(self, data: ContactUsData, file_path: str=None):
        self.name_input.fill(data.name)
        self.email_input.fill(data.email)
        self.subject_input.fill(data.subject)
        self.message_input.fill(data.message)
        if file_path:
            self.upload_file_input.set_input_files(file_path)

    def submit_form(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_btn.click()

