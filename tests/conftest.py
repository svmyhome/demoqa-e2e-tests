import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_managment():

    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'


@pytest.fixture(scope='function')
def browser_web(browser_managment):
    browser.config.window_width = 1900
    browser.config.window_height = 1300


@pytest.fixture(scope='function')
def browser_mobile(browser_managment):
    browser.config.window_width = 390
    browser.config.window_height = 844
