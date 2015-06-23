from django.test import TestCase
from django.core.validators import ValidationError

from app.validators import regex_validator, json_validator, json_schema_check, json_schema_validator


class AppValidatorsTest(TestCase):

    def test_regex_validator_valid(self):
        for re in ['a', 'a+', '^a*.+$']:
            with self.subTest(re=re):
                regex_validator(re)

    def test_regex_validator_invalid(self):
        for re in ['*', '+$^.']:
            with self.subTest(re=re):
                with self.assertRaises(ValidationError):
                    regex_validator(re)

    def test_json_validator_valid(self):
        for json in ['{}', '[]', '{"id":1}']:
            with self.subTest(json=json):
                json_validator(json)

    def test_json_validator_invalid(self):
        for json in ['{', '{\'id\': 1}', '[', '', None, 1]:
            with self.subTest(json=json):
                with self.assertRaises(ValidationError):
                    json_validator(json)

    def test_json_schema_invalid(self):
        for json, keys in (
            ("", {"properties": {}}),
            ({"id": "a"}, None)
        ):
            with self.subTest(json=json, keys=keys):
                with self.assertRaises(ValueError):
                    json_schema_check(json, keys)

    def test_json_schema_valid(self):
        for json, keys in (
            ({"id": "1"}, {"properties": {"id": {"type": "string"}}}),
        ):
            with self.subTest(json=json, keys=keys):
                json_schema_check(json, keys)

    def test_json_schema_invalid_key_missing(self):
        for json, keys in (
            ({"id": "1"}, {"properties": {"id": {"type": "string"},
                                          "n": {"type": "string"}},
                           "required": ["n"]
                           }),
        ):
            with self.subTest(json=json, keys=keys):
                with self.assertRaises(ValidationError):
                    json_schema_check(json, keys)

    def test_json_schema_validator_valid(self):
        for schema in (
            {"type": "object"},
            {"maxItems": 4}
        ):
            json_schema_validator(schema)

    def test_json_schema_validator_invalid(self):
        for schema in (
            ["list", 1, 5],
        ):
            with self.assertRaises(ValidationError):
                json_schema_validator(schema)


    # FIXME: Find a way to strip properties not in schema
    # or throw error if more than schema is found
    #def test_json_schema_invalid_key(self):
        #for json, keys in (
                          #({"id": "1",
                            #"hacking": "the gate"}, {"properties": {"id": {"type": "string"}}}),
        #):
            #with self.subTest(json=json, keys=keys):
                #with self.assertRaises(ValidationError):
                    #json_schema_check(json, keys)
