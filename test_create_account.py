# -*- coding: utf-8 -*-
from account import Account
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


user_data = Account()


def test_untitled_test_case(app):
    app.open_main_page()
    app.login(user_data.username, user_data.password)
    app.create_account(user_data)
    app.logout()
