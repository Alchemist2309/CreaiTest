# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**CreaiTest** is an automated testing suite for the Creai website (https://www.creai.mx/) using Selenium WebDriver with Python and the Behave BDD framework.

- **Tech Stack**: Python 3.12+, Selenium 4.16+, Behave 1.2.6+, Chrome/ChromeDriver
- **Language**: Test scenarios and documentation are in Spanish, code is in English
- **Testing Approach**: BDD with Gherkin syntax, Page Object Model pattern

## Essential Commands

### Environment Setup
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running Tests
```bash
# Run all tests
behave

# Run specific feature file
behave features/home_creai.feature

# Run with verbose output
behave -v

# Run specific scenario by name
behave -n "validar carga exitosa de la homepage"

# Dry run (check step definitions without executing)
behave --dry-run
```

## Architecture

### Page Object Model (POM)

The project follows the Page Object Model pattern with page classes in the `pages/` directory.

**Key characteristics:**
- Locators defined as class-level tuples: `ELEMENT = (By.XPATH, "//xpath")`
- All page interactions encapsulated in methods
- Uses WebDriverWait with 10-second timeout for explicit waits
- Verification methods return boolean values (not assertions)
- Error handling with try/except for TimeoutException and NoSuchElementException

**Example pattern from `pages/creai_page.py`:**
```python
class CreaiPage:
    URL = "https://www.creai.mx/"
    LOGO = (By.XPATH, "//img[contains(@src, 'Logo.svg')]")

    def logo_displayed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.LOGO)
            )
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
```

### WebDriver Configuration

**Location:** `utils/driver.py`

**Important details:**
- Chrome runs in **headed mode** by default (headless is commented out)
- Global implicit wait: 10 seconds
- Window size: 1920x1080
- ChromeDriver auto-managed via webdriver-manager
- No automatic driver cleanup (manual quit required)

**Chrome options:**
```python
--no-sandbox
--disable--gpu  # Note: Has typo with double dash
--window-size=1920,1080
# --headless=new  # Commented out
```

### BDD with Behave

**Feature files:** `features/*.feature` (written in Spanish Gherkin)

**Step definitions:** `features/steps/creai_steps.py`

**Context usage pattern:**
- `context.driver` - WebDriver instance
- `context.creai_page` - Page object instance
- Each `@given` step creates fresh driver and page object
- Assertions done in `@then` steps using `assert` with custom messages

**No environment.py file exists** - driver cleanup happens manually in steps rather than via Behave hooks.

### Wait Strategy

The project uses a **mixed wait strategy**:
- **Implicit wait**: 10 seconds (set globally in driver.py)
- **Explicit waits**: WebDriverWait with 10-second timeout in page methods
- Note: Mixing both is not best practice but is the current implementation

## Code Conventions

### Naming
- **Classes**: PascalCase (`CreaiPage`)
- **Methods**: snake_case (`logo_displayed`)
- **Constants/Locators**: UPPERCASE (`CTA_BUTTON`)
- **Files**: snake_case (`creai_page.py`, `home_creai.feature`)

### Import Organization
```python
# Standard library
import requests

# Third-party
from selenium import webdriver
from selenium.webdriver.common.by import By

# Local
from utils.driver import get_driver
from pages.creai_page import CreaiPage
```

### Assertion Pattern
Page objects return boolean values; assertions happen in step definitions:
```python
# In page object
def is_cta_visible(self):
    return element.is_displayed()

# In step definition
assert context.creai_page.is_cta_visible(), "El botón CTA no está visible"
```

## Known Issues

1. **Missing constant**: `creai_page.py:95` references `self.ABOUT_URL` which is not defined in the class
2. **Chrome flag typo**: `'--disable--gpu'` has double dash (should be `--disable-gpu`)
3. **No driver cleanup**: Missing `features/environment.py` with `after_scenario` hook to properly quit driver

## Project-Specific Patterns

### Cookie Consent Handling
Dual-strategy approach in `CreaiPage`:
1. First attempts to click the cookie acceptance button
2. Falls back to JavaScript-based banner removal if button not found
3. Called before interacting with other elements to prevent interference

### HTTP Status Validation
Uses the `requests` library (not Selenium) to validate HTTP status codes:
```python
response = requests.get(self.URL)
return response.status_code
```

### Console Error Checking
Reads browser logs directly via Selenium:
```python
logs = self.driver.get_log("browser")
severe_errors = [log for log in logs if log['level'] == 'SEVERE']
```

### Locator Strategy
- **XPATH**: Used for complex elements and text-based matching
- **CSS Selectors**: Used for simple element queries
- All locators stored as class constants at the top of page classes

## Current Test Coverage

The test suite covers:
1. **Page load validation** - HTTP 200 status, no SEVERE console errors
2. **Element visibility** - Logo, contact button, minimum 3 sections
3. **Navigation** - About Us menu click and URL validation

## Important Notes

- **No configuration files**: No behave.ini, pytest.ini, or setup.cfg
- **No test reporting**: HTML reports or Allure not configured
- **Hardcoded URLs**: Base URL is hardcoded in CreaiPage, not using environment variables
- **No parallel execution**: Tests run serially (standard Behave behavior)
- **No CI/CD**: No GitHub Actions or other CI configuration present
- **No package structure**: No `__init__.py` files, imports work from project root
