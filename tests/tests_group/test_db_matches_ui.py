from model.group import GroupData


def test_group_list(app, db):
    groups_from_ui = app.group_helper.get_groups()

    def clean(group):
        return GroupData(id=group.id, name=group.name.strip())

    groups_from_db = map(clean, db.get_groups())

    assert sorted(groups_from_ui, key=GroupData.id_or_max) == sorted(groups_from_db, key=GroupData.id_or_max)
