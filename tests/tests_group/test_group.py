# -*- coding: utf-8 -*-
import random

from model.group import GroupData


def test_create_group(app, db, json_groups):
    group = json_groups
    old_group_list = db.get_groups()
    app.group_helper.create_group(group)
    new_group_list = db.get_groups()
    old_group_list.append(group)
    assert sorted(new_group_list, key=GroupData.id_or_max) == sorted(old_group_list, key=GroupData.id_or_max)


def test_edit_some_group(app, db):
    if not db.get_groups():
        app.group_helper.create_group(GroupData(name="name", footer="footer", header="header"))

    old_groups = db.get_groups()
    group = random.choice(old_groups)
    edition_group_index = old_groups.index(group)
    edition_group = app.group_helper.edit_group_by_id(GroupData(name="assert_name", footer="footer_test"), group.id)
    new_groups = db.get_groups()

    edition_group = GroupData(id=group.id, name=edition_group.name,
                              footer=edition_group.footer, header=group.header)

    assert len(old_groups) == app.group_helper.count_of_groups()
    old_groups[edition_group_index] = edition_group
    assert sorted(old_groups, key=GroupData.id_or_max) == sorted(new_groups, key=GroupData.id_or_max)


def test_delete_some_group(app, db):
    if not db.get_groups():
        app.group_helper.create_group(GroupData())

    old_groups = db.get_groups()
    group = random.choice(old_groups)
    app.group_helper.delete_group_by_id(group.id)
    new_groups = db.get_groups()
    old_groups.remove(group)

    assert sorted(old_groups, key=GroupData.id_or_max) == sorted(new_groups, key=GroupData.id_or_max)


def test_delete_all_group(app, db):
    if not db.get_groups():
        app.group_helper.create_group(GroupData())
    app.group_helper.delete_all_group()

    assert app.group_helper.count_of_groups() == 0
    assert len(db.get_groups()) == 0
