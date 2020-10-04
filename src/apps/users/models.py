from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from src.apps.libraries.models import LibraryBook
from src.utils.models import TimeStampedModelMixin


class User(AbstractUser):
    ...


class UserLibraryBook(models.Model, TimeStampedModelMixin):
    LENDING_STATUS = 'lending'
    RETURNED_STATUS = 'returned'

    # TODO: lost book case
    STATUS_CHOICES = (
        (LENDING_STATUS, _('lending')),
        (RETURNED_STATUS, _('returned')),
    )

    library_book = models.ForeignKey(
        to=LibraryBook,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
    )

    lended_dt = models.DateTimeField(
        null=True,
        blank=True,
    )

    deadline_dt = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('user library book')
        verbose_name_plural = _('user library books')
