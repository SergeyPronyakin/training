# -*- coding: utf-8 -*-
from model.account import AccountData


def test_delete_all_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())
    app.account_helper.delete_all_accounts()

