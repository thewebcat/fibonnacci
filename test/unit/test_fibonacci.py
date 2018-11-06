import json

import pytest
from django.http import JsonResponse
from django.test import RequestFactory

from fibonacci.apps.core.views import FiboView

request_factory = RequestFactory()


@pytest.mark.parametrize('param', [(0, 144), (1, 144), (5, 28657), (5, 144), (0, 46368)])
def test_short(param):
    request = request_factory.get('/fibonacci/', data={'from': param[0], 'to': param[1]})
    response = FiboView.as_view()(request)
    assert response.status_code == 200
    assert isinstance(response, JsonResponse)
    assert 'result' in response.content.decode()
    assert json.loads(response.content.decode())['result'][-1] == param[1]
