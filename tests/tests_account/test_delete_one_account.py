# -*- coding: utf-8 -*-
from fixture.application import Application
from model.account import AccountData


def test_delete_one_account(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())
    app.account_helper.delete_one_account()
