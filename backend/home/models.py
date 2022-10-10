from django.conf import settings
from django.db import models


class Services(models.Model):
    "Generated Model"
    service = models.CharField(
        max_length=256,
    )
    status = models.CharField(
        max_length=256,
    )
    createdDate = models.DateField()
    terminatedDate = models.DateField()
    description = models.TextField()
