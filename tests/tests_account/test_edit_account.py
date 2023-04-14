# -*- coding: utf-8 -*-
import pytest
from model.account import AccountData


@pytest.mark.usefixtures("create_account")
def test_edit_accounts(app):
    app.account_helper.edit_account(AccountData().test_data())
