from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Clase base para todas las paginas del POM."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        """Espera a que el elemento sea visible y lo devuelve."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """Espera a que los elementos sean visibles y los devuelve."""
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        """Espera a que el elemento sea visible y hace clic."""
        el = self.find(locator)
        el.click()

    def type(self, locator, text):
        """Espera a que el elemento sea visible, lo limpia y escribe texto."""
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """Devuelve el texto del elemento."""
        el = self.find(locator)
        return el.text

    def is_visible(self, locator):
        """Verifica si un elemento es visible en la pagina."""
        try:
            self.find(locator)
            return True
        except Exception:
            return False

    def get_title(self):
        """Devuelve el titulo de la pagina actual."""
        return self.driver.title