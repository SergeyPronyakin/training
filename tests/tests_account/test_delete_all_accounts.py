# -*- coding: utf-8 -*-
from model.account import AccountData


def test_delete_all_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())

    count_of_accounts_before_deleting = int(app.account_helper.get_accounts_count_from_page())
    old_accounts = app.account_helper.accounts()

    app.account_helper.delete_all_accounts()

    count_of_accounts_after_deleting = int(app.account_helper.get_accounts_count_from_page())
    new_accounts = app.account_helper.accounts()

    assert len(old_accounts) > 0
    assert len(new_accounts) == 0
    assert count_of_accounts_before_deleting >= count_of_accounts_after_deleting
    assert count_of_accounts_after_deleting == 0
