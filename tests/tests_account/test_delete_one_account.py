# -*- coding: utf-8 -*-
from model.account import AccountData
from random import randrange


def test_delete_one_account(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())
    old_accounts = app.account_helper.get_accounts()

    index = randrange(len(old_accounts))
    app.account_helper.delete_account_by_index(index)
    new_accounts = app.account_helper.get_accounts()
    
    count_of_accounts_after_deleting = int(app.account_helper.get_count_of_accounts_from_home_page())

    assert len(old_accounts) == app.account_helper.count_of_accounts() + 1
    assert count_of_accounts_before_deleting == count_of_accounts_after_deleting + 1
    old_accounts[index:index + 1] = []
    assert sorted(new_accounts, key=AccountData.id_or_max) == sorted(old_accounts, key=AccountData.id_or_max)
