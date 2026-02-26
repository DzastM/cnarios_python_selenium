import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration class for test settings."""
    
    # Browser settings
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 15))
    
    # Base URL
    BASE_URL = os.getenv("BASE_URL", "https://www.example.com")
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "True").lower() == "true"
    SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "..", "screenshots")
    
    # Report settings
    REPORT_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")
