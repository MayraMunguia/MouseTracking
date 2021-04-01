from ..models.preguntas import Preguntas
from rest_framework import serializers


class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'
