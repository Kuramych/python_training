from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.delete_first_contact()


#def test_delete_all_contacts(app):
 #   app.contact.delete_all_contacts()
