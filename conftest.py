import pytest
import os
from config.config import Config


def pytest_configure(config):
    """Configure pytest."""
    # Create directories for screenshots and reports
    if not os.path.exists(Config.SCREENSHOT_DIR):
        os.makedirs(Config.SCREENSHOT_DIR)
    if not os.path.exists(Config.REPORT_DIR):
        os.makedirs(Config.REPORT_DIR)


@pytest.fixture(scope="session")
def test_env():
    """Provide test environment configuration."""
    return {
        "base_url": Config.BASE_URL,
        "browser": Config.BROWSER,
        "headless": Config.HEADLESS,
    }
