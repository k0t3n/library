from django.contrib import admin

from src.apps.books.models import Book, BookAuthorship


class BookAuthorshipAdminInline(admin.TabularInline):
    model = BookAuthorship
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher')
    filter_horizontal = ('authors',)
    inlines = (BookAuthorshipAdminInline,)
