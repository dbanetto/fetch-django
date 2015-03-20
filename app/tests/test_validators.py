from django.test import TestCase
from django.core.validators import ValidationError

from app.validators import regex_validator, json_validator, json_schema_check


class AppValidatorsTest(TestCase):

    def test_regex_validator_valid(self):
        for re in ['a', 'a+', '^a*.+$']:
            with self.subTest(re=re):
                self.assertTrue(regex_validator(re))

    def test_regex_validator_invalid(self):
        for re in ['*', '+$^.']:
            with self.subTest(re=re):
                self.assertFalse(regex_validator(re))

    def test_json_validator_valid(self):
        for json in ['{}', '[]', '{"id":1}']:
            with self.subTest(json=json):
                self.assertTrue(json_validator(json),
                                "{} {}".format(json, type(json)))

    def test_json_validator_invalid(self):
        for json in ['{', '{\'id\': 1}', '[', '', None, 1]:
            with self.subTest(json=json):
                self.assertFalse(json_validator(json))

    def test_json_schema_invalid(self):
        for json, keys in (
                          ("", ['id']),
                          (1, ["id"]),
                          ({"id": "a"}, None)
        ):
            with self.subTest(json=json, keys=keys):
                self.assertFalse(json_schema_check(json, keys))

    def test_json_schema_valid(self):
        for json, keys in (
                          ({"id": "1"}, ['id']),
        ):
            with self.subTest(json=json, keys=keys):
                self.assertTrue(json_schema_check(json, keys))

    def test_json_schema_invalid_key(self):
        for json, keys in (
                          ({"id": "1",
                            "hacking": "the gate"}, ['id']),
        ):
            with self.subTest(json=json, keys=keys):
                with self.assertRaises(ValidationError):
                    json_schema_check(json, keys)
