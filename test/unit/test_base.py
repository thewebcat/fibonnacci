from fibonacci.apps.core.utils import fibo


def test_base():
    f = iter(fibo())
    assert next(f) == 0
    assert next(f) == 1
    assert next(f) == 1
    assert next(f) == 2
    assert next(f) == 3
    assert next(f) == 5
    assert next(f) == 8


