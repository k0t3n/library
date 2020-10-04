from django.db import models
from django.utils.translation import gettext as _

from src.apps.authors.models import Author
from src.apps.publishers.models import Publisher
from src.utils.models import TimeStampedModelMixin


class BookAuthorship(models.Model, TimeStampedModelMixin):
    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('book authorship')
        verbose_name_plural = _('books authorship')

    def __str__(self):
        return f'{self.book} - {self.author}'


class Book(models.Model, TimeStampedModelMixin):
    title = models.CharField(
        max_length=255,
    )

    authors = models.ManyToManyField(
        to=Author,
        through=BookAuthorship,
    )

    publisher = models.ForeignKey(
        to=Publisher,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __str__(self):
        return self.title
