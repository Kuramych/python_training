from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    def clean(group):
        return Group(id=group.id, name=group.name.replace(" ", ""))

    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    print(timeit(lambda: map(clean, app.group.get_group_list()), number=1))
    assert False #sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
