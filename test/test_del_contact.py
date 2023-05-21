def test_delete_first_contact(app):
    app.fixture_contact.session.login(username="admin", password="secret")
    app.fixture_contact.contact.delete_first_contact()
    app.fixture_contact.session.logout()
