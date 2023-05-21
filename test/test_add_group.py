from model.group import Group


def test_add_group(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.create_group(Group(name="adfsfas", header="asfasfafs", footer="asfasfas"))
    app.fixture_group.session.logout()


def test_add_empty_group(app ):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.create_group(Group(name="", header="", footer=""))
    app.fixture_group.session.logout()


