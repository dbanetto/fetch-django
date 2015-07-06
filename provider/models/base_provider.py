import json

from django.db import models
from json_field import JSONField

from app.validators import json_schema_validator


class BaseProvider(models.Model):
    """
    The Base logic of a provider
    Requires a client side implementation
    No web interface to create or edit, this is admin only
    """
    name = models.CharField(max_length=160,
                            verbose_name="Base Provider's name")

    available_options = JSONField(default='{"properties": {"id": {"title": "id", "type": "integer", "required": false}}}',
                                  help_text="A JSON Schema of options that"
                                  " the base provider allows",
                                  validators=[json_schema_validator])

    def available_options_json(self):
        return json.dumps(self.available_options)

    def __str__(self):
        return self.name
