from model.group import Group
from random import randrange


def test_modify_group_name(app):
    group = Group(name="New_name")
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    group = Group(header="New_header")
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_rewrite_group(app):
    group = Group(name="123", header="3123", footer="213")
    if app.group.count() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


