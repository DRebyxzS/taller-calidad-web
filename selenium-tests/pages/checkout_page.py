import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CheckoutPage(BasePage):
    """Pagina de checkout (informacion + confirmacion + completado)."""

    FIRST_NAME = (By.CSS_SELECTOR, '[data-test="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, '[data-test="lastName"]')
    POSTAL_CODE = (By.CSS_SELECTOR, '[data-test="postalCode"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-test="continue"]')
    FINISH_BUTTON = (By.CSS_SELECTOR, '[data-test="finish"]')
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')
    CHECKOUT_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEM = (By.CSS_SELECTOR, ".cart_item")

    def __init__(self, driver):
        super().__init__(driver)

    def _wait_for_checkout_page(self):
        """Espera a que la pagina de checkout cargue completamente."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.FIRST_NAME))

    def fill_information(self, first_name, last_name, postal_code):
        """Rellena el formulario de informacion del checkout."""
        self._wait_for_checkout_page()
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        """Hace clic en Continue para ir al resumen."""
        self.click(self.CONTINUE_BUTTON)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.CART_ITEM))

    def finish_checkout(self):
        """Hace clic en Finish para completar la compra."""
        self.click(self.FINISH_BUTTON)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))

    def get_complete_message(self):
        """Devuelve el mensaje de confirmacion de la compra."""
        return self.get_text(self.COMPLETE_HEADER)

    def complete_checkout_as_guest(
        self,
        first_name=None,
        last_name=None,
        postal_code=None,
    ):
        """Completa todo el flujo de checkout con datos de invitado."""
        self.fill_information(
            first_name or os.environ.get("GUEST_FIRST_NAME", "Juan"),
            last_name or os.environ.get("GUEST_LAST_NAME", "Perez"),
            postal_code or os.environ.get("GUEST_POSTAL_CODE", "110111"),
        )
        self.continue_checkout()
        self.finish_checkout()
        return self.get_complete_message()