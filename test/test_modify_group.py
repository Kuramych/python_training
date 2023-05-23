from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New_name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New_header"))


def test_rewrite_group(app):
    app.group.modify_first_group(Group(name="123", header="3123", footer="213"))

