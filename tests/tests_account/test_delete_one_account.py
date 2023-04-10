# -*- coding: utf-8 -*-
from model.user import UserData


def test_delete_accounts(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.delete_one_account()
    app.session.logout()
