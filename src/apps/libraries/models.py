from django.db import models
from django.utils.translation import gettext as _

from src.apps.books.models import Book
from src.utils.models import TimeStampedModelMixin


class LibraryBook(models.Model, TimeStampedModelMixin):
    library = models.ForeignKey(
        to='Library',
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    class Meta:
        verbose_name = _('library book')
        verbose_name_plural = _('library books')

    def __str__(self):
        return f'{self.library} - {self.book}'


class Library(models.Model, TimeStampedModelMixin):
    title = models.CharField(
        max_length=128,
    )

    books = models.ManyToManyField(
        to=Book,
        through=LibraryBook,
    )

    class Meta:
        verbose_name = _('library')
        verbose_name_plural = _('libraries')

    def __str__(self):
        return self.title
