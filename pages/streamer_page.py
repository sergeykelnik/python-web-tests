"""
Twitch Streamer/Channel Page Object.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class StreamerPage(BasePage):
    """Page Object for Twitch Streamer/Channel Page."""

    # Locators
    VIDEO_PLAYER = (By.XPATH, "//button[@role='link']//img")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_video_player_visible(self) -> bool:
        """Check if the video player is visible."""
        return self.is_element_visible(self.VIDEO_PLAYER, timeout=10)
