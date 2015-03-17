import json
import re

from django.core.validators import ValidationError
from django.utils.translation import ugettext as _


def regex_validator(value):
    try:
        re.compile(value)
        return True
    except:
        return False


def json_validator(value):
    if type(value) is not str:
        return False

    try:
        json.loads(value)
        return True
    except ValueError:
        return False


def json_schema_check(json_obj, keylist):
    """
    Validates a json object or dict against a list of values the
    json_obj should only have

    returns True on success
    raises ValidationError if incorrect
    """
    if type(json_obj) is not dict:
        return False
    if type(keylist) is not list:
        return False

    for k in json_obj:
        if k not in keylist:
            raise ValidationError(
                _('Invalid JSON: invalid key \"%(key)s\"'),
                params={'key': k}
            )
    for l in keylist:
        if l not in json_obj:
            raise ValidationError(
                _('Invalid JSON: Missing key \"%(key)s\"'),
                params={'key': l}
            )
    return True
