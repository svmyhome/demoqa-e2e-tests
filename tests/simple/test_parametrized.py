import pytest


@pytest.mark.parametrize('browser', ['Chrome', 'Firefox'])
def test_parametrized(browser):
    pass


@pytest.mark.parametrize('browser, test_user', [('Chrome', '100'), ('Firefox', '200')])
def test_parametrized_1(browser, test_user):
    pass


@pytest.mark.parametrize(
    'browser, test_user',
    [('Chrome', 100), ('Firefox', 200)],
    ids=['Description by first tuple', 'Description by second tuple'],
)
def test_parametrized_2(browser, test_user):
    pass


@pytest.mark.parametrize('browser', ['Chrome', 'Firefox'])
@pytest.mark.parametrize(
    'test_user',
    [100, 200],
    ids=['Description by first tuple', 'Description by second tuple'],
)
def test_parametrized_3(browser, test_user):
    pass
