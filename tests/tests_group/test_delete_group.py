# -*- coding: utf-8 -*-
import pytest


@pytest.mark.usefixtures("create_group")
def test_delete_group(app):
    app.group_helper.delete_group()
    app.group_helper.return_to_the_group_page()
