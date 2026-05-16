from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    """Utilidades de espera personalizadas."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_url_contains(self, text):
        """Espera a que la URL contenga un texto especifico."""
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.url_contains(text))

    def wait_for_title_contains(self, text):
        """Espera a que el titulo contenga un texto especifico."""
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.title_contains(text))