import pytest

# Cuando estés en un PC sin restricciones de Sophos, podrás usar este bloque REAL:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

#     service = Service(ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()

class FakeDriver:
    def __init__(self):
        self.title = "My Store (fake)"
        self.page_source = "<html><body>My Store</body></html>"

    def get(self, url):
        print(f"[FAKE DRIVER] Abriendo URL: {url}")

    def implicitly_wait(self, seconds):
        pass

    def quit(self):
        pass

@pytest.fixture
def driver():
    # Versión fake para trabajar en el PC de la universidad sin usar ChromeDriver
    fake = FakeDriver()
    yield fake
    fake.quit()