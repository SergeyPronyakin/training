# -*- coding: utf-8 -*-
from model.account import AccountData


def test_delete_all_accounts(app):
    if not app.account_helper.count_of_accounts():
        app.account_helper.create_account(AccountData())
    app.account_helper.delete_all_accounts()

    # New account text waiting for...
    # WebDriverWait(wd, 5).until(
    #     EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{account.firstname}')]")))
    #
    # # Assert first name at home page after updating
    # assert wd.find_element_by_xpath("//form[2]/table/tbody/tr[2]/td[3]").text == account.firstname
    # assert wd.find_element_by_xpath("//form[2]/table/tbody/tr[2]/td[5]").text == account.email

