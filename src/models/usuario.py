from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    CASCADE
)

class Usuarios(Model):
    """
    Modelo para los usuarios
    """
    id_usuario = CharField(max_length=200)
    nombre = CharField(max_length=200)
    a_paterno = CharField(max_length=200)
    a_materno = CharField(max_length=200)
    edad =  IntegerField()
    sexo = BooleanField(default=False)
    navegador = CharField(max_length=30)

    # def __str__(self):
    #     return self.nombre

