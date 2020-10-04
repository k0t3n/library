from django.contrib import admin

from src.apps.authors.models import Author
from src.apps.books.admin import BookAuthorshipAdminInline


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name')
    inlines = (BookAuthorshipAdminInline,)
