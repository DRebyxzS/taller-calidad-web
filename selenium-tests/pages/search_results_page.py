from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class SearchResultsPage(BasePage):
    """Pagina de resultados de busqueda/filtrado de productos."""

    INVENTORY_ITEMS = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    INVENTORY_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    SORT_DROPDOWN = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_count(self):
        """Devuelve la cantidad de productos en los resultados."""
        items = self.find_all(self.INVENTORY_ITEMS)
        return len(items)

    def get_product_names(self):
        """Devuelve una lista con los nombres de los productos."""
        elements = self.find_all(self.INVENTORY_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self):
        """Devuelve una lista con los precios de los productos."""
        elements = self.find_all(self.INVENTORY_PRICES)
        return [el.text for el in elements]

    def sort_by_price_low_to_high(self):
        """Ordena los productos de menor a mayor precio."""
        dropdown = self.find(self.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value("lohi")

    def select_product_by_name(self, product_name):
        """Selecciona un producto haciendo clic en su nombre."""
        elements = self.find_all(self.INVENTORY_NAMES)
        for el in elements:
            if el.text == product_name:
                el.click()
                return
        raise Exception(f"Producto '{product_name}' no encontrado")