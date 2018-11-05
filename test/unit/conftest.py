import pytest

from fibonacci.apps.core.serializers import FiboSerializer


@pytest.fixture
def serializer(request):
    return FiboSerializer(data={'from': request.param[0], 'to': request.param[1]})
