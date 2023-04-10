from fixture.application import Application
import pytest

from model.account import AccountData
from model.group import GroupData
from model.user import UserData


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit)
    return fixture


@pytest.fixture
def create_account(app):
    app.session.login(UserData().username, UserData().password)
    app.account_helper.create_account(AccountData())
    app.account_helper.return_to_the_home_page()
    app.session.logout()


@pytest.fixture
def create_group(app):
    app.session.login(UserData().username, UserData().password)
    app.group_helper.create_group(GroupData())
    app.group_helper.return_to_the_group_page()
    app.session.logout()
