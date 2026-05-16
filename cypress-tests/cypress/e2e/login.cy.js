describe('Login flow', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('hace login con credenciales válidas', () => {
    cy.get('[data-test="username"]').type('standard_user')
    cy.get('[data-test="password"]').type('secret_sauce')
    cy.get('[data-test="login-button"]').click()
    cy.location('pathname').should('eq', '/inventory.html')
  })

  it('muestra error con credenciales inválidas', () => {
    cy.get('[data-test="username"]').type('usuario_invalido')
    cy.get('[data-test="password"]').type('mala_contraseña')
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="error"]').should('be.visible')
  })

  it('no permite login con campos vacíos', () => {
    cy.get('[data-test="login-button"]').click()
    cy.get('[data-test="error"]').should('be.visible')
  })
})