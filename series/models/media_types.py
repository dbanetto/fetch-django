import json

from django.db import models

from app.validators import json_schema_validator
from jsonfield import JSONField

_default='''{
    "properties":
    {
        "id": {
            "title": "ID",
            "type": "integer"
            }
    },
    "required": ["id"]
}'''

class MediaType(models.Model):
    """
    Over arching difference between series
    provides more options for different media types
    """
    name = models.CharField(max_length=80,
                            help_text="Name of the media type")
    available_options = JSONField(help_text="A JSON schema of options that"
                                  " the media type allows",
                                  validators=[json_schema_validator],
                                  default=_default)

    def __str__(self):
        return self.name

    def get_available_options(self):
        return json.dumps(self.available_options)
