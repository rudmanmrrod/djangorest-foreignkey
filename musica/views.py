from rest_framework import viewsets
from .models import *
from .serializers import *

class AlbumViewSet(viewsets.ModelViewSet):
    """!
    Vista para mostrar los albumnes

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class CancionesViewSet(viewsets.ModelViewSet):
    """!
    Vistas para registrar las canciones

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    model = Canciones
    queryset = Canciones.objects.all()
    serializer_class = CancionesSerializer