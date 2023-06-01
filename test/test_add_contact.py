# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname=lastname, firstname=firstname, address=address,email=email, email2=email2,
                    email3=email3, home=home, work=work, phone2=phone2, mobile=mobile)
            for lastname in ["", random_string("lastname", 10)]
            for firstname in ["", random_string("firstname", 20)]
            for address in ["", random_string("footer", 20)]
            for email in ["", random_string("footer", 20)]
            for email2 in ["", random_string("footer", 20)]
            for email3 in ["", random_string("footer", 20)]
            for email3 in ["", random_string("footer", 20)]
            for home in ["", random_string("footer", 10)]
            for work in ["", random_string("footer", 10)]
            for phone2 in ["", random_string("footer", 10)]
            for mobile in ["", random_string("footer", 10)]]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)