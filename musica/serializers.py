from rest_framework import serializers
from .models import *

class CancionesSerializer(serializers.ModelSerializer):
    """!
    Clase para serializar el modelo de canciones

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """

    class Meta:
        model = Canciones
        fields = ("nombre",)


class AlbumSerializer(serializers.ModelSerializer):
    """!
    Clase para serializar el modelo de album

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    tracks = CancionesSerializer(many=True)
    
    class Meta:
        model = Album
        fields = ("nombre","tracks")

    def create(self, validated_data):
	    album = Album( nombre=validated_data.get("nombre") )
	    album.save()        
	    tracks = validated_data.get('tracks')
	    for track in tracks:
	      Canciones.objects.create(album=album, **track)
	    return validated_data

class CancionesSolasSerializer(serializers.ModelSerializer):
    """!
    Clase para serializar el modelo de canciones solas

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """

    album_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Canciones
        fields = ("nombre","album","album_id")
        depth = 1