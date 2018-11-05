import pytest
from django.core.exceptions import SuspiciousOperation

from fibonacci.apps.core.utils import fibo

f = iter(fibo())


@pytest.mark.parametrize('param', (0, 1, 1, 2, 3, 5, 8, 13, 21))
def test_base(param):
    assert next(f) == param


@pytest.mark.parametrize('serializer', [
    (1, 144),
    ('5', '89'),
], indirect=True)
def test_serializer(serializer):
    data = serializer.validate()
    assert isinstance(data['from'], int)
    assert isinstance(data['to'], int)


@pytest.mark.parametrize('serializer', [(-1, 144)], indirect=True)
def test_serializer(serializer):
    data = serializer.validate()
    assert isinstance(data['from'], int)
    assert data['from'] == 1


@pytest.mark.parametrize('serializer', [
    (2, 'qwe'),
    ('123', 'qwe'),
    ('qwe', 144),
], indirect=True)
def test_serializer_failed(serializer):
    with pytest.raises(SuspiciousOperation):
        serializer.validate()

