from django.db import models
from django.utils.translation import gettext as _

from src.utils.models import TimeStampedModelMixin


class Author(models.Model, TimeStampedModelMixin):
    first_name = models.CharField(
        max_length=64,
    )

    middle_name = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=64,
    )

    photo = models.ImageField()

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    def __str__(self):
        return self.initials

    @property
    def initials(self):
        if self.middle_name:
            return f'{self.first_name[0]}. {self.middle_name[0]}. {self.last_name}'
