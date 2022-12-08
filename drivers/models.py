from django.db import models
from clients.models import Client

# Create your models here.

class Driver(models.Model):
    """Model definition for Driver."""

    # TODO: Define fields here
    persona = models.ForeignKey(Client, on_delete=models.CASCADE)
    licencia = models.IntegerField()
    imglicencia = models.ImageField( upload_to='DRIVE', height_field=None, width_field=None, max_length=None)
    imgantecedentes = models.ImageField( upload_to='DRIVE', height_field=None, width_field=None, max_length=None)
    


    class Meta:
        """Meta definition for Driver."""

        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        """Unicode representation of Driver."""
        return str(self.persona)
    

