from ..models.respuestas import Respuestas
from rest_framework import serializers


class RespuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuestas
        fields = '__all__'
