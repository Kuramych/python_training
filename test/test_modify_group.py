import random

from model.group import Group
from random import randrange


def test_modify_group_name(app, db, check_ui):
    group_modification = Group(name="New_name")
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_modification.id = group.id
    app.group.modify_group_by_id(group.id, group_modification)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[old_groups.index(group)] = group_modification
    if check_ui:
        assert sorted(map(clean, old_groups), key=Group.id_or_max) == sorted(map(clean, new_groups),
                                                                             key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    group_modification = Group(header="New_header")
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_modification.id = group.id
    app.group.modify_group_by_id(group.id, group_modification)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(map(clean, old_groups), key=Group.id_or_max) == sorted(map(clean, new_groups),
                                                                             key=Group.id_or_max)

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


def clean(group):
    return Group(id=group.id, name=group.name.replace(" ", ""))
