from functools import wraps

from django.core.cache import cache

from fibonacci.apps.core.utils import logger


def cached_output(timeout: int, prefix=None):

    def decorator(func):

        @wraps(func)
        def inner(*args, **kwargs):
            _from = kwargs['_from']
            _to = kwargs['_to']
            cached = cache.get('result', None)
            if cached:
                logger.info('from cache')
                if cached[-1] == _to:
                    result = [item for item in cached if _from <= item]
                elif cached[-1] > _to:
                    result = [item for item in cached if _from <= item <= _to]
                else:
                    result = func(_from=_from, _to=_to, cached=cached)
                    if cached:
                        result = cached + result[2:]
                    cache.set('result', result, timeout)
                logger.info(result)
            else:
                result = func(_to=_to)
                cache.set('result', result, timeout)
                logger.info('from generator')
            return result[result.index(_from):]

        return inner

    return decorator
