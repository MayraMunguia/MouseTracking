from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    SmallIntegerField,
    CASCADE
)
from .cuestionarios import Cuestionarios
from .preguntas import Preguntas

class PreguntaCuestionario(Model):

    id_pregunta_cuestionario = CharField(max_length=200)
    id_cuestionario = ForeignKey(Cuestionarios, on_delete=CASCADE)
    id_pregunta = ForeignKey(Preguntas, on_delete=CASCADE)
    orden = SmallIntegerField()


    # def __str__(self):
    #     return self.nombre

