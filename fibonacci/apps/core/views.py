from django.core.cache import cache
from django.http import JsonResponse
from django.views.generic.base import View

from fibonacci.apps.core.serializers import FiboSerializer
from fibonacci.apps.core.utils import fibo, logger


class FiboView(View):

    @staticmethod
    def _generator(_to: int, _from=0, cached=None) -> list:
        params = dict(start=cached[-2], tmp=cached[-1]) if cached else {}
        result = []
        for item in fibo(**params):
            if _from <= item <= _to:
                result.append(item)
            else:
                if item > _to:
                    break
        if cached:
            result = cached + result[2:]
        return result

    def _filtered_list(self, data: dict) -> list:
        _from = data['from']
        _to = data['to']
        cached = cache.get('result', None)
        if cached:
            logger.error(cached)
            if cached[-1] == _to:
                result = [item for item in cached if _from <= item]
            elif cached[-1] > _to:
                result = [item for item in cached if _from <= item <= _to]
            else:
                result = self._generator(_from, _to, cached)
                logger.error(result)
                cache.set('result', result)
        else:
            result = self._generator(_to)
            cache.set('result', result)
            result = result[result.index(_from):]
        return result

    def get(self, request) -> object:
        serializer = FiboSerializer(data=request.GET)
        data = serializer.validate()
        result = self._filtered_list(data)
        return JsonResponse({'result': result})
