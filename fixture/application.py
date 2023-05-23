from selenium import webdriver
from fixture.session import Session_helper
from fixture.contact import Contact_helper
from fixture.group import Group_helper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome(executable_path=r'')
        self.wd.implicitly_wait(5)
        self.session = Session_helper(self)
        self.contact = Contact_helper(self)
        self.group = Group_helper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.wd.quit()
