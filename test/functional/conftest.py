import pytest

from test.functional.utils import Client


@pytest.fixture(scope='session')
def client():
    return Client(endpoint_url='http://test:8000')
