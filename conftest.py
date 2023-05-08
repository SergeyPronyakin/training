import json
import os.path
from fixture.application import Application
import pytest
from model.user import UserData
import importlib

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=target["browser"], base_url=target["baseUrl"])
        fixture.session.login(UserData(username=target["username"], password=target["password"]))
    fixture.session.ensure_login(UserData(username=target["username"], password=target["password"]))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.quit()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

