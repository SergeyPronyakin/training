# -*- coding: utf-8 -*-
from model.account import AccountData


def test_create_account(app):
    account_data = AccountData()
    old_accounts = app.account_helper.get_accounts()
    app.account_helper.create_account(account_data)
    new_accounts = app.account_helper.get_accounts()

    assert app.account_helper.count_of_accounts() == len(old_accounts) + 1
    old_accounts.append(account_data)
    assert sorted(new_accounts, key=AccountData.id_or_max) == sorted(old_accounts, key=AccountData.id_or_max)


