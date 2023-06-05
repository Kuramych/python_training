from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
        self.contact_cache = None

    def init_contact_creation(self):
        wd = self.app.wd
        # init contact creation
        wd.find_element("link text", "add new").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        wd.find_elements("name", "selected[]")[index].click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.home_page()
        # select all group
        wd.find_element(By.ID, "MassCB").click()
        # submit deletion
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def home_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.NAME, "searchstring")) > 0:
            return
        wd.find_element("link text", "home").click()

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.update_contact()
        self.contact_cache = None

    def modify_random_contact(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        self.update_contact()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                      all_phones_from_home_page=all_phones, address=address,
                                                  all_emails=all_emails))

        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        element = wd.find_elements(By.NAME, "entry")[index]
        cell = element.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.home_page()
        element = wd.find_elements(By.NAME, "entry")[index]
        cell = element.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        home = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home,
                       mobile=mobile, work=work, phone2=phone2, address=address, email=email, email2=email2,
                       email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        #self.home_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()
        wd.find_element("xpath", "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(int(id))
        self.fill_contact_form(new_contact_data)
        self.update_contact()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.home_page()
        element = wd.find_elements(By.NAME, "entry")[id]
        cell = element.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

