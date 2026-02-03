"""
WebDriver factory for creating Chrome browser instances with mobile emulation.
Uses Selenium 4's built-in Chrome driver management.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from config.config import Config
from config.devices import MobileDevices


class DriverFactory:
    """Factory class for creating Chrome WebDriver instances with mobile emulation."""

    @staticmethod
    def create_driver(
            mobile_emulation: bool = Config.MOBILE_EMULATION,
            device_name: str = Config.DEFAULT_DEVICE
    ) -> webdriver.Chrome:
        """
        Create and configure a Chrome WebDriver with optional mobile emulation.

        Args:
            mobile_emulation: Enable mobile device emulation
            device_name: Name of the mobile device to emulate (e.g., 'iPhone 12 Pro', 'Pixel 7')

        Returns:
            Configured Chrome WebDriver instance
        """
        options = ChromeOptions()
        # Basic Chrome options
        options.add_argument("--no-sandbox")

        # Mobile emulation
        if mobile_emulation:
            device_profile = MobileDevices.get_device(device_name)
            mobile_emulation_config = device_profile.to_chrome_options()
            options.add_experimental_option("mobileEmulation", mobile_emulation_config)

        # Create a driver using Selenium 4's built-in driver management
        driver = webdriver.Chrome(options=options)

        # Set timeouts
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

        return driver
