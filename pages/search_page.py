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
    CHANNELS_TAB = (By.XPATH, "//div[contains(text(), 'Channels')]")
    SEARCH_RESULT = (By.XPATH, "(//img)[1]")
    SEARCH_RESULT_BY_INDEX = "(//img)[{index}]"
    START_WATCHING_BUTTON = (By.XPATH, "//div[contains(text(),'Start Watching')]")
    STREAMER_AVATAR = (By.XPATH, "//img[contains(@class, 'tw-image-avatar')]")
    STREAMER_AVATAR_POPUP = (By.XPATH, "(//img[contains(@class, 'tw-image-avatar')])[2]")

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

    def select_streamer_by_index(self, index: int = 1) -> "StreamerPage":
        """
        Select a streamer from the results by 1-based index.

        Args:
            index: The 1-based index of the streamer to select.
        """
        if index < 1:
            raise ValueError("index must be a positive integer")
        locator = (By.XPATH, self.SEARCH_RESULT_BY_INDEX.format(index=index))
        self.click(locator)
        if self.is_element_visible(self.START_WATCHING_BUTTON):
            self.click(self.START_WATCHING_BUTTON)
        self.click(self.STREAMER_AVATAR)
        self.click(self.STREAMER_AVATAR_POPUP)
        return StreamerPage(self.driver)

    def click_channels_tab(self) -> "SearchPage":
        """Click on the Channels tab."""
        self.click(self.CHANNELS_TAB)
        return self

    def is_search_result_visible(self) -> bool:
        return self.is_element_visible(self.SEARCH_RESULT)
