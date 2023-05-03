from fixture.application import Application
import pytest
from model.user import UserData

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        fixture.session.login(UserData(username="admin", password="secret"))
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
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


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/index.php")
