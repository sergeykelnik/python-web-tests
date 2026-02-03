"""
Test cases for Twitch search functionality.
Tests run with Chrome mobile emulation.
"""
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage


@pytest.mark.smoke
@pytest.mark.mobile
class TestTwitchSearch:
    """Test suite for Twitch search functionality with mobile emulation."""

    def test_search_starcraft_and_select_streamer(self, driver: WebDriver):
        """
        Test the complete flow:
        1. Go to Twitch
        2. Accept cookies if present
        3. Click on the search icon
        4. Input "StarCraft II"
        5. Scroll down 2 times
        6. Select one streamer
        7. Make sure the video player is visible
        8. Make a screenshot of the final state
        """
        home_page = HomePage(driver)
        home_page.open()

        home_page.accept_cookies_if_present()

        search_page = home_page.click_search_icon()

        search_page.search_for("StarCraft II")

        search_page.click_channels_tab()

        search_page.swipe(max_scrolls=2, pause=3.0)

        streamer_page = search_page.select_streamer()

        assert streamer_page.is_video_player_visible()
        streamer_page.take_screenshot("test_search_starcraft_complete")
