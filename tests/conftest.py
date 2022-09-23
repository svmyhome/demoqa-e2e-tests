import os

import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 5
    # browser.config.wait_for_no_overlap_found_by_js = True  # Ждет скрытия оверлеев при открытии окна. Не работает с невидимыми полями ввода например при загрузке файла через input
    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
    browser.config.window_width = 1900
    browser.config.window_height = 1300

    yield
