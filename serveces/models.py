from django.db import models
from clients.models import Client
from drivers.models import Driver

# Create your models here.



# Create your models here.
class Services(models.Model):
    """Model definition for Services."""

    # TODO: Define fields here
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Driver, on_delete=models.CASCADE)
    lat = models.FloatField()
    lng = models.FloatField()
    fechapeticion = models.DateField( auto_now_add=True)
    




    class Meta:
        """Meta definition for Services."""

        verbose_name = 'Services'
        verbose_name_plural = 'Services'

