# -*- coding: utf-8 -*-
from fixture.application import Application
from model.account import AccountData


def test_delete_one_account(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData(firstname="Firstname", middlename="Midlename", lastname="Lastname",
                                                  mobile="89160000101", email="test@gmail.com"))
    app.account_helper.delete_one_account()
