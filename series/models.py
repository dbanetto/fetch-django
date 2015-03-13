import os

from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db import models
from app.storage import OverwriteStorage

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
    if instance:
        filename = '{}.{}'.format(instance.id, ext)
    # return the whole path to the file
    return os.path.join(path, filename)


class Series(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the series")

    start_date = models.DateField(default=timezone.now(),
                                  null=True)
    end_date = models.DateField(default=timezone.now(),
                                null=True)

    current_count = models.PositiveSmallIntegerField(default=0)
    total_count = models.PositiveSmallIntegerField(default=0)

    poster = models.ImageField(editable=True,
                               upload_to=poster_path,
                               storage=OverwriteStorage())

    media_type = models.ForeignKey(MediaType,
                                   help_text="Series' media type")

    media_type_options = JSONField(blank=True,
                                   help_text="A JSON object of options"
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
    release_schedule_options = JSONField(blank=True,
                                         help_text="A JSON object of needed"
                                         " info for each type of release schedule")

    def next_release(self):
        """
        Return a Date object of the next next_release
        If the series is finished airing will return None
        """
        if self.has_ended():
            return None
        pass

    def has_started(self):
        " Boolean of if the series has started airing/publishing "
        return self.start_date is not None and  \
               timezone.now().date() >= self.start_date

    def has_ended(self):
        " Boolean of if the series has ended airing/publishing "
        return self.end_date is not None and  \
               timezone.now().date() > self.end_date

    def is_airing(self):
        " Boolean of if the series is currently airing/publishing "
        return self.has_started() and not self.has_ended()

    def __str__(self):
        return "{} ({})".format(self.name, self.provider.name)

    def bootstrap_progressbar(self):
        """
        Generate HTML for a progress bar using bootstrap 3
        """
        text = ""
        sr = ""
        pb_class = "progress-bar-success"
        value = self.current_count
        max = self.total_count

        if self.total_count == 0:
            pb_class = "progress-bar-warning progress-bar-striped"
            value = self.current_count
            max = self.current_count
            prec = 100
        else:
            prec = round(value/max * 100)

        return """
        <div class="progress">
            <div class="progress-bar {pb_class}" role="progressbar" aria-valuenow="{value}" aria-valuemin="0" aria-valuemax="{max}" style="width: {prec}%">
                <span class="sr-only">{sr}</span>
                {text}
            </div>
        </div>
        """.format(pb_class=pb_class,
                   value=value,
                   max=max,
                   prec=prec,
                   sr=sr,
                   text=text)
