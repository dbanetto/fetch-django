from django.db import models
from django.utils.translation import ugettext as _

from select_multiple_field.models import SelectMultipleField


class BaseProvider(models.Model):
    """
    The Base logic of a provider
    Requires a client side implementation
    """
    TV_SHOW = 'TV'
    PODCAST = 'PD'
    COMIC = 'CM'
    UNKNOWN = '??'
    MEDIA_TYPE_CHOICES = (
        (TV_SHOW, _('TV Show')),
        (PODCAST, _('Podcast')),
        (COMIC,   _('Comic')),
        (UNKNOWN, _('Unknown')),
    )
    media_types = SelectMultipleField(max_length=len(MEDIA_TYPE_CHOICES)*2,
                                      choices=MEDIA_TYPE_CHOICES,
                                      default=UNKNOWN,
                                      verbose_name="Media types")

    name = models.CharField(max_length=160,
                            verbose_name="Base Provider's name")

    def get_media_types_csv(self):
        """
        Returns the media_types list in CSV format
        """
        return ",".join(self.media_types)

    def __str__(self):
        return "{} ({})".format(self.name, ", ".join(self.media_types))


class Provider(models.Model):
    """
    The Provider specific information to be able to fetch any series
    from the provider
    Does not needed client side implementation
    """
    base_provider = models.ForeignKey(BaseProvider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the provider")
    website = models.CharField(max_length=250,
                               verbose_name="Provider's website")

    # provider specific config

    def __str__(self):
        return "{} ({})".format(self.name, self.base_provider.name)
