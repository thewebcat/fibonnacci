from django.http import JsonResponse
from django.views.generic.base import View

from fibonacci.apps.core.decorators import cached_output
from fibonacci.apps.core.serializers import FiboSerializer
from fibonacci.apps.core.utils import fibo


class FiboView(View):

    @staticmethod
    @cached_output(60 * 60)
    def fibo_generator(_to: int, _from=0, cached=None) -> list:
        params = dict(start=cached[-2], tmp=cached[-1]) if cached else {}
        result = []
        for item in fibo(**params):
            if _from <= item <= _to:
                result.append(item)
            else:
                if item > _to:
                    break
        return result

    def get(self, request) -> object:
        serializer = FiboSerializer(data=request.GET)
        data = serializer.validate()
        result = self.fibo_generator(_from=data['from'], _to=data['to'])
        return JsonResponse({'result': result})
