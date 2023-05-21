def test_delete_first_group(app):
    app.fixture_group.session.login(username="admin", password="secret")
    app.fixture_group.group.delete_first_group()
    app.fixture_group.session.logout()


