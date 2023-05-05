# -*- coding: utf-8 -*-

from model.account import AccountData


def test_test(app):
    app.account_helper.create_account(AccountData(firstname="FIRST", lastname="LAST",
                                                   address="address", home_phone="test", work_phone="work"))
    #                                               mobile="test", email="ee", email2="erer", email3="ssdsd"))
    print("TEST: " + str(app.account_helper.get_accounts()))
    #print("ID =====" + str(app.account_helper.get_account_by_id("1047")))
