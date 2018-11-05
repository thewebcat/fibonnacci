from django.http import JsonResponse
from django.views.generic.base import View

from fibonacci.apps.core.serializers import FiboSerializer


class FiboView(View):
    def get(self, request) -> object:
        serializer = FiboSerializer(data=request.GET)
        data = serializer.validate()
        return JsonResponse({'data': data})
