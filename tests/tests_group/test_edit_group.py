# -*- coding: utf-8 -*-
from model.group import GroupData
from datetime import datetime


def test_edit_group(app):
    assert_name = "New name " + str(datetime.now())[:-7]

    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())

    old_group_list = app.group_helper.groups()
    app.group_helper.edit_group(assert_name)
    new_group_list = app.group_helper.groups()

    assert new_group_list[0].name == assert_name
    assert len(old_group_list) == app.group_helper.count_of_groups()
