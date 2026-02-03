"""WebDriver factory for Chrome with mobile emulation."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from config.config import Config
from config.devices import MobileDevices


class DriverFactory:
    """Factory for creating Chrome WebDriver with mobile emulation."""

    @staticmethod
    def create_driver(
            mobile_emulation: bool = Config.MOBILE_EMULATION,
            device_name: str = Config.DEFAULT_DEVICE
    ) -> webdriver.Chrome:
        """Create configured Chrome WebDriver with optional mobile emulation."""
        options = ChromeOptions()
        options.add_argument("--no-sandbox")

        if mobile_emulation:
            device_profile = MobileDevices.get_device(device_name)
            mobile_emulation_config = device_profile.to_chrome_options()
            options.add_experimental_option("mobileEmulation", mobile_emulation_config)

        driver = webdriver.Chrome(options=options)

        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

        return driver
