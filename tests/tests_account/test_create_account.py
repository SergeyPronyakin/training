# -*- coding: utf-8 -*-
from model.account import AccountData
from model.user import UserData


def test_create_account(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.create_account(AccountData())
    app.account_helper.return_to_the_home_page()
    app.session.logout()
