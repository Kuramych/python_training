import pytest
from fixture.application_group import Application_group
from fixture.application_contact import Application_contact

@pytest.fixture(scope = "session")
def app_group(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture
@pytest.fixture(scope = "session")
def app_contact(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture
