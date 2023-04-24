# -*- coding: utf-8 -*-
from model.group import GroupData


def test_delete_all_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData(name="Groupname", header="Header", footer="Footer"))
    app.group_helper.delete_all_group()

    group_list = app.group_helper.groups()
    assert len(group_list) == 0

