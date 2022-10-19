import pytest
from selene import be
from selene.support.shared import browser


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
    browser.config.window_width = window_width
    browser.config.window_height = window_height
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)


@pytest.fixture(params=[390])
def browser_manager(request):
    browser.config.window_width = request.param
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://github.com/'
    return request.param


@pytest.fixture(params=[844])
def browser_height(request):
    browser.config.window_height = request.param
    return request.param


def test_parametrization(browser_manager, browser_height):
    browser.open('')
    browser.element('.Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)


@pytest.mark.parametrize('browser_manager', [1900], indirect=True)
@pytest.mark.parametrize('browser_height', [1300], indirect=True)
def test_with_indirect_parametrization(browser_manager, browser_height):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(be.visible)
