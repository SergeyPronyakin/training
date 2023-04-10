# -*- coding: utf-8 -*-
import pytest
from model.user import UserData


@pytest.mark.usefixtures("create_account")
def test_delete_all_accounts(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.delete_all_accounts()
    app.session.logout()

