import pytest


@pytest.mark.parametrize('param', [(0, 144), (5, 46368), (5, 144), (0, 56554)])
def test_short(client, param):
    resp = client.request(method='GET', path=f'/fibonacci/?from={param[0]}&to={param[1]}')
    assert isinstance(resp, dict)