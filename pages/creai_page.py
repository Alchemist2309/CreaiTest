import requests
from selenium.webdriver.common.by import By

class CreaiPage:
    URL = "https://www.creai.mx/"

    #Localizadores

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def get_status_code(self):
        response = requests.get(self.URL)
        return response.status_code