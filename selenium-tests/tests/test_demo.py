def test_open_homepage(driver):
    url = "http://automationpractice.com/index.php"
    driver.get(url)

    # Imprimir el título para ver qué devuelve realmente
    print("TÍTULO OBTENIDO:", driver.title)

    # Comprobamos simplemente que la página carga (título no vacío)
    assert driver.title != ""