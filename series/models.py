from django.db import models

from provider.models import Provider


class Series(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=160,
                            verbose_name="Name of the series")

    def __str__(self):
        return "{} {}".format(self.name, self.provider.name)
