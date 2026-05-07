from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.NAME, "submit_search")

    def open(self, url):
        self.driver.get(url)

    def search(self, term):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)