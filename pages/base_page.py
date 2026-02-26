from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper
from config.config import Config
import os
import time


class BasePage:
    """Base Page Object class."""
    
    def __init__(self, driver):
        """
        Initialize BasePage.
        
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WaitHelper(driver)
    
    def navigate_to(self, url: str = None):
        """
        Navigate to a URL.
        
        Args:
            url: URL to navigate to. If not provided, uses Config.BASE_URL
        """
        url = url or Config.BASE_URL
        self.driver.get(url)
    
    def find_element(self, locator: tuple):
        """
        Find a single element.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            WebElement
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator: tuple):
        """
        Find multiple elements.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            List of WebElements
        """
        return self.driver.find_elements(*locator)
    
    def click(self, locator: tuple):
        """
        Click on an element.
        
        Args:
            locator: Tuple of (By.*, locator_value)
        """
        element = self.wait.wait_for_element_clickable(locator)
        element.click()
    
    def type_text(self, locator: tuple, text: str):
        """
        Type text into an element.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            text: Text to type
        """
        element = self.wait.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: tuple) -> str:
        """
        Get text from an element.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            Text content of the element
        """
        element = self.wait.wait_for_element_visible(locator)
        return element.text
    
    def is_element_visible(self, locator: tuple) -> bool:
        """
        Check if element is visible.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            True if visible, False otherwise
        """
        try:
            element = self.wait.wait_for_element_visible(locator)
            return element.is_displayed()
        except:
            return False
    
    def is_element_present(self, locator: tuple) -> bool:
        """
        Check if element is present in DOM.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            True if present, False otherwise
        """
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
    
    def take_screenshot(self, filename: str = None) -> str:
        """
        Take a screenshot of the current page.
        
        Args:
            filename: Name for the screenshot file
            
        Returns:
            Path to the screenshot file
        """
        if not os.path.exists(Config.SCREENSHOT_DIR):
            os.makedirs(Config.SCREENSHOT_DIR)
        
        if filename is None:
            filename = f"screenshot_{int(time.time())}.png"
        
        filepath = os.path.join(Config.SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(filepath)
        
        return filepath
    
    def get_page_title(self) -> str:
        """
        Get the page title.
        
        Returns:
            Page title
        """
        return self.driver.title
    
    def get_current_url(self) -> str:
        """
        Get the current URL.
        
        Returns:
            Current URL
        """
        return self.driver.current_url
