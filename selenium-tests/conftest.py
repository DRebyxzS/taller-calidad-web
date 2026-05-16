import pytest
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Cargar variables de entorno desde .env
load_dotenv()

# Agregar raiz del proyecto al path
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def driver():
    """Fixture que provee un WebDriver para los tests."""
    browser = os.environ.get("BROWSER", "firefox").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)

        if os.environ.get("CI") == "true":
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    else:
        # Firefox: sin popup de contraseñas comprometidas
        options = webdriver.FirefoxOptions()

        if os.environ.get("CI") == "true":
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar screenshot automaticamente cuando un test falla."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(
                os.path.dirname(__file__), "reports", "screenshots"
            )
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            try:
                driver.save_screenshot(filepath)
                print(f"\nScreenshot guardado: {filepath}")
            except Exception as e:
                print(f"\nNo se pudo guardar screenshot: {e}")