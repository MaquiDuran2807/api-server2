from django.db import models
from clients.models import Client
from cars.models import Auto
from django.utils import timezone

# Create your models here.

class Driver(models.Model):
    """Model definition for Driver."""

    # TODO: Define fields here
    persona = models.OneToOneField(Client, on_delete=models.CASCADE)
    licencia = models.IntegerField()
    imglicencia = models.ImageField( upload_to='DRIVE', height_field=None, width_field=None, max_length=None)
    imgantecedentes = models.ImageField( upload_to='DRIVE', height_field=None, width_field=None, max_length=None)
    timestamp = models.DateTimeField(default=timezone.now)
    

    


    class Meta:
        """Meta definition for Driver."""

        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        """Unicode representation of Driver."""
        return str(self.persona)

class terminos(models.Model):
    """Model definition for terminos."""
    persona = models.ForeignKey(Client, on_delete=models.CASCADE)
    terminos = models.BooleanField(default=False)
    timezone = models.DateTimeField(default=timezone.now)

    class Meta:
        """Meta definition for terminos."""

        verbose_name = 'terminos'
        verbose_name_plural = 'terminos'
    def __str__(self):
        """Unicode representation of terminos."""
        return str(self.persona)

class AutoDriver(models.Model):
    """Model definition for AutoDriver."""
    conductor = models.ForeignKey(Driver, on_delete=models.CASCADE)
    autos = models.ManyToManyField(Auto)
    class Meta:
        """Meta definition for AutoDriver."""

        verbose_name = 'AutoDriver'
        verbose_name_plural = 'AutoDrivers'
    def __str__(self):
        """Unicode representation of AutoDriver."""
        return str(self.conductor)

    

