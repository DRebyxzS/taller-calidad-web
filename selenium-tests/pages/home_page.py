from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    def open(self, url):
        self.driver.get(url)