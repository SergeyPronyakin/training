# -*- coding: utf-8 -*-
from model.group import GroupData


def test_create_group(app):
    group = GroupData()
    old_group_list = app.group_helper.groups()

    app.group_helper.create_group(group)

    new_group_list = app.group_helper.groups()
    assert len(new_group_list) == len(old_group_list) + 1
    old_group_list.append(group)
    assert sorted(new_group_list, key=GroupData.id_or_max) == sorted(old_group_list, key=GroupData.id_or_max)
