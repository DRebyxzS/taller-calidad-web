import pytest
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Cargar variables de entorno desde .env
load_dotenv()

# Agregar raiz del proyecto al path
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def driver():
    """Fixture que provee un WebDriver de Chrome para los tests."""
    options = webdriver.ChromeOptions()

    # Opciones basicas
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Desactivar guardar contrasena
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    # Si estamos en CI (GitHub Actions), ejecutar sin interfaz grafica
    if os.environ.get("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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