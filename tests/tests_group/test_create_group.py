# -*- coding: utf-8 -*-
from model.group import GroupData


def test_create_group(app):
    app.group_helper.create_group(GroupData())
