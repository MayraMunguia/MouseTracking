from ..models.pregunta_cuestionario import PreguntaCuestionario
from rest_framework import serializers


class PreguntaCuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreguntaCuestionario
        fields = '__all__'
