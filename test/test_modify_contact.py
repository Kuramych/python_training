from model.contact import Contact
import random
from random import randrange



def test_modify_contact_firstname(app, db, check_ui):
    contact_modification = Contact(firstname="New_name")
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modification.id = contact.id
    app.contact.modify_contact_by_id(contact.id, contact_modification)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[old_contacts.index(contact)] = contact_modification
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    contact = Contact(firstname="New_name")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_random_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    contact = Contact(bday="1")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_random_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_all_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="Test"))
    contact = Contact("adsad", "sfdsdf", "vxcxv", "hfghfgh", "xcvvx", "fjhfgjf", "cxzczcxzv", "chcnvc",
                               "dsfdsdf", "qewter", "jkghjgjg", "cbvbcncn", "fghfhfghf", "asdasad", "vbxcnbn", "1",
                               "April", "2000", "4", "February", "2010", "gfdgdg", "bvcbcbv", "gfdgdgdg")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_random_contact(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
