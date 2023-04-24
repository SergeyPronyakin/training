from fixture.application import Application
import pytest

from model.account import AccountData
from model.group import GroupData
from model.user import UserData

fixture = None


@pytest.fixture
def app():
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(UserData(username="admin", password="secret"))
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(UserData(username="admin", password="secret"))
    fixture.session.ensure_login(UserData(username="admin", password="secret"))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
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
