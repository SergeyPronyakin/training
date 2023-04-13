import pytest

from model.account import AccountData
from model.user import UserData


@pytest.mark.usefixtures("create_account")
def test_edit_accounts(app):
    app.session.login(UserData())
    app.account_helper.edit_account(AccountData().test_data())
    app.session.logout()
