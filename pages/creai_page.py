import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class CreaiPage:
    URL = "https://www.creai.mx/"
    ABOUT_URL = "https://www.creai.mx/about-us"
    SPANISH_ABOUT_URL = "https://www.creai.mx/es-mx/about-us"

    # Localizadores
    LOGO = (By.XPATH, "//img[contains(@src, 'Logo.svg')]")
    COOKIES = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")
    CTA_BUTTON = (By.XPATH, "//a[contains(@href, '/contact')]")
    SECTIONS = (By.CSS_SELECTOR, "section")
    ABOUT_US = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Success stories'])[1]/following::div[2]")
    ABOUT_US_LINK = (By.XPATH, "//a[contains(@href, '/about-us') or contains(@href, '/es-mx/about-us')]")
    LANGUAGE_SELECTOR_ES = (By.XPATH, "//a[contains(@href, '/es-mx') or contains(text(), 'ES') or contains(text(), 'Español')]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_status_code(self):
        response = requests.get(self.URL)
        return response.status_code
    
    def console_errors(self):
        logs = self.driver.get_log("browser")
        severe_logs = [log for log in logs if log["level"] == "SEVERE"]
        return len(severe_logs) == 0

    def accept_cookies(self):
        try:
            cookies_button = self.wait.until(EC.element_to_be_clickable(self.COOKIES))
            cookies_button.click()
            return True
        except (TimeoutException, NoSuchElementException):
            self.remove_cookie_banner()
            return False

    def remove_cookie_banner(self):
        js = """
            document.querySelectorAll('[id*=cookie], [class*=cookie]').forEach(e => e.remove());
        """
        try:
            self.driver.execute_script(js)
        except Exception:
            pass

    def logo_displayed(self):
        try:
            try:
                cookies_button = self.wait.until(EC.element_to_be_clickable(self.COOKIES))
                cookies_button.click()
            except (TimeoutException, NoSuchElementException):
                self.remove_cookie_banner()
            
            logo_element = self.wait.until(EC.visibility_of_element_located(self.LOGO))
            return logo_element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def is_cta_visible(self):
        try:
            cta_element = self.wait.until(
                EC.visibility_of_element_located(self.CTA_BUTTON)
            )
            return cta_element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def count_sections(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(self.SECTIONS)
            )
            sections = self.driver.find_elements(*self.SECTIONS)
            visible_sections = [s for s in sections if s.is_displayed()]
            return len(visible_sections)
        except (TimeoutException, NoSuchElementException):
            return 0

    def click_about_us(self):
        self.accept_cookies()
        self.driver.find_element(*self.ABOUT_US).click()    
           
        
    def validate_about_us_url(self):
        try:
            self.wait.until(EC.url_contains("/about-us"))
            current_url = self.driver.current_url
            return current_url == self.ABOUT_URL
        except TimeoutException:
            return False

    def select_spanish_language(self):
        try:
            self.accept_cookies()
            language_button = self.wait.until(
                EC.element_to_be_clickable(self.LANGUAGE_SELECTOR_ES)
            )
            language_button.click()
            time.sleep(2)  # Esperar a que la página recargue con el nuevo idioma
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def click_about_us_multilanguage(self):
        try:
            about_link = self.wait.until(
                EC.element_to_be_clickable(self.ABOUT_US_LINK)
            )
            about_link.click()
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def validate_spanish_about_us_url(self):
        try:
            self.wait.until(EC.url_contains("/es-mx/about-us"))
            current_url = self.driver.current_url
            return current_url == self.SPANISH_ABOUT_URL
        except TimeoutException:
            return False

