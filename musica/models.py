from django.db import models

class Album(models.Model):
    """!
    Clase que contiene el album

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    nombre = models.CharField(max_length=128, unique=True)
    
class Canciones(models.Model):
    """!
    Clase que contiene las canciones del album

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    nombre = models.CharField(max_length=128, unique=True)

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')