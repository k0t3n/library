from django.db import models
from django.utils.translation import gettext as _

from src.utils.models import TimeStampedModelMixin


class Publisher(models.Model, TimeStampedModelMixin):
    title = models.CharField(
        max_length=64,
    )

    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')
