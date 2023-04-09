# -*- coding: utf-8 -*-
from model.account import UserData


def test_delete_accounts(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.delete_accounts()
    app.session.logout()
