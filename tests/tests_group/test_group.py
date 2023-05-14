# -*- coding: utf-8 -*-
from model.group import GroupData
from random import randrange


def test_create_group(app, json_groups):
    group = json_groups
    old_group_list = app.group_helper.get_groups()

    app.group_helper.create_group(group)

    new_group_list = app.group_helper.get_groups()
    assert app.group_helper.count_of_groups() == len(old_group_list) + 1
    old_group_list.append(group)
    assert sorted(new_group_list, key=GroupData.id_or_max) == sorted(old_group_list, key=GroupData.id_or_max)


def test_edit_some_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData(name="name", footer="footer", header="header"))

    group = GroupData(name="assert_name")
    old_groups = app.group_helper.get_groups()
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group_helper.edit_group_by_index(group, index)
    new_groups = app.group_helper.get_groups()

    assert len(old_groups) == app.group_helper.count_of_groups()
    old_groups[index] = group
    assert sorted(old_groups, key=GroupData.id_or_max) == sorted(new_groups, key=GroupData.id_or_max)


def test_delete_some_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())

    old_groups = app.group_helper.get_groups()

    index = randrange(len(old_groups))
    app.group_helper.delete_group_by_index(index)

    new_groups = app.group_helper.get_groups()

    assert len(old_groups) - 1 == app.group_helper.count_of_groups()
    old_groups[index:index + 1] = []
    assert old_groups == new_groups


def test_delete_all_group(app):
    if not app.group_helper.count_of_groups():
        app.group_helper.create_group(GroupData())
    app.group_helper.delete_all_group()

    assert app.group_helper.count_of_groups() == 0
