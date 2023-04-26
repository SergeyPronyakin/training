# -*- coding: utf-8 -*-
from model.group import GroupData
from random import randrange


def test_delete_some_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())

    old_groups = app.group_helper.groups()

    index = randrange(len(old_groups))
    app.group_helper.delete_group_by_index(index)

    new_groups = app.group_helper.groups()

    assert len(old_groups) - 1 == app.group_helper.count_of_groups()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
