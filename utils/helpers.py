"""
Helper functions for test automation.
"""
import os
import time
from datetime import datetime
from functools import wraps
from typing import Optional, Callable

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config.config import Config


class Helpers:
    """Collection of helper functions for test automation."""

    @staticmethod
    def take_screenshot(driver: WebDriver, name: Optional[str] = None) -> str:
        """
        Take a screenshot and save it to the screenshots directory.

        Args:
            driver: WebDriver instance
            name: Optional name for the screenshot

        Returns:
            Path to the saved screenshot
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
        filepath = os.path.join(Config.SCREENSHOT_DIR, filename)
        driver.save_screenshot(filepath)
        return filepath

    @staticmethod
    def highlight_element(border: str = '3px solid red', duration: float = 0.2):
        """
        Decorator that highlights an element with a colored border before interaction.
        Use this on methods that interact with elements (click, type, etc).

        Args:
            border: CSS border style (default: '3px solid red')
            duration: How long to show highlight in seconds (default: 0.2)

        Usage:
            @highlight_element()
            def click_element(self, element):
                element.click()

            @highlight_element(border='5px solid blue', duration=0.5)
            def type_on_element(self, element, text):
                element.send_keys(text)
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                # Check if first arg is a WebElement (direct element interaction)
                if args and isinstance(args[0], WebElement):
                    element = args[0]
                    driver = self.driver
                    # Highlight element
                    driver.execute_script(f"arguments[0].style.border='{border}'", element)
                    time.sleep(duration)

                # Execute original method
                return func(self, *args, **kwargs)

            return wrapper

        return decorator
