import os

import pytest
from selene.support.shared import browser
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import utils
from utils import attach_evidence


# @pytest.fixture(scope='function')
# def browser_management():
#     browser.config.timeout = 5
#     # browser.config.wait_for_no_overlap_found_by_js = True  # Ждет скрытия оверлеев при открытии окна. Не работает с невидимыми полями ввода например при загрузке файла через input
#     browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
#     browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#     browser.config.window_width = 1900
#     browser.config.window_height = 1300
#
#     yield


@pytest.fixture(scope='function')
def setup_chrom():
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {'enableVNC': True, 'enableVideo': True},
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor='https://user1:1234@selenoid.autotests.cloud//wd/hub',
        options=options,
    )
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.driver = driver

    yield

    attach_evidence.add_video(browser)
    attach_evidence.add_logs(browser)
    attach_evidence.add_html(browser)
    attach_evidence.add_screenshot(browser)
