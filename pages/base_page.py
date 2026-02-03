"""Base Page with common methods for all page objects."""
import time
from typing import Tuple, List

from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import Helpers


class BasePage:
    """Base class for all Page Objects."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate_to(self, url: str) -> None:
        """Navigate to URL."""
        self.driver.get(url)

    def find_element(self, locator: Tuple[str, str], timeout: int = 5) -> WebElement:
        """Find element with explicit wait."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator: Tuple[str, str], timeout: int = 5) -> List[WebElement]:
        """Find multiple elements."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator: Tuple[str, str], timeout: int = 5) -> None:
        """Click element."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        self.click_element(element)

    @Helpers.highlight_element()
    def click_element(self, element: WebElement) -> None:
        """Click WebElement with highlighting."""
        element.click()

    def type(self, locator: Tuple[str, str], text: str, clear_first: bool = True) -> None:
        """Type text into input field."""
        element = self.find_element(locator)
        self.type_on_element(element, text, clear_first)

    @Helpers.highlight_element()
    def type_on_element(self, element: WebElement, text: str, clear_first: bool = True) -> None:
        """Type text on element with highlighting."""
        if clear_first:
            element.clear()
        element.send_keys(text)

    def is_element_visible(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is clickable."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_element_not_visible(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        """Check if element is not visible."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def swipe(self, max_scrolls: int = 3, pause: float = 0.5) -> None:
        """Scroll down the page."""
        import time

        for _ in range(max_scrolls):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(pause)

    def take_screenshot(self, name: str, timeout: int = 1) -> str:
        """Take screenshot of current page."""
        time.sleep(timeout)
        return Helpers.take_screenshot(self.driver, name)

    def press_enter(self, locator: Tuple[str, str]) -> None:
        """Press Enter key on element."""
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)
