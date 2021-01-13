import uuid
from django.db import models


class ClockApi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hours = models.IntegerField()
    minuts = models.IntegerField()
    angle = models.FloatField()
    date = models.DateTimeField()
