# -*- coding: utf-8 -*-
import pytest

from model.account import UserData


@pytest.mark.skip("Test is not ready")
def test_delete_all_accounts(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.delete_all_accounts()
    app.session.logout()
