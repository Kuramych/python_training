from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="New_name"))


def test_edit_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(bday="1"))


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact("adsad", "sfdsdf", "vxcxv", "hfghfgh", "xcvvx", "fjhfgjf", "cxzczcxzv", "chcnvc",
                               "dsfdsdf", "qewter", "jkghjgjg", "cbvbcncn", "fghfhfghf", "asdasad", "vbxcnbn", "1",
                               "April", "2000", "4", "February", "2010", "gfdgdg", "bvcbcbv", "gfdgdgdg"))
