from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create_group(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    if check_ui:
        assert sorted(map(clean, new_groups), key=Group.id_or_max) == sorted(map(clean, old_groups),
                                                                             key=Group.id_or_max)


def clean(group):
    return Group(id=group.id, name=group.name.replace(" ", ""))
