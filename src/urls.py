from django.contrib import admin
from django.urls import include, path

api_patterns = [
    path('users/', include('src.apps.users.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_patterns)),
]
