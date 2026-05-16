from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login_and_homepage_loads(driver):
    """Test de humo: Verificar que se puede hacer login y la pagina principal carga."""
    login = LoginPage(driver)
    login.open()
    login.login_as_standard_user()

    home = HomePage(driver)
    product_count = home.get_product_count()
    assert product_count > 0, "No se encontraron productos en la pagina principal"
    assert "Swag Labs" in driver.title, "El titulo de la pagina no es el esperado"