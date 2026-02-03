"""
Configuration settings for the test framework.
All values are loaded from .env file.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
env_file = Path(__file__).parent.parent / ".env"
load_dotenv(env_file)


class Config:
    """Configuration class - all values loaded from .env file."""

    # Base URLs
    BASE_URL = os.getenv("BASE_URL", "https://m.twitch.tv")

    # Timeouts (in seconds)
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "20"))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))

    # Chrome browser settings
    MOBILE_EMULATION = os.getenv("MOBILE_EMULATION", "true").lower() in ("true", "1", "yes")
    DEFAULT_DEVICE = os.getenv("DEFAULT_DEVICE", "iPhone 12 Pro")

    # Screenshot settings
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() in ("true", "1", "yes")
    SCREENSHOT_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.getenv("SCREENSHOT_DIR", "screenshots")
    )

    # Report settings
    REPORT_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        os.getenv("REPORT_DIR", "reports")
    )


# Create directories if they don't exist
os.makedirs(Config.SCREENSHOT_DIR, exist_ok=True)
os.makedirs(Config.REPORT_DIR, exist_ok=True)
