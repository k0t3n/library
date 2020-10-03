from django.contrib import admin

from src.apps.libraries.models import Library, LibraryBook


class LibraryBookInline(admin.TabularInline):
    model = LibraryBook
    extra = 0


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = (LibraryBookInline,)
