from django.db import models
from clients.models import Client

# Create your models here.


class Auto(models.Model):
    """Model definition for Auto."""


    # TODO: Define fields here
    propietario = models.ForeignKey(Client, on_delete=models.CASCADE)
    marca = models.CharField( max_length=50)
    referencia = models.CharField( max_length=50)
    modelo = models.IntegerField()
    imgsoat = models.ImageField(verbose_name='soat', upload_to='car', height_field=None, width_field=None, max_length=None)
    imgauto = models.ImageField(verbose_name='foto del auto', upload_to='car', height_field=None, width_field=None, max_length=None)
    img_tarjeta_propi = models.ImageField(verbose_name='foto de la tarjeta de propiedad', upload_to=None, height_field=None, width_field=None, max_length=None)
    numero_placa = models.CharField( db_index=True, max_length=50)
    color = models.CharField( max_length=50)
    es_propio = models.BooleanField(default=True)


    class Meta:
        """Meta definition for Auto."""

        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        """Unicode representation of Auto."""
        return str(self.propietario)
        

