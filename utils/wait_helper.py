from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WaitHelper:
    """Helper class for common wait operations."""
    
    def __init__(self, driver, timeout: int = None):
        """
        Initialize WaitHelper.
        
        Args:
            driver: WebDriver instance
            timeout: Wait timeout in seconds
        """
        from config.config import Config
        self.driver = driver
        self.timeout = timeout or Config.EXPLICIT_WAIT
    
    def wait_for_element_visible(self, locator: tuple):
        """
        Wait for element to be visible.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def wait_for_element_clickable(self, locator: tuple):
        """
        Wait for element to be clickable.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
    
    def wait_for_element_present(self, locator: tuple):
        """
        Wait for element to be present in DOM.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def wait_for_elements_present(self, locator: tuple):
        """
        Wait for elements to be present in DOM.
        
        Args:
            locator: Tuple of (By.*, locator_value)
            
        Returns:
            List of WebElements
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
    
    def wait_for_url_contains(self, text: str):
        """
        Wait for URL to contain specific text.
        
        Args:
            text: Text that should be in URL
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.url_contains(text)
        )
    
    def wait_for_title_contains(self, text: str):
        """
        Wait for title to contain specific text.
        
        Args:
            text: Text that should be in title
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.title_contains(text)
        )
