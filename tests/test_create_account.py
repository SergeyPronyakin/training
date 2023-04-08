# -*- coding: utf-8 -*-
from model.account import Account
from fixture.application import Application
import pytest
from fixture.session_helper import SessionHelper


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


user_data = Account()
account_helper = SessionHelper(app)


def test_create_account(app):
    app.session.login(user_data.username, user_data.password)
    app.session.create_account(user_data)
    app.session.logout()
