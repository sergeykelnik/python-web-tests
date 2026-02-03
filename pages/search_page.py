"""
Twitch Search Page Object.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from pages.streamer_page import StreamerPage


class SearchPage(BasePage):
    """Page Object for Twitch Search Page."""

    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search'], input[aria-label='Search Input']")
    STREAMER_AVATAR = (By.XPATH, "(//div[@role='list']/div[contains(@class,'Layout-')]"
                                 "//img[contains(@class, 'tw-image-avatar')])[1]")
    CHANNELS_TAB = (By.XPATH, "//div[contains(text(), 'Channels')]")
    SEARCH_RESULT = (By.XPATH, "(//img)[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def search_for(self, query: str) -> "SearchPage":
        """
        Perform a complete search operation.

        Args:
            query: Search term to search for
        """
        self.type(self.SEARCH_INPUT, query)
        self.press_enter(self.SEARCH_INPUT)
        return self

    def swipe(self, max_scrolls: int = 3, pause: float = 0.5) -> "SearchPage":
        """
        Scroll down the search results using mouse wheel movements.

        Args:
            max_scrolls: Number of times to scroll down (default: 3)
            pause: Pause duration in seconds between scrolls (default: 0.5)
        """
        super().swipe(max_scrolls=max_scrolls, pause=pause)
        return self

    def select_streamer(self) -> "StreamerPage":
        """
        Select a streamer from the results by index.
        """
        self.click(self.STREAMER_AVATAR)
        return StreamerPage(self.driver)

    def click_channels_tab(self) -> "SearchPage":
        """Click on the Channels tab."""
        self.click(self.CHANNELS_TAB)
        return self

    def is_search_result_visible(self) -> bool:
        return self.is_element_visible(self.SEARCH_RESULT)
