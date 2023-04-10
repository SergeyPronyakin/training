import pytest
from model.user import UserData


@pytest.mark.usefixtures("create_account")
def test_delete_accounts(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.edit_account()
    app.session.logout()
