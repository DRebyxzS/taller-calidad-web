import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):
    """Pagina de inicio de sesion de Saucedemo."""

    USERNAME = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Abre la pagina de login y espera que cargue."""
        base_url = os.environ.get("SUT_BASE_URL", "https://www.saucedemo.com/")
        self.driver.get(base_url)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, username, password):
        """Realiza el login con las credenciales dadas."""
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def login_as_standard_user(self):
        """Realiza login con el usuario de prueba configurado."""
        username = os.environ.get("SUT_USERNAME", "standard_user")
        password = os.environ.get("SUT_PASSWORD", "secret_sauce")
        self.login(username, password)
        wait = WebDriverWait(self.driver, 10)
        inventory_locator = (By.CSS_SELECTOR, ".inventory_item")
        wait.until(EC.visibility_of_element_located(inventory_locator))

    def get_error_message(self):
        """Devuelve el mensaje de error si existe."""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return None