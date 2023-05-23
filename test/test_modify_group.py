from model.group import Group


def test_modify_group_name(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.modify_first_group(Group(name="New_name"))
    app.fixture_group.session.logout()


def test_modify_group_header(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.modify_first_group(Group(header="New_header"))
    app.fixture_group.session.logout()


def test_rewrite_group(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.modify_first_group(Group(name="123", header="3123", footer="213"))
    app.fixture_group.session.logout()
