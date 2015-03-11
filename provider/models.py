import json

from django.db import models
from json_field import JSONField


class BaseProvider(models.Model):
    """
    The Base logic of a provider
    Requires a client side implementation
    No web interface to create or edit, this is admin only
    """
    name = models.CharField(max_length=160,
                            verbose_name="Base Provider's name")

    available_options = models.TextField(default="id",
                                         help_text="A CSV list of options that"
                                         " the base provider allows")

    def get_available_options(self):
        return self.available_options.split(',')

    def as_dict(self):
        return {'name': self.name,
                'available_options': self.get_available_options()}

    def __str__(self):
        return self.name


class Provider(models.Model):
    """
    The Provider specific information to be able to fetch any series
    from the provider
    Does not needed client side implementation
    """
    base_provider = models.ForeignKey(BaseProvider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the provider")
    website = models.URLField(help_text="url to the provider's website",
                              verbose_name="Provider's website")

    regex_find_count = models.CharField(max_length=256,
                                        default="\d+",
                                        help_text="Regular expression used "
                                        "client side "
                                        "to extract the episode/chapter count "
                                        "from a file name")
    options = JSONField(help_text="JSON Object filled of BaseProvider's"
                                  " available_options with data")

    available_options = models.TextField(default="quality",
                                         help_text="A CSV list of options that"
                                         " the provider allows")

    def __str__(self):
        return "{} ({})".format(self.name, self.base_provider.name)

    def get_available_options(self):
        return self.available_options.split(',')

    def as_dict(self):
        return {'name': self.name,
                'website': self.website,
                'base_provider': self.base_provider.id,
                'regex_find_count': self.regex_find_count,
                'options': json.dumps(self.options),
                'available_options': self.get_available_options()
                }
