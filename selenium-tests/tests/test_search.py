from pages.home_page import HomePage

BASE_URL = "https://www.saucedemo.com/"

def test_search_product(driver):
    home = HomePage(driver)
    home.open(BASE_URL)
    assert driver.title != ""