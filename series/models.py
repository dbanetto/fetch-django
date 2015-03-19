import os
import json
from datetime import timedelta, time, datetime
from dateutil.relativedelta import relativedelta

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
    title = models.CharField(max_length=160,
                             verbose_name="Name of the series")

    search_title = models.CharField(max_length=256,
                                    verbose_name="String to be used when searching for the series")

    start_date = models.DateField(default=None,
                                  null=True)
    end_date = models.DateField(default=None,
                                null=True)

    release_time = models.TimeField(default=time(hour=12))

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
        Return a DateTime object of the next next_release
        If the series is finished airing will return None
        """
        if self.has_ended():
            return None

        if not self.has_started():
            return datetime.combine(self.start_date, self.release_time)

        if self.start_date is None:
            return None

        # is airing

        release_date = self.start_date
        delta = None
        if self.release_schedule == Series.WEEKLY:
            delta = relativedelta(days=7)
        elif self.release_schedule == Series.FORTNIGHTLY:
            delta = relativedelta(days=14)
        elif self.release_schedule == Series.MONTHLY:
            delta = relativedelta(months=1)
        else:
            return None

        while release_date < timezone.now().date():
            release_date += delta

        assert(type(self.release_time) is time)
        release_datetime = datetime.combine(release_date, self.release_time)
        return release_datetime


    def has_started(self):
        """
        Boolean of if the series has started airing/publishing
        """
        return self.start_date is not None and  \
               timezone.now().date() >= self.start_date

    def has_ended(self):
        """
        Boolean of if the series has ended airing/publishing
        """
        return self.end_date is not None and  \
               timezone.now().date() > self.end_date

    def is_airing(self):
        """
        Boolean of if the series is currently airing/publishing
        """
        return self.has_started() and not self.has_ended()

    def __str__(self):
        return "{} ({})".format(self.title, self.provider.name)

    def bootstrap_label_class(self):
        """
        Generate HTML class for label using bootstrap 3
        """
        if self.is_airing():
            return 'label-success'
        if self.has_ended():
            return 'label-danger'
        if not self.has_started():
            return 'label-info'

    def label_text(self):
        """
        Generate HTML class for label using bootstrap 3
        """
        if self.is_airing():
            return _('Airing')
        if self.has_ended():
            return _('Finished')
        if not self.has_started():
            return _('Yet to air')

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

    def release_schedule_options_json(self):
        return json.dumps(self.release_schedule_options)

    def media_type_options_json(self):
        return json.dumps(self.media_type_options)
