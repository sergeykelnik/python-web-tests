"""Helper functions for test automation."""
import os
import time
from datetime import datetime
from functools import wraps
from typing import Optional, Callable

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from config.config import Config


class Helpers:
    """Test automation helpers."""

    @staticmethod
    def take_screenshot(driver: WebDriver, name: Optional[str] = None) -> str:
        """Take screenshot and save to screenshots directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png" if name else f"screenshot_{timestamp}.png"
        filepath = os.path.join(Config.SCREENSHOT_DIR, filename)
        driver.save_screenshot(filepath)
        return filepath

    @staticmethod
    def highlight_element(border: str = '3px solid red', duration: float = 0.2):
        """Decorator to highlight element before interaction."""

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if args and isinstance(args[0], WebElement):
                    element = args[0]
                    driver = self.driver
                    driver.execute_script(f"arguments[0].style.border='{border}'", element)
                    time.sleep(duration)

                return func(self, *args, **kwargs)

            return wrapper

        return decorator
