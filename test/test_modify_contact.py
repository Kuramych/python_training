from model.contact import Contact


def test_modify_contact_firstname(app):
    app.fixture_contact.session.login(username="admin", password="secret")
    app.fixture_contact.contact.modify_first_contact(Contact(firstname="New_name"))
    app.fixture_contact.session.logout()


def test_edit_contact_bday(app):
    app.fixture_contact.session.login(username="admin", password="secret")
    app.fixture_contact.contact.modify_first_contact(Contact(bday="1"))
    app.fixture_contact.session.logout()

