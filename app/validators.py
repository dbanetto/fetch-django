import json
import re

from jsonschema import validate, Draft4Validator
from jsonschema.exceptions import ValidationError as SchemaValidationError
from jsonschema.exceptions import SchemaError
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _


def regex_validator(value):
    """
    raises ValidationError if value is not valid regex string
    """
    try:
        re.compile(value)
    except Exception as e:
        raise ValidationError(_('Invalid regex %(err)s'),
                              params={'err': e})


def json_validator(value):
    """
    raises ValidationError if value is not valid json string
    """
    if type(value) is not str:
        raise ValidationError(_('Not a string'))

    try:
        json.loads(value)
    except ValueError:
        raise ValidationError(_('Invalid Json string %(value)s'),
                              params={'value': value})


def json_schema_validator(value):
    """
    raises ValidationError if value is not a valid json schema
    """
    try:
        Draft4Validator.check_schema(value)
    except SchemaError as e:
        raise ValidationError(_('Schema is invalid: %(msg)s'),
                              params={"msg": str(e.message)})


def json_schema_check(json_obj, schema):
    """
    Validates a json object against a schema

    raises ValidationError if json_obj does not conform
    """
    if type(json_obj) is not dict:
        raise ValueError('json_obj is not a dict, but {}'.format(type(json_obj)))

    if type(schema) is dict:
        try:
            validate(json_obj, schema)
        except SchemaValidationError as e: #FIXME: Make better error messages
            raise ValidationError(_('Failed to match schema: %(msg)s'),
                                  params={"msg": str(e.message)})
    else:
        raise ValueError('schema is not a dict but {}'.format(type(schema)))
