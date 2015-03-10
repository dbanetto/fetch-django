import json

from django.core.validators import ValidationError
from django.utils.translation import ugettext as _

def json_validator(value):
    try:
        json.loads(value)
        return True
    except ValueError as err:
        return False
