# -*- coding: utf-8 -*-
from model.group import GroupData
from model.user import UserData


def test_create_group(app):
    app.session.login(UserData())
    app.group_helper.create_group(GroupData())
    app.group_helper.return_to_the_group_page()
    app.session.logout()
