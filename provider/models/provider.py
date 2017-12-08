import json

from django.db import models
from jsonfield import JSONField

from provider.models import BaseProvider


class Provider(models.Model):
    """
    The Provider specific information to be able to fetch any series
    from the provider
    Does not needed client side implementation
    """

    base_provider = models.ForeignKey(BaseProvider, on_delete=models.CASCADE)
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
                                  " available_options with data",
                        blank=True, default={})

    def __str__(self):
        return "{} ({})".format(self.name, self.base_provider.name)

    def base_provider_options_json(self):
        """
        Get options as a JSON string
        """
        return json.dumps(self.options)
