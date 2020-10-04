from django.db import models


class TimeStampedModelMixin:
    created_dt = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    updated_dt = models.DateTimeField(
        auto_now=True
    )
