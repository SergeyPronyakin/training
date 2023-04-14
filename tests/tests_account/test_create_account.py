# -*- coding: utf-8 -*-
from model.account import AccountData


def test_create_account(app):
    app.account_helper.create_account(AccountData())
