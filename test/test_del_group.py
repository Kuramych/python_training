def test_delete_first_group(app_group):
    app_group.session.login(username="admin", password="secret")
    app_group.group.delete_first_group()
    app_group.session.logout()
