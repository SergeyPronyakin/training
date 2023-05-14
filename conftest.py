import json
import jsonpickle
import os.path
from fixture.application import Application
import pytest

from fixture.db import DbFixture
from model.user import UserData
import importlib

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=web_config["browser"], base_url=web_config["baseUrl"])
    fixture.session.ensure_login(UserData(username=web_config["username"], password=web_config["password"]))
    return fixture


@pytest.fixture(scope="session")
def db(request):
    web_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=web_config["host"], name=web_config["name"],
                          user=web_config["user"], password=web_config["password"])

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


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
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as json_file:
        return jsonpickle.decode(json_file.read())
