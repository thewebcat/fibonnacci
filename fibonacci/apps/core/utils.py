import logging

logger = logging.getLogger(__name__)


def fibo(start=0, tmp=1):
    while True:
        yield start
        start, tmp = tmp, start + tmp
