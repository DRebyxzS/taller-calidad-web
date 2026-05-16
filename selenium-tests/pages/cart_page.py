from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class CartPage(BasePage):
    """Pagina del carrito de compras."""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CART_ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[data-test="checkout"]')
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, '[data-test="continue-shopping"]')

    def __init__(self, driver):
        super().__init__(driver)

    def _wait_for_cart_page(self):
        """Espera a que la pagina del carrito cargue completamente."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON))

    def get_cart_item_count(self):
        """Devuelve la cantidad de items en el carrito."""
        items = self.find_all(self.CART_ITEMS)
        return len(items)

    def get_cart_item_names(self):
        """Devuelve los nombres de los productos en el carrito."""
        elements = self.find_all(self.CART_ITEM_NAMES)
        return [el.text for el in elements]

    def proceed_to_checkout(self):
        """Hace clic en el boton Checkout y espera que cargue."""
        self._wait_for_cart_page()
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        """Vuelve a la pagina de productos."""
        self.click(self.CONTINUE_SHOPPING)