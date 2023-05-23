from model.contact import Contact


def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New_name"))


def test_edit_contact_bday(app):
    app.contact.modify_first_contact(Contact(bday="1"))


