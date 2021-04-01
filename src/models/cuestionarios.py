from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    BooleanField,
    CASCADE
)
from .usuario import Usuarios

class Cuestionarios(Model):


    id_cuestionario = CharField(max_length=200)
    id_usuario =  ForeignKey(Usuarios, on_delete= CASCADE)
    fecha_aplicacion = DateTimeField()


    # def __str__(self):
    #     return self.nombre

