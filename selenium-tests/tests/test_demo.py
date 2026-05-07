def test_open_homepage(driver):
    url = "http://automationpractice.com/index.php"
    driver.get(url)
    assert "My Store" in driver.title