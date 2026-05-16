def test_open_homepage(driver):
    url = "https://www.saucedemo.com/"
    driver.get(url)
    assert driver.title != ""