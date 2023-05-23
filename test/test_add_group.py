from model.group import Group


def test_add_group(app):
    app.fixture_group.group.create_group(Group(name="adfsfas", header="asfasfafs", footer="asfasfas"))


def test_add_empty_group(app):
    app.fixture_group.group.create_group(Group(name="", header="", footer=""))


