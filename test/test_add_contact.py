# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="vxcxv", firstname="adsad")
    app.contact.create_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)