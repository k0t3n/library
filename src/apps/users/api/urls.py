from django.urls import path

from src.apps.users.api.views import CurrentUserView

urlpatterns = [
    path('current/', CurrentUserView.as_view(), name='current'),
]
