from django.test import TestCase
from django.core.validators import ValidationError

from app.validators import regex_validator, json_validator, json_schema_check


class AppValidatorsTest(TestCase):

    def test_regex_validator_valid(self):
        for re in ['a', 'a+', '^a*.+$']:
            self.assertTrue(regex_validator(re))

    def test_regex_validator_invalid(self):
        for re in ['*', '+$^.']:
            self.assertFalse(regex_validator(re))

    def test_json_validator_valid(self):
        for json in ['{}', '[]', '{"id":1}']:
            self.assertTrue(json_validator(json))

    def test_json_validator_invalid(self):
        for json in ['{', '{\'id\': 1}', '[']:
            self.assertFalse(json_validator(json))

    def test_json_schema_valid(self):
        for json, list in (
                           ({"id": "1"}, ['id']),
                          ):
            self.assertTrue(json_schema_check(json, list))

    def test_json_schema_invalid_key(self):
        for json, list in (
                           ({"id": "1",
                             "hacking": "the gate"}, ['id']),
                          ):
            with self.assertRaises(ValidationError):
                json_schema_check(json, list)
