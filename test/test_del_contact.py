def test_delete_first_contact(app):
    app.fixture_contact.contact.delete_first_contact()


def test_delete_all_contacts(app):
    app.fixture_contact.contact.delete_all_contacts()
