import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class HomePage(BasePage):
    """Pagina principal (inventario) de Saucedemo despues del login."""

    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    MENU_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")

    def __init__(self, driver):
        super().__init__(driver)

    def _wait_for_inventory(self):
        """Espera a que el inventario cargue despues del login."""
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEMS))

    def get_product_count(self):
        """Devuelve la cantidad de productos visibles."""
        self._wait_for_inventory()
        items = self.find_all(self.INVENTORY_ITEMS)
        return len(items)

    def get_product_names(self):
        """Devuelve una lista con los nombres de los productos."""
        self._wait_for_inventory()
        elements = self.find_all(self.INVENTORY_NAMES)
        return [el.text for el in elements]

    def add_product_to_cart(self, product_name):
        """Agrega un producto al carrito por su nombre y espera confirmacion."""
        product_key = product_name.lower().replace(" ", "-")
        add_button = (
            By.CSS_SELECTOR,
            f'[data-test="add-to-cart-{product_key}"]',
        )
        # Esperar a que el boton sea clickeable
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(add_button))
        self.click(add_button)
        # Esperar a que el badge del carrito aparezca
        time.sleep(1)
        try:
            wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        except Exception:
            pass

    def go_to_cart(self):
        """Navega al carrito."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.CART_LINK))
        self.click(self.CART_LINK)

    def get_cart_item_count(self):
        """Devuelve el numero de items en el carrito (del badge)."""
        try:
            wait = WebDriverWait(self.driver, 5)
            badge = wait.until(EC.visibility_of_element_located(self.CART_BADGE))
            return int(badge.text)
        except Exception:
            return 0