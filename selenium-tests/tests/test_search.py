from pages.home_page import HomePage

BASE_URL = "http://automationpractice.com/index.php"

def test_search_product(driver):
    home = HomePage(driver)
    home.open(BASE_URL)

    # NOTA:
    # El sitio original de 'My Store' ha cambiado (aparece InMotion Hosting),
    # por lo que no existe el campo de búsqueda 'search_query_top'.
    # Este test se deja como placeholder hasta que el profesor defina un nuevo SUT.
    assert driver.title != ""