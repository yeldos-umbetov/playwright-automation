from playwright.sync_api import Page
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.slider_carousel = page.locator("#slide-carousel")
        self.features_items_header = page.get_by_role("heading")

    def is_visible(self) -> bool:
        return self.page.slider_carousel.is_visible() and self.features_items_header.is_visible()