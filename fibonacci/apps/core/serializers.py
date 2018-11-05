from django.core.exceptions import SuspiciousOperation

from fibonacci.apps.core.utils import logger


class BaseSerializer:
    FIELDS = ()

    def __init__(self, data: dict) -> None:
        self.data = data

    def validate(self) -> dict:
        validated_data = dict()
        for key, default, _type in self.FIELDS:
            value = self.data.get(key, default)
            if not isinstance(value, _type):
                try:
                    value = _type(value)
                except ValueError as err:
                    logger.error(err)
                    raise SuspiciousOperation(err)
            validated_data[key] = value
        return validated_data


class FiboSerializer(BaseSerializer):
    FIELDS = (
        ('from', 0, int),
        ('to', 144, int),
    )
