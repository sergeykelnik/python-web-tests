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

    @pytest.mark.parametrize(
        "search_query",
        [
            "StarCraft II",
            "Counter Strike"
        ],
    )
    def test_search_game_and_select_streamer(self, driver: WebDriver, search_query: str):
        """
        Test the complete flow:
        1. Go to Twitch
        2. Accept cookies if present
        3. Click on the search icon
        4. Input search query
        5. Scroll down 2 times
        6. Select one streamer
        7. Make sure the video player is visible
        8. Make a screenshot of the final state
        """
        home_page = HomePage(driver)
        home_page.open()

        home_page.accept_cookies_if_present()

        search_page = home_page.click_search_icon()

        search_page.search_for(search_query)

        search_page.click_channels_tab()

        assert search_page.is_search_result_visible()

        search_page.swipe(max_scrolls=2, pause=1)

        streamer_page = search_page.select_streamer_by_index(3)

        assert streamer_page.is_video_player_visible()
        streamer_page.take_screenshot(f"PASS_test_search_game_and_select_streamer['{search_query}']", 1)
