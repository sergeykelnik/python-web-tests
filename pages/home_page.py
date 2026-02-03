"""
Twitch Home Page Object.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config.config import Config
from pages.base_page import BasePage
from pages.search_page import SearchPage


class HomePage(BasePage):
    """Page Object for Twitch Home Page."""

    # Locators
    SEARCH_BUTTON = (By.XPATH, "(//div[contains(text(),'Browse')])[1]") #Text-related locators should be handled during l8n testing
    ACCEPT_COOKIES = (By.XPATH, "(//button[@data-a-target='consent-banner-accept'])[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.url = Config.BASE_URL

    def open(self) -> "HomePage":
        """Navigate to Twitch home page and wait for it to fully load."""
        self.navigate_to(self.url)
        return self

    def accept_cookies_if_present(self) -> "HomePage":
        """Accept cookies if the banner is present."""
        self.click(self.ACCEPT_COOKIES)
        return self

    def click_search_icon(self) -> "SearchPage":
        """Click on the search icon to open the search."""
        self.click(self.SEARCH_BUTTON)
        return SearchPage(self.driver)
