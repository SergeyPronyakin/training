# -*- coding: utf-8 -*-
from model.account import AccountData


def test_acc(app):
    # app.account_helper.create_account(AccountData(firstname="Firstname", middlename="Midlename",
    #                                               lastname="Lastname", mobile="89160000101",
    #                                               email="test@gmail.com"))
    app.account_helper.accounts()
