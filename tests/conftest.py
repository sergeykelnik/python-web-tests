"""
Pytest fixtures for test configuration.
"""

import pytest

from config.config import Config
from drivers.driver_factory import DriverFactory
from utils.helpers import Helpers


@pytest.fixture(scope="function")
def driver():
    """
    Create a Chrome WebDriver instance for each test.
    Uses settings from .env file (headless, mobile_emulation, device).

    Yields:
        Chrome WebDriver instance
    """
    _driver = DriverFactory.create_driver()
    yield _driver
    _driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Hook to capture screenshots on test failure.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if Config.SCREENSHOT_ON_FAILURE:
            driver = item.funcargs.get("driver") or item.funcargs.get("driver_headless")
            if driver:
                Helpers.take_screenshot(driver, f"FAIL_{item.name}")
