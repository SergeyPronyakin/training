# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


def test_create_group(app):
    app.open_main_page()
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_name", header="header", footer="footer"))
    app.return_to_the_group_page()
    app.logout()
