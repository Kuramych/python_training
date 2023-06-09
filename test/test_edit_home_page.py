import re
from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == several_spaces(contact_from_edit_page.address)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert clear(contact_from_home_page.all_emails) == merge_emails_like_on_home_page(contact_from_edit_page)


def test_compare_inf_from_home_and_database(app, db):
    contacts_from_database = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for contact_from_home_page, contact_from_database in zip(contacts_from_home_page, contacts_from_database):
        assert clear(contact_from_home_page.firstname) == clear(contact_from_database.firstname)
        assert clear(contact_from_home_page.lastname) == clear(contact_from_database.lastname)
        assert clear(contact_from_home_page.address) == clear(contact_from_database.address)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_database)
        assert clear(contact_from_home_page.all_emails) == merge_emails_like_on_home_page(contact_from_database)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    s = re.sub("[() -]", "", s)
    return s


def several_spaces(s):
    return re.sub(r"\s{2,}", " ", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))
