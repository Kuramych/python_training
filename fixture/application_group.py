from selenium import webdriver
from fixture.session import Session_helper
from fixture.group import Group_helper


class Application_group:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(30)
        self.session = Session_helper(self)
        self.group = Group_helper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()