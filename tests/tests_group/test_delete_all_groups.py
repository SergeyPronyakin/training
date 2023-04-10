# -*- coding: utf-8 -*-
import pytest
from model.user import UserData


@pytest.mark.skip("Test is not ready for homework")
def test_delete_all_group(app):
    app.session.login(UserData().username, UserData().password)
    app.group_helper.delete_all_group()
    app.group_helper.return_to_the_group_page()
    app.session.logout()

