from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    CASCADE
)
from .cuestionarios import Cuestionarios
from .preguntas import Preguntas
from .respuestas import Respuestas

class Resultados(Model):
    """
    Modelo para los usuarios
    """
    id_resultados = CharField(max_length=200)
    id_cuestionario = ForeignKey(Cuestionarios, on_delete=CASCADE)
    id_pregunta = ForeignKey(Preguntas, on_delete=CASCADE)
    id_respuesta = ForeignKey(Respuestas, on_delete=Respuestas)
    tiempo_respuesta =  DateTimeField()


    # def __str__(self):
    #     return self.nombre

