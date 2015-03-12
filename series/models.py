import os

from django.utils import timezone
from django.utils.translation import ugettext as _
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


class ReleaseSchedule(models.Model):
    """
    Type of release schedule
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


def poster_path(instance, filename):
    path = 'series/poster'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}/{}.{}'.format(instance.provider.name,
                                     instance.name,
                                     ext)
    else:
        pass  # TODO: Raise exception
    # return the whole path to the file
    return os.path.join(path, filename)


class Series(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the series")

    start_date = models.DateField(default=timezone.now())
    end_date = models.DateField(default=timezone.now())

    current_count = models.PositiveSmallIntegerField(default=0)
    total_count = models.PositiveSmallIntegerField(default=0)

    poster = models.ImageField(editable=True,
                               upload_to=poster_path)

    media_type = models.ForeignKey(MediaType,
                                   help_text="Series' media type")

    media_type_options = JSONField(help_text="A JSON object of options"
                                   " made available from the media type")

    NONE = 'N'
    WEEKLY = 'W'
    FORTNIGHTLY = 'F'
    MONTHLY = 'M'
    DISCRETE = 'D'
    RELEASE_SCHEDULE_CHOICES = (
        (NONE, _('None')),
        (WEEKLY, _('Weekly')),
        (FORTNIGHTLY, _('Fortnightly')),
        (MONTHLY, _('Monthly')),
        (DISCRETE, _('Discrete')),
    )
    release_schedule = models.CharField(max_length=1,
                                        default=WEEKLY,
                                        choices=RELEASE_SCHEDULE_CHOICES)
    release_schedule_options = JSONField(help_text="A JSON object of needed"
                                         " info for each type of release schedule")

    def next_release(self):
        """
        Return a Date object of the next next_release
        If the series is finished airing will return None
        """
        if self.series_ended:
            return None
        pass

    def series_ended(self):
        " Boolean of if the series has ended airing/publishing "
        return timezone.now().date() > self.end_date

    def series_airing(self):
        " Boolean of if the series is currently airing/publishing "
        return timezone.now().date() < self.end_date and \
               timezone.now().date() > self.start_date

    def __str__(self):
        return "{} ({})".format(self.name, self.provider.name)
