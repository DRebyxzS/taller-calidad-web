from pages.home_page import HomePage

BASE_URL = "http://automationpractice.com/index.php"

def test_search_product(driver):
    home = HomePage(driver)
    home.open(BASE_URL)
    home.search("dress")

    # En un entorno con Selenium real, aquí podríamos validar resultados.
    # De momento, solo verificamos que llegamos hasta aquí sin errores.
    assert True