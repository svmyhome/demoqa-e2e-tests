import os

import pytest


@pytest.mark.skip(reason='Task1 Сломано окружение тест не проходит')
def test_skipped_1():
    pass


@pytest.mark.skip(reason='Task-1 Сломано окружение тест не проходит')
def test_skipped_2():
    pass


def test_skipped_3():
    if os.getenv("OS1") == "Linux":
        pytest.skip(reason='Тест не предназначен для Linux')
    pass


def test_skipped_4():
    if os.getenv("OS1") == "Linux1":
        pytest.skip(reason='Тест не предназначен для Linux')
    pass


@pytest.mark.xfail(reason='BUG-1', strict=True)
def test_xfail():
    assert False
