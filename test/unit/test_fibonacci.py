import pytest
from django.http import JsonResponse
from django.test import RequestFactory

from fibonacci.apps.core.views import FiboView


@pytest.mark.parametrize('param', [(0, 144), (1, 144), (5, 46368), (5, 144), (0, 56554)])
def test_short(param):
    request_factory = RequestFactory()
    request = request_factory.get('/fibonacci/', data=dict(_from=param[0], _to=param[1]))
    view = FiboView.as_view()
    response = view(request)
    assert response.status_code == 200
    assert isinstance(response, JsonResponse)
    assert 'result' in response.content.decode()
