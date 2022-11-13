import pytest

from utils.base_session import BaseSession


@pytest.fixture(scope='session')
def reqres_session():
    with BaseSession(base_url='https://reqres.in') as session:
        yield session


@pytest.fixture(scope='session')
def shop_session():
    with BaseSession(base_url='https://demowebshop.tricentis.com') as session:
        yield session
