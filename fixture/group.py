from selenium.webdriver.common.by import By
from model.group import  Group


class Group_helper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element("link text", "group page").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element("name", "new").click()
        # fill group form
        self.fill_form_group(group)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def open_group_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0:
            return
        wd.find_element("link text", "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        wd.find_element("name", "delete").click()
        self.return_to_group_page()
        self.group_cache = None

    def submit_modification_group(self):
        wd = self.app.wd
        wd.find_element("name", "update").click()

    def fill_form_group(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def edit_group(self):
        wd = self.app.wd
        wd.find_element("name", "edit").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def modify_first_group(self, new_group_data):
        self.open_group_page()
        self.select_first_group()
        self.edit_group()
        self.fill_form_group(new_group_data)
        self.submit_modification_group()
        self.return_to_group_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


