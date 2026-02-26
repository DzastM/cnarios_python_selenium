import pytest
from base.base_test import BaseTest
from pages.example_page import ExamplePage


class TestExample(BaseTest):
    """Example test class demonstrating test structure."""
    
    def test_page_loads(self):
        """Test that the page loads successfully."""
        page = ExamplePage(self.driver)
        page.navigate_to()
        
        # Verify page loaded
        assert page.get_current_url() is not None
        print(f"Page URL: {page.get_current_url()}")
    
    def test_page_title(self):
        """Test that the page has a title."""
        page = ExamplePage(self.driver)
        page.navigate_to()
        
        title = page.get_page_title()
        assert title is not None
        print(f"Page Title: {title}")
    
    @pytest.mark.skip(reason="Example test - update with real test data")
    def test_search_functionality(self):
        """Example test for search functionality."""
        page = ExamplePage(self.driver)
        page.navigate_to()
        
        # Perform search
        page.search("example query")
        
        # Verify results
        assert page.get_results_count() > 0
