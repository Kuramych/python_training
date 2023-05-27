from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import Contact


class Contact_helper:
    def __init__(self, app):
        self.app = app

    def enter_contact(self):
        wd = self.app.wd
        # Enter new contact
        wd.find_element("name", "submit").click()

    def update_contact(self):
        wd = self.app.wd
        # Enter new contact
        wd.find_element("name", "update").click()

    def create_contact(self, contact):
        self.home_page()
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.enter_contact()

    def init_contact_creation(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element("link text", "add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.home_page()
        wd.find_element("name", "selected[]").click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.home_page()
        # select all group
        wd.find_element(By.ID, "MassCB").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def home_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.NAME, "searchstring")) > 0:
            return
        wd.find_element("link text", "home").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.home_page()
        wd.find_element("xpath", "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        self.update_contact()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_with_visible_value("bday", contact.bday)
        self.change_field_with_visible_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_with_visible_value("aday", contact.aday)
        self.change_field_with_visible_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def change_field_with_visible_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            Select(wd.find_element("name", field_name)).select_by_visible_text(text)

    def count(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.home_page()
        contacts = []
        for element in (wd.find_elements(By.CSS_SELECTOR, "tr")[1:]):
            text = element.text
            id = element.find_element(By.NAME, "selected[]").get_attribute("value")
            lastname, firstname = text.split(' ')[0:2]
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts
