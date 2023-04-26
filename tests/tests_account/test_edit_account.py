# -*- coding: utf-8 -*-
import random
import string
from model.account import AccountData


def test_edit_accounts(app):
    assert_data = ''.join(random.choices(string.ascii_lowercase, k=5))
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    old_accounts = app.account_helper.accounts()
    account_data = AccountData(firstname=assert_data, lastname=assert_data)
    account_data.id = old_accounts[0].id

    app.account_helper.edit_account(account_data)
    new_accounts = app.account_helper.accounts()
    old_accounts[0] = account_data

    assert sorted(old_accounts, key=AccountData.id_or_max) == sorted(new_accounts, key=AccountData.id_or_max)


