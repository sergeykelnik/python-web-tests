"""
Mobile device emulation profiles for Chrome.
"""
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class DeviceProfile:
    """Represents a mobile device profile for emulation."""
    name: str
    width: int
    height: int
    device_scale_factor: float
    user_agent: str

    def to_chrome_options(self) -> Dict[str, Any]:
        """Convert device profile to Chrome mobile emulation options."""
        return {
            "deviceMetrics": {
                "width": self.width,
                "height": self.height,
                "pixelRatio": self.device_scale_factor,
                "touch": True
            },
            "userAgent": self.user_agent
        }


class MobileDevices:
    """Collection of mobile device profiles for emulation."""

    IPHONE_12_PRO = DeviceProfile(
        name="iPhone 12 Pro",
        width=390,
        height=844,
        device_scale_factor=3.0,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    )

    PIXEL_7 = DeviceProfile(
        name="Pixel 7",
        width=412,
        height=915,
        device_scale_factor=2.625,
        user_agent="Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
    )

    SAMSUNG_GALAXY_S21 = DeviceProfile(
        name="Samsung Galaxy S21",
        width=360,
        height=800,
        device_scale_factor=3.0,
        user_agent="Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
    )

    @classmethod
    def get_device(cls, device_name: str) -> DeviceProfile:
        """Get device profile by name."""
        devices = {
            "iPhone 12 Pro": cls.IPHONE_12_PRO,
            "Pixel 7": cls.PIXEL_7,
            "Samsung Galaxy S21": cls.SAMSUNG_GALAXY_S21,
        }

        if device_name not in devices:
            raise ValueError(f"Unknown device: {device_name}. Available: {list(devices.keys())}")

        return devices[device_name]
