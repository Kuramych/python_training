import pytest
from fixture.application_group import Application_group
from fixture.application_contact import Application_contact


@pytest.fixture(scope="session")
def app(request):
    class App:
        def __init__(self):
            self.fixture_group = Application_group()
            self.fixture_contact = Application_contact()

        def destroy(self):
            self.fixture_group.destroy()
            self.fixture_contact.destroy()

        def fin(self):
            self.fixture_group.session.logout()
            self.fixture_contact.session.logout()
            self.fixture_group.destroy()
            self.fixture_contact.destroy()

    fixture = App()
    fixture.fixture_group.session.login(username="admin", password="secret")
    fixture.fixture_contact.session.login(username="admin", password="secret")
    request.addfinalizer(fixture.fin)
    return fixture