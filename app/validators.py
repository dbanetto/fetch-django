import json
import re

from jsonschema import validate

from django.core.validators import ValidationError
from django.utils.translation import ugettext as _


def regex_validator(value):
    try:
        re.compile(value)
        return True
    except:
        return False


def json_validator(value):
    """
    returns false if value is not valid json
    """
    if type(value) is not str:
        return False

    try:
        json.loads(value)
        return True
    except ValueError:
        return False


def json_schema_check(json_obj, schema):
    """
    Validates a json object or dict against a list of values the
    json_obj should only have

    returns True on success
    raises ValidationError if incorrect
    """
    if type(json_obj) is not dict:
        raise ValueError('json_obj is not a dict')

    if type(schema) is list: # FIXME: Once transition to full JSON schema complete, remove me
        for k in json_obj:
            if k not in schema:
                raise ValidationError(
                    _('Invalid JSON: invalid key \"%(key)s\"'),
                    params={'key': k}
                )
        for l in schema:
            if l not in json_obj:
                raise ValidationError(
                    _('Invalid JSON: Missing key \"%(key)s\"'),
                    params={'key': l}
                )
    elif type(schema) is dict:
        validate(json_obj, schema)
    else:
        raise ValueError('schema is not a list or a dict but {}'.format(type(schema)))
    return True
