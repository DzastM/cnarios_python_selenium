from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from config.config import Config
import subprocess
import os


class DriverFactory:
    """Factory class to create WebDriver instances."""
    
    @staticmethod
    def create_driver(browser: str = None):
        """
        Create and return a WebDriver instance.
        
        Args:
            browser: Browser type ('chrome' or 'firefox'). Uses Config.BROWSER if not specified.
            
        Returns:
            WebDriver instance
        """
        browser = browser or Config.BROWSER
        
        if browser == "chrome":
            return DriverFactory._create_chrome_driver()
        elif browser == "firefox":
            return DriverFactory._create_firefox_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    
    @staticmethod
    def _create_chrome_driver():
        """Create a Chrome WebDriver instance using Selenium Manager."""
        options = webdriver.ChromeOptions()
        
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")
        
        # Use Selenium Manager (built-in to Selenium 4.6+)
        options.add_argument("--disable-search-engine-choice-screen")
        
        # Create driver - Selenium Manager will handle driver download
        driver = webdriver.Chrome(options=options)
        
        return driver
    
    @staticmethod
    def _create_firefox_driver():
        """Create a Firefox WebDriver instance using Selenium Manager."""
        options = webdriver.FirefoxOptions()
        
        if Config.HEADLESS:
            options.add_argument("--headless")
        
        # Create driver - Selenium Manager will handle driver download
        driver = webdriver.Firefox(options=options)
        
        return driver
