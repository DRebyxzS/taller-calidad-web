Taller de Calidad de Software Web - UCC
Descripción
Repositorio para el taller de Calidad de Software Web de la Universidad Cooperativa de Colombia.

Herramientas
Selenium (Python + POM) — Sección A
Cypress (E2E + mocking) — Sección B
LoadRunner (pruebas de carga) — Sección C
OWASP ZAP (seguridad) — Sección D
Hotjar (usabilidad) — Sección E
SUT (Site Under Test)
Original: https://automationpractice.com (ya no disponible)
Actual: https://www.saucedemo.com (tienda de pruebas oficial)
Estado del taller
 Sección A: Selenium — POM completo + 4 tests + CI + screenshots
 Sección B: Cypress — Pendiente
 Sección C: LoadRunner — Pendiente
 Sección D: OWASP ZAP — Pendiente
 Sección E: Hotjar — Pendiente
Estructura Selenium
selenium-tests/
├── conftest.py ← Fixture driver + screenshots automáticos
├── pytest.ini ← Configuración con reportes HTML
├── requirements.txt ← Dependencias Python
├── pages/
│ ├── base_page.py ← POM — BasePage
│ ├── login_page.py ← POM — LoginPage
│ ├── home_page.py ← POM — HomePage
│ ├── search_results_page.py ← POM — SearchResultsPage
│ ├── product_page.py ← POM — ProductPage
│ ├── cart_page.py ← POM — CartPage
│ └── checkout_page.py ← POM — CheckoutPage
├── tests/
│ ├── test_demo.py ← Test de humo (login + carga)
│ ├── test_search.py ← Test de búsqueda/filtrado
│ ├── test_add_to_cart.py ← Test de agregar al carrito
│ └── test_checkout_guest.py ← Test de checkout como invitado
├── utils/
│ └── wait_utils.py ← Utilidades de espera
├── reports/ ← Reportes HTML + screenshots
├── tests_smoke/ ← Preparada para tests de humo
├── tests_regression/ ← Preparada para tests de regresión
└── fixtures/ ← Preparada para fixtures

## Ejecutar tests Selenium
```bash
cd selenium-tests
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
pytest                        # ejecutar todos
pytest --html=reports/report.html  # con reporte HTML