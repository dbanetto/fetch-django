import re
import json
from datetime import time, datetime
from dateutil.relativedelta import relativedelta

from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db import models
from django.core.exceptions import ValidationError

from app.storage import OverwriteStorage
from jsonfield import JSONField
from provider.models import Provider
from series.models import MediaType
from series.util import poster_path


class Series(models.Model):
    """
    Series
    """

    provider = models.ForeignKey(Provider)
    title = models.CharField(max_length=160,
                             verbose_name="Name of the series")

    search_title = models.CharField(max_length=256,
                                    blank=True,
                                    default='',
                                    verbose_name="String to be used when searching for the series")

    save_path = models.CharField(max_length=256,
                                 default='',
                                 blank=True,
                                 verbose_name="Path to be sorted into")

    info_url = models.URLField(blank=True,
                               verbose_name="Information URL")

    start_date = models.DateField(default=None,
                                  null=True)
    end_date = models.DateField(default=None,
                                null=True)

    release_time = models.TimeField(default=time(hour=12))

    current_count = models.PositiveSmallIntegerField(default=0)
    total_count = models.PositiveSmallIntegerField(default=0)

    poster = models.ImageField(editable=True,
                               upload_to=poster_path,
                               storage=OverwriteStorage(),
                               null=True)

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

    def clean(self):
        """
        Clean and validate model

        Throws ValidationError when:
            - current count is below 0
            - total count is defined & below zero
            - total count is defined & current is larger than total
        """
        if self.current_count < 0:
            raise ValidationError('Currnet count cannot be below zero')

        if self.total_count is not None:
            if self.total_count < 0:
                raise ValidationError('Currnet count cannot be below zero')
            if self.current_count > self.total_count != 0:
                raise ValidationError('Current count cannot be bigger than total count, unless total count is zero')

        if self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValidationError('Start date cannot be greater than end date')

    def next_release(self):
        """
        Calculate the datetime of the next release of the series

        Returns:
            Return a DateTime object of the next next_release
            If the series is finished airing will return None
        """
        if self.start_date is None:
            return None

        if self.has_ended():
            return None

        if not self.has_started():
            return datetime.combine(self.start_date, self.release_time)

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
            if self.end_date is not None:
                return datetime.combine(self.end_date, self.release_time)
            else:
                return None

        while datetime.combine(release_date, self.release_time) < datetime.now():
            release_date += delta

        release_datetime = datetime.combine(release_date, self.release_time)
        return release_datetime

    def has_started(self):
        """
        Series has started airing/publishing

        Note:
            uses release_time for time of day
        """
        return self.start_date is not None and \
                timezone.now() >= timezone.make_aware(
                    datetime.combine(self.start_date, self.release_time))

    def has_ended(self):
        """
        Series has ended airing/publishing

        Note:
            uses release_time for time of day
        """
        if self.total_count != 0 and self.current_count >= self.total_count:
            return True

        if self.end_date is not None:
            return timezone.now() > timezone.make_aware(
                   datetime.combine(self.end_date, self.release_time))

        return False

    def is_airing(self):
        """
        Boolean of if the series is currently airing/publishing

        note:
            relies on has_started() and has_ended()
        """
        return self.has_started() and not self.has_ended()

    def __str__(self):
        return "{} ({})".format(self.title, self.provider.name)

    def bootstrap_label_class(self):
        """
        Generate HTML class for label for bootstrap 3
        """
        if self.is_airing():
            return 'label-success'
        if self.has_ended():
            return 'label-danger'
        if not self.has_started():
            return 'label-info'

    def label_text(self):
        """
        Generate HTML class for label for bootstrap 3
        """
        if self.is_airing():
            return _('Airing')
        if self.has_ended():
            return _('Finished')
        if not self.has_started():
            return _('Soon')

    def bootstrap_progressbar(self):
        """
        Generate HTML for a progress bar for bootstrap 3
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
        """
        dumps release_schedule as json
        """
        return json.dumps(self.release_schedule_options)

    def media_type_options_json(self):
        """
        dumps media_type_options as json
        """
        return json.dumps(self.media_type_options)

    def info_url_domain(self):
        """
        Get the domain name of the info_url
        """
        if type(self.info_url) is str:
            return re.sub('^.*://', '', self.info_url).split('/')[0]
