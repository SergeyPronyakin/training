# -*- coding: utf-8 -*-
from model.account import UserData
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


def test_create_account(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.create_account(UserData())
    app.session.logout()
