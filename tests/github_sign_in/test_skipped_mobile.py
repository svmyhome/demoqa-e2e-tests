import os

import pytest
from selene import by, be
from selene.support.shared import browser


def test_singin_web(browser_web):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)


def test_singin_mobile(browser_mobile):
    if browser.config.window_width == 390 and browser.config.window_height == 844:
        pytest.skip(
            reason=f'Тест не предназначен для мобильного разрешения {browser.config.window_width} * {browser.config.window_height}'
        )
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)


@pytest.mark.parametrize(
    ['window_width', 'window_height'],
    [
        pytest.param(1900, 1300),
        pytest.param(
            390,
            844,
            marks=[
                pytest.mark.skip(
                    f'The test is not suitable for {browser.config.window_width} * {browser.config.window_height} resolution'
                )
            ],
        ),
    ],
    ids=["Web resolution", "Mobile resolution"],
)
def test_with_param3(window_width, window_height):
    print(window_width)
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)
