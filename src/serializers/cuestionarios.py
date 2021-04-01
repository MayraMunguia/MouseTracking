from ..models.cuestionarios import Cuestionarios
from rest_framework import serializers


class CuestionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuestionarios
        fields = '__all__'
