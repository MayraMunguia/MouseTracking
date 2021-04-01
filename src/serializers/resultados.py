from ..models.resultados import Resultados
from rest_framework import serializers


class ResultadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultados
        fields = '__all__'
