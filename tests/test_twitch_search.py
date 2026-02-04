"""Test cases for Twitch search functionality."""
import logging

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.mobile
class TestTwitchSearch:
    """Twitch search tests with mobile emulation."""

    @pytest.mark.parametrize(
        "search_query",
        [
            "StarCraft II",
            "Counter Strike"
        ],
    )
    def test_search_game_and_select_streamer(self, driver: WebDriver, search_query: str):
        """Test search game, select streamer, and verify video player."""
        logger.info(f"Starting test with search query: '{search_query}'")

        logger.info("Opening Twitch home page")
        home_page = HomePage(driver)
        home_page.open()

        logger.info("Accepting cookies if present")
        home_page.accept_cookies_if_present()

        logger.info("Clicking search icon")
        search_page = home_page.click_search_icon()

        logger.info(f"Searching for: '{search_query}'")
        search_page.search_for(search_query)

        logger.info("Clicking Channels tab")
        search_page.click_channels_tab()

        logger.info("Verifying search results are visible")
        assert search_page.is_search_result_visible()

        logger.info("Scrolling down 2 times")
        search_page.swipe(max_scrolls=2, pause=1)

        logger.info("Selecting streamer at index 3")
        streamer_page = search_page.select_streamer_by_index(2)

        logger.info("Verifying video player is visible")
        assert streamer_page.is_video_player_visible()

        logger.info("Taking screenshot of final state")
        streamer_page.take_screenshot(f"PASS_test_search_game_and_select_streamer['{search_query}']", 1)

        logger.info(f"Test completed successfully for: '{search_query}'")
