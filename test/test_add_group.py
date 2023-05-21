from model.group import Group


def test_add_group(app_group):
    app_group.session.login(username="admin", password="secret")
    app_group.group.create_group(Group(name="adfsfas", header="asfasfafs", footer="asfasfas"))
    app_group.session.logout()


def test_add_empty_group(app_group):
    app_group.session.login(username="admin", password="secret")
    app_group.group.create_group(Group(name="", header="", footer=""))
    app_group.session.logout()


