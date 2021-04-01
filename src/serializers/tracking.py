from ..models.tracking import Tracking
from rest_framework import serializers


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'
