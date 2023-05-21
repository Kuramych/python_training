def test_delete_first_contact(app_contact):
    app_contact.session.login(username="admin", password="secret")
    app_contact.contact.delete_first_contact()
    app_contact.session.logout()
