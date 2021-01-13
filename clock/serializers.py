from rest_framework import serializers
from .models import ClockApi


class ClockSerializer(serializers.ModelSerializer):
    model = ClockApi

    fields = (
        'id',
        'hours',
        'minuts',
        'angle',
        'date',
    )
