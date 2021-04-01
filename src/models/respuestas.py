from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    CASCADE
)
from .preguntas import Preguntas

class Respuestas(Model):
    """
    Modelo para los usuarios
    """
    id_respuestas = CharField(max_length=200)
    id_preguntas = ForeignKey(Preguntas,on_delete=CASCADE)
    descripcion = CharField(max_length=100)

    # def __str__(self):
    #     return self.nombre

