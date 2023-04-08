# -*- coding: utf-8 -*-
from model.group import GroupData
from model.account import UserData
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


def test_create_group(app):
    app.session.login(UserData().username, UserData().password)
    app.group_helper.create_group(GroupData())
    app.group_helper.return_to_the_group_page()
    app.session.logout()
