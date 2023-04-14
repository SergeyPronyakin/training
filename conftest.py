from fixture.application import Application
import pytest

from model.account import AccountData
from model.group import GroupData
from model.user import UserData


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    fixture.session.login(UserData())

    def fin():
        fixture.session.logout()
        fixture.quit()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def create_account(app):
    app.account_helper.create_account(AccountData())
    app.account_helper.return_to_the_home_page()


@pytest.fixture
def create_group(app):
    app.group_helper.create_group(GroupData())
    app.group_helper.return_to_the_group_page()
