from pages.login_page import LoginPage
from pages.search_results_page import SearchResultsPage


def test_search_product(driver):
    """Test: Verificar que se pueden buscar/filtrar productos."""
    # 1. Login
    login = LoginPage(driver)
    login.open()
    login.login_as_standard_user()

    # 2. En la pagina de resultados, verificar productos visibles
    search_results = SearchResultsPage(driver)
    product_count = search_results.get_product_count()
    assert product_count == 6, f"Se esperaban 6 productos, se encontraron {product_count}"

    # 3. Ordenar por precio (menor a mayor) como forma de busqueda/filtro
    search_results.sort_by_price_low_to_high()

    # 4. Verificar que los precios estan ordenados
    prices = search_results.get_product_prices()
    price_values = [float(p.replace("$", "")) for p in prices]
    assert price_values == sorted(price_values), "Los productos no estan ordenados por precio"

    # 5. Seleccionar un producto
    search_results.select_product_by_name("Sauce Labs Onesie")