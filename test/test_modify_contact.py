from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New_name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(bday="1"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_all_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact("adsad", "sfdsdf", "vxcxv", "hfghfgh", "xcvvx", "fjhfgjf", "cxzczcxzv", "chcnvc",
                               "dsfdsdf", "qewter", "jkghjgjg", "cbvbcncn", "fghfhfghf", "asdasad", "vbxcnbn", "1",
                               "April", "2000", "4", "February", "2010", "gfdgdg", "bvcbcbv", "gfdgdgdg"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
