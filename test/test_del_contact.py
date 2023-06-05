from model.contact import Contact
import random
import time
from random import randrange


def test_delete_first_contact(app, db, check_ui):
    time.sleep(4)
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    time.sleep(4)
    contact = random.choice(old_contacts)
    time.sleep(5)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contact_list()
    time.sleep(5)
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_first_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    time.sleep(5)
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []

#def test_delete_all_contacts(app):
 #   app.contact.delete_all_contacts()

