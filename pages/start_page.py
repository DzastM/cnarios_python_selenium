from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StartPage(BasePage):
    
    # Page locators
    # HEADING = (By.TAG_NAME, "h1")
    # SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search']")
    # SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    # RESULTS = (By.CSS_SELECTOR, ".results li")
    CHALLENGES_BUTTON = (By.XPATH, "//button[text()='Challenges']")
    START_EXPLORING_BUTTON = (By.XPATH, "//button[text()='Start Exploring']")

    def __init__(self, driver):
        """Initialize StartPage."""
        super().__init__(driver)
    
    # def get_heading(self) -> str:
    #     """
    #     Get the page heading.
        
    #     Returns:
    #         Heading text
    #     """
    #     return self.get_text(self.HEADING)
    
    def click_button(self, button_name: str):
        if button_name == "Challenges":
            self.click(self.CHALLENGES_BUTTON)
        elif button_name == "Start Exploring":
            self.click(self.START_EXPLORING_BUTTON)
    
    # def get_results_count(self) -> int:
    #     """
    #     Get the number of search results.
        
    #     Returns:
    #         Number of results
    #     """
    #     results = self.find_elements(self.RESULTS)
    #     return len(results)
    
    # def get_result_text(self, index: int) -> str:
    #     """
    #     Get text from a specific result.
        
    #     Args:
    #         index: Result index (0-based)
            
    #     Returns:
    #         Text of the result
    #     """
    #     results = self.find_elements(self.RESULTS)
    #     if index < len(results):
    #         return results[index].text
    #     return ""
