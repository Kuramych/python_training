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
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element("name", "submit").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        # open group page
        wd.find_element("link text", "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element("name", "selected[]").click()
        # submit deletion
        wd.find_element("name", "delete").click()
        self.return_to_group_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element("name", "selected[]").click()
        wd.find_element("name", "edit").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        wd.find_element("name", "update").click()
        self.return_to_group_page()