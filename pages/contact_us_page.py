from playwright.sync_api import Page
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.get_in_touch_text =  page.get_by_role("heading", name="Get In Touch")

