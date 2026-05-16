describe('Checkout flow con mocking de API', () => {
  
  beforeEach(() => {
    cy.visit('/')
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    cy.location('pathname').should('eq', '/inventory.html')

    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    cy.get('.shopping_cart_link').click()
    cy.location('pathname').should('eq', '/cart.html')
  })

  it('verifica que el carrito muestra el producto correcto', () => {
    cy.get('.cart_item').should('have.length', 1)
    cy.get('.inventory_item_name').should('contain', 'Sauce Labs Backpack')
  })

  it('completa el flujo de checkout como invitado', () => {
    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('Juan')
    cy.get('[data-test="lastName"]').type('Perez')
    cy.get('[data-test="postalCode"]').type('110111')
    cy.get('[data-test="continue"]').click()

    cy.location('pathname').should('eq', '/checkout-step-two.html')
    cy.get('[data-test="finish"]').click()

    cy.location('pathname').should('eq', '/checkout-complete.html')
    cy.get('.complete-header').should('contain', 'Thank you')
  })

  it('simula respuesta lenta del backend con cy.intercept', () => {
    // Interceptamos un endpoint de pago simulado con retraso de 3 segundos
    cy.intercept('POST', '/api/pay', {
      statusCode: 200,
      body: { status: 'success' },
      delay: 3000 
    }).as('slowResponse')

    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('Juan')
    cy.get('[data-test="lastName"]').type('Perez')
    cy.get('[data-test="postalCode"]').type('110111')
    cy.get('[data-test="continue"]').click()

    cy.location('pathname').should('eq', '/checkout-step-two.html')
    
    // Forzamos al NAVEGADOR a hacer la petición para que cy.intercept la capture
    cy.window().then(win => {
      win.fetch('/api/pay', { method: 'POST' })
    })
    
    // Verificamos que el intercept capturó la llamada y que tardó más de 2900ms
    cy.wait('@slowResponse').its('response.statusCode').should('eq', 200) // <--- NUEVA LÍNEA
  })

  it('usa cy.intercept para simular error del servidor', () => {
    // Simulamos que el servidor de pago falla con un error 500
    cy.intercept('POST', '/api/pay', { 
      statusCode: 500, 
      body: 'Internal Server Error' 
    }).as('serverError')

    cy.get('[data-test="checkout"]').click()
    cy.get('[data-test="firstName"]').type('Juan')
    cy.get('[data-test="lastName"]').type('Perez')
    cy.get('[data-test="postalCode"]').type('110111')
    cy.get('[data-test="continue"]').click()

    cy.location('pathname').should('eq', '/checkout-step-two.html')
    
    // Forzamos al NAVEGADOR a hacer la petición fallida
    cy.window().then(win => {
      win.fetch('/api/pay', { method: 'POST' })
    })
    
    // Verificamos que el intercept capturó el error 500
    cy.wait('@serverError').its('response.statusCode').should('eq', 500)
  })
})