# -*- coding: utf-8 -*-
from model.group import GroupData
from datetime import datetime
from random import randrange


def test_edit_some_group(app):
    assert_name = "New name " + str(datetime.now())[:-7]

    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())

    group = GroupData(name=assert_name)
    old_groups = app.group_helper.groups()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group_helper.edit_group_by_index(group, index)
    new_groups = app.group_helper.groups()

    assert len(old_groups) == app.group_helper.count_of_groups()
    old_groups[index] = group
    assert sorted(old_groups, key=GroupData.id_or_max) == sorted(new_groups, key=GroupData.id_or_max)
