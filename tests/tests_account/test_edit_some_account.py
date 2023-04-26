# -*- coding: utf-8 -*-
from random import randrange
import random
import string
from model.account import AccountData


def test_edit_some_accounts(app):
    assert_data = ''.join(random.choices(string.ascii_lowercase, k=5))
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    old_accounts = app.account_helper.accounts()
    index = randrange(len(old_accounts))
    account_data = AccountData(firstname=assert_data, lastname=assert_data)
    account_data.id = old_accounts[index].id

    app.account_helper.edit_some_account_by_index(account_data, index)
    new_accounts = app.account_helper.accounts()
    old_accounts[index] = account_data

    assert sorted(old_accounts, key=AccountData.id_or_max) == sorted(new_accounts, key=AccountData.id_or_max)
