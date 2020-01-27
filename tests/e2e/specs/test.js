// https://docs.cypress.io/api/introduction/api.html

describe('The login page', () => {
  it('Visits the app root url', () => {
    cy.visit('/login');
    cy.get('.headline').contains('Sign in');
  });

  it('Knows what true us', () => expect(true).to.equal(true));
});
