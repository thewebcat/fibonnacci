import os
import django
import pytest
from django.conf import settings
from django.core.cache import cache

from fibonacci.apps.core.serializers import FiboSerializer


@pytest.fixture
def serializer(request):
    return FiboSerializer(data={'from': request.param[0], 'to': request.param[1]})


@pytest.fixture(scope='module', autouse=True)
def redis_clean():
    cache.clear()


# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fibonacci.config.settings')


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    # If you have any test specific settings, you can declare them here,
    # e.g.
    # settings.PASSWORD_HASHERS = (
    #     'django.contrib.auth.hashers.MD5PasswordHasher',
    # )
    django.setup()
    # Note: In Django =< 1.6 you'll need to run this instead
    # settings.configure()
