class ProductPurchasingPage(BasePage):
    """Product Purchasing page object."""
    
    # Page locators
    HEADING = (By.TAG_NAME, "h1")
    
    def __init__(self, driver):
        super().__init__(driver)