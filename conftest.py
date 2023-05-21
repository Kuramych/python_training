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
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture