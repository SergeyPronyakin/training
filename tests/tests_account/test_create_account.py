# -*- coding: utf-8 -*-
from model.account import AccountData


def test_create_account(app):
    old_accounts = app.account_helper.accounts()
    app.account_helper.create_account(AccountData())
    new_accounts = app.account_helper.accounts()

    assert len(new_accounts) == len(old_accounts) + 1

