import pytest
import os
from drivers.driver_factory import DriverFactory
from config.config import Config


class BaseTest:
    """Base test class with common setup and teardown."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup method that runs before each test."""
        self.driver = DriverFactory.create_driver()
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        yield
        self.teardown_method()
    
    def teardown_method(self):
        """Teardown method that runs after each test."""
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
    
    def take_screenshot(self, name: str = None):
        """
        Take a screenshot for debugging.
        
        Args:
            name: Screenshot filename
        """
        if not os.path.exists(Config.SCREENSHOT_DIR):
            os.makedirs(Config.SCREENSHOT_DIR)
        
        if name is None:
            name = f"screenshot_{id(self)}.png"
        
        filepath = os.path.join(Config.SCREENSHOT_DIR, name)
        self.driver.save_screenshot(filepath)
