# Selenium & Python Automation Framework

A robust base structure for Selenium WebDriver automation tests using Python.

## Project Structure

```
project/
├── config/
│   ├── config.py           # Configuration settings
│   └── __init__.py
├── drivers/
│   ├── driver_factory.py   # WebDriver factory
│   └── __init__.py
├── pages/
│   ├── base_page.py        # Base page object class
│   ├── example_page.py     # Example page object
│   └── __init__.py
├── tests/
│   ├── test_example.py     # Example test class
│   └── __init__.py
├── utils/
│   ├── wait_helper.py      # Wait utilities
│   └── __init__.py
├── base/
│   ├── base_test.py        # Base test class
│   └── __init__.py
├── screenshots/            # Stored screenshots (auto-created)
├── reports/               # Test reports (auto-created)
├── conftest.py            # Pytest configuration
├── .env.example           # Environment variables template
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Features

- **Page Object Model (POM)**: Organized page objects with base class
- **WebDriver Factory**: Easy browser setup (Chrome, Firefox)
- **Wait Helpers**: Explicit wait utilities for common scenarios
- **Configuration Management**: Environment-based configuration
- **Base Test Class**: Common setup/teardown for all tests
- **Screenshot Capture**: Automatic screenshot directory management
- **Pytest Integration**: Full pytest support with automatic fixtures

## Installation

1. **Clone/Create the project**
   ```bash
   cd cnarios_python_selenium
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   copy .env.example .env
   # Edit .env with your settings
   ```

## Configuration

Edit `.env` file to customize:

```env
BROWSER=chrome              # Browser type: chrome, firefox
HEADLESS=False              # Run in headless mode
IMPLICIT_WAIT=10            # Implicit wait timeout (seconds)
EXPLICIT_WAIT=15            # Explicit wait timeout (seconds)
BASE_URL=https://example.com # Your test base URL
SCREENSHOT_ON_FAILURE=True  # Take screenshots on test failure
```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_example.py
```

### Run specific test
```bash
pytest tests/test_example.py::TestExample::test_page_loads
```

### Run with verbose output
```bash
pytest -v
```

### Run with HTML report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run in headless mode
```bash
HEADLESS=True pytest
```

## Creating New Tests

### 1. Create a Page Object

```python
# pages/my_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyPage(BasePage):
    ELEMENT = (By.ID, "element_id")
    
    def do_something(self):
        self.click(self.ELEMENT)
```

### 2. Create a Test Class

```python
# tests/test_my_feature.py
from base.base_test import BaseTest
from pages.my_page import MyPage

class TestMyFeature(BaseTest):
    def test_something(self):
        page = MyPage(self.driver)
        page.navigate_to()
        page.do_something()
        assert some_condition
```

## Key Classes & Methods

### BasePage
- `navigate_to(url)` - Navigate to URL
- `click(locator)` - Wait and click element
- `type_text(locator, text)` - Type text into element
- `get_text(locator)` - Get element text
- `is_element_visible(locator)` - Check visibility
- `is_element_present(locator)` - Check if present in DOM
- `take_screenshot(filename)` - Take screenshot

### WaitHelper
- `wait_for_element_visible(locator)` - Wait for visibility
- `wait_for_element_clickable(locator)` - Wait for clickable
- `wait_for_element_present(locator)` - Wait for presence
- `wait_for_url_contains(text)` - Wait for URL change
- `wait_for_title_contains(text)` - Wait for title change

### DriverFactory
- `create_driver(browser)` - Create WebDriver instance

## Best Practices

1. **Use Page Objects**: Keep tests clean by using page objects
2. **Explicit Waits**: Always wait for elements before interacting
3. **Meaningful Names**: Use descriptive test and method names
4. **DRY Principle**: Reuse common functionality in base classes
5. **Error Handling**: Handle exceptions gracefully
6. **Assertions**: Assert specific conditions, not generic ones

## Troubleshooting

### WebDriver not found
```bash
pip install webdriver-manager
```

### Selenium version issues
```bash
pip install --upgrade selenium
```

### Port already in use
Try a different port or kill the process using it

## Dependencies

- **selenium** >= 4.15.2 - WebDriver bindings
- **pytest** >= 7.4.3 - Testing framework
- **pytest-html** >= 4.1.1 - HTML reporting
- **python-dotenv** >= 1.0.0 - Environment variables
- **webdriver-manager** >= 4.0.1 - WebDriver management

## License

This project is open source and available for personal/commercial use.

## Support

For issues or questions, refer to the official documentation:
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
