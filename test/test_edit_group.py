from model.group import Group


def test_edit_group(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.edit_group(Group(name="adfsfas", header="asfasfafs", footer="asfasfas"))
    app.fixture_group.session.logout()
