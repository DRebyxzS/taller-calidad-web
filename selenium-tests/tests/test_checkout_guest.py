import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_guest(driver):
    """Test: Completar el flujo de checkout como invitado."""
    # 1. Login
    login = LoginPage(driver)
    login.open()
    login.login_as_standard_user()

    # 2. Agregar un producto al carrito
    home = HomePage(driver)
    time.sleep(2)
    product_name = "Sauce Labs Backpack"
    home.add_product_to_cart(product_name)

    # 3. Verificar que se agrego al carrito
    cart_count = home.get_cart_item_count()
    assert cart_count >= 1, f"Se esperaba al menos 1 item en el carrito, se encontraron {cart_count}"

    # 4. Ir al carrito
    home.go_to_cart()

    # 5. Esperar a que cargue la pagina del carrito
    time.sleep(2)

    # 6. Verificar que el producto esta en el carrito
    cart = CartPage(driver)
    cart_items = cart.get_cart_item_names()
    assert product_name in cart_items, f"El producto '{product_name}' no esta en el carrito. Items: {cart_items}"

    # 7. Proceder al checkout
    cart.proceed_to_checkout()

    # 8. Completar el checkout con datos de invitado
    checkout = CheckoutPage(driver)
    message = checkout.complete_checkout_as_guest(
        first_name="Juan",
        last_name="Perez",
        postal_code="110111",
    )

    # 9. Verificar que la compra se completo
    assert "Thank you" in message, f"Mensaje de confirmacion inesperado: {message}"