from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView,ListCreateAPIView,ListAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.usuario import UsuariosSerializer
from ..models.usuario import Usuarios
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_400_BAD_REQUEST,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_500_INTERNAL_SERVER_ERROR
    )
from datetime import datetime, date
from django.db import transaction
import json
import logging
logger = logging.getLogger(__name__)



class AccesoUsuariosCreateView(ListCreateAPIView):
    """
    Vista usada para crear nuevos registros de entrada e inicializar proceso de cabina
    """
    serializer_class = UsuariosSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = UsuariosSerializer
        serialized_data = serializer(data=data)
        data_is_valid = serialized_data.is_valid(raise_exception=True)

        try:
            with transaction.atomic():
                # validamos activo, accion a realizar y usuarioS
                usuario = Usuarios.objects.get(id_usuario = data['id_usuario'])


                print(usuario)

                nuevo_ingreso =  Acceso(
                    usuario = usuario,
                    fecha = datetime.now()
                )

                nuevo_ingreso.save()

                # #publish
                # mqtt_client = mqtt.Client()
                # mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
                # mqtt_client.connect(MQTT_ADDRESS, 1883)
                # mqtt_client.publish(MQTT_TOPIC,"ON")
                # print('hi from the mqtt side')


                return_value={
                    "message" : "Se realizó el check-In y sanitización con éxito.",
                    "nombre" : usuario.nombre,
                    "Apellido_Paterno" : usuario.a_paterno,
                    "Apellido_Materno" :  usuario.a_materno
                }

                return Response(return_value, status=HTTP_200_OK)
        except Exception as ex:
            logger.error(ex)
            return_value={"message" : "Ocurrió un error inesperado..", "exception": str(ex) }
            return Response(return_value, status=HTTP_400_BAD_REQUEST)

