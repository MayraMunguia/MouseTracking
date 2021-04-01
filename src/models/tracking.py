from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    DateTimeField,
    DecimalField,
    BooleanField,
    TimeField,
    CASCADE
)
from .resultados import Resultados

class Tracking(Model):
    """
    Modelo para los usuarios
    """
    id_tracking = CharField(max_length=200)
    id_resultado = ForeignKey(Resultados, on_delete=CASCADE)
    x_axis = DecimalField(max_digits = 7,decimal_places=6)
    y_axis = DecimalField(max_digits = 7,decimal_places=6)
    no_movimiento = IntegerField()
    hora = TimeField()


    # def __str__(self):    
    #     return self.nombre

