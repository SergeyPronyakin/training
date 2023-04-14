# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures("create_account")
def test_delete_one_account(app):
    app.account_helper.delete_one_account()