from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_purchasing import ProductPurchasingPage


class ChallengesPage(BasePage):
    """Challenges page object."""
    
    # Page locators
    HEADING = (By.TAG_NAME, "h1")
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    RESULTS = (By.CSS_SELECTOR, ".results li")
    PRODUCT_PURCHASING_TEXT = "E-commerce End-to-End Product Purchasing Flow"
    VIEW_CHALLENGE_BUTTON = (By.XPATH, f"//h2[contains(., '{PRODUCT_PURCHASING_TEXT}')]/../..//button[contains(., 'View Challenge')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_view_challenge(self, challenge_name: str) -> None:
        button_locator = (By.XPATH, f"//h2[contains(., '{challenge_name}')]/../..//button[contains(., 'View Challenge')]")
        self.click(button_locator)
        if challenge_name == self.PRODUCT_PURCHASING_TEXT:            
            return ProductPurchasingPage(self.driver)

    # def search(self, query: str):
    #     """
    #     Perform a search.
        
    #     Args:
    #         query: Search query
    #     """
    #     self.type_text(self.SEARCH_BOX, query)
    #     self.click(self.SEARCH_BUTTON)
    
    # def get_results_count(self) -> int:
    #     """
    #     Get the number of search results.
        
    #     Returns:
    #         Number of results
    #     """
    #     results = self.find_elements(self.RESULTS)
    #     return len(results)
    
    def get_result_text(self, index: int) -> str:
        """
        Get text from a specific result.
        
        Args:
            index: Result index (0-based)
            
        Returns:
            Text of the result
        """
        results = self.find_elements(self.RESULTS)
        if index < len(results):
            return results[index].text
        return ""
