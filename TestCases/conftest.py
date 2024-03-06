from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ##################################### PyTest HTML Report #####################################
def pytest_configure(config):
    config.option.project_name = 'ProctorTracK'
    config.option.module_name = 'Instructor'
    config.option.tester = 'Prasad'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
