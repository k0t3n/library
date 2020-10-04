from django.contrib import admin

from src.apps.users.models import User, UserLibraryBook


class UserLibraryBookAdminInline(admin.TabularInline):
    model = UserLibraryBook
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    inlines = (UserLibraryBookAdminInline,)
