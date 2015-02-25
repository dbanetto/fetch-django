from django.db import models


class BaseProvider(models.Model):
    """
    The Base logic of a provider
    Requires a client side implementation
    No web interface to create or edit, this is admin only
    """
    name = models.CharField(max_length=160,
                            verbose_name="Base Provider's name")

    avaiable_options = models.TextField(default="quality",
                                        help_text="A CSV list of options that "
                                        "the base provider allows")

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

    def __str__(self):
        return "{} ({})".format(self.name, self.base_provider.name)
