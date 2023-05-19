from selenium import webdriver
from fixture.session import Session_helper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
        self.session = Session_helper(self)


    def return_to_group_page(self):
        wd = self.wd
        # return to groups page
        wd.find_element("link text", "group page").click()

    def create_group(self, group):
        wd = self.wd
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
        wd = self.wd
        # open group page
        wd.find_element("link text", "groups").click()



    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()