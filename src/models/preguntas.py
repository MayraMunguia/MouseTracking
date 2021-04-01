from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    CASCADE
)

class Preguntas(Model):

    id_pregunta = CharField(max_length=200)
    descripcion = CharField(max_length=500)
    es_control = BooleanField(default=False)

    # def __str__(self):
    #     return self.nombre

