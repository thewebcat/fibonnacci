import pytest

from fibonacci.apps.core.views import FiboView


@pytest.mark.parametrize('param', [(0, 144), (5, 46368), (5, 144), (0, 56554)])
def test_short(param):
    resp = FiboView.fibo_generator(_from=param[0], _to=param[1])
    assert isinstance(resp, list)
    assert True
