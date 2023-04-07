# -*- coding: utf-8 -*-
from group import Group
from account import Account
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


user_data = Account()
group_data = Group()


def test_create_group(app):
    app.open_main_page()
    app.login(user_data.username, user_data.password)
    app.create_group(group_data)
    app.return_to_the_group_page()
    app.logout()
