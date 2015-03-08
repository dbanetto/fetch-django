from django.utils import timezone
from django.db import models
from json_field import JSONField

from provider.models import Provider


class MediaType(models.Model):
    """
    Over arching difference between series
    provides more options for different media types
    """
    name = models.CharField(max_length=80,
                            help_text="Name of the media type")
    available_options = models.TextField(default="id",
                                         help_text="A CSV list of options that"
                                         " the media type allows")

    def __str__(self):
        return self.name

    def get_available_options(self):
        return self.available_options.split(',')


class Series(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the series")
    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(default=timezone.now())

    current_count = models.PositiveSmallIntegerField(default=0)
    total_count = models.PositiveSmallIntegerField(default=0)

    poster = models.ImageField(blank=True,
                               upload_to='series/posters')

    provider_options = JSONField(blank=True,
                                 help_text="A JSON object of options"
                                 " made available from the provider")
    media_type_options = JSONField(blank=True,
                                   help_text="A JSON object of options"
                                   " made available from the media type")

    media_type = models.ForeignKey(MediaType,
                                   default=None,
                                   help_text="Series' media type")

    def next_release():
        " Return a Date object of the next release "
        pass

    def series_ended(self):
        " Boolean of if the series has ended airing/publishing "
        pass

    def series_airing(self):
        " Boolean of if the series is currently airing/publishing "
        pass

    def __str__(self):
        return "{} ({})".format(self.name, self.provider.name)
