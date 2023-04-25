# -*- coding: utf-8 -*-
from model.account import AccountData


def test_edit_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())
    app.account_helper.edit_account(AccountData().test_data())
