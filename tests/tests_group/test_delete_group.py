# -*- coding: utf-8 -*-
from model.group import GroupData


def test_delete_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())
    app.group_helper.delete_group()
