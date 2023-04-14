# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures("create_account")
def test_delete_all_accounts(app):
    app.account_helper.delete_all_accounts()

