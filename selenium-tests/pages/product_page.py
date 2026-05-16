from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProductPage(BasePage):
    """Pagina de detalle de un producto."""

    PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, '[data-test="back-to-products"]')
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_name(self):
        """Devuelve el nombre del producto."""
        return self.get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        """Devuelve el precio del producto."""
        return self.get_text(self.PRODUCT_PRICE)

    def add_to_cart(self):
        """Agrega el producto al carrito."""
        self.click(self.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        """Navega al carrito."""
        self.click(self.CART_LINK)

    def get_cart_item_count(self):
        """Devuelve el numero de items en el carrito."""
        try:
            badge = self.find(self.CART_BADGE)
            return int(badge.text)
        except Exception:
            return 0