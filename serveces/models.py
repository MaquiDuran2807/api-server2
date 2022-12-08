from django.db import models
from clients.models import Client
from drivers.models import Driver

# Create your models here.



# Create your models here.
class Services(models.Model):
    """Model definition for Services."""

    # TODO: Define fields here
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    conductor = models.ForeignKey(Driver, on_delete=models.CASCADE)
    latori = models.FloatField()
    lngori = models.FloatField()
    latdes = models.FloatField()
    lngdes = models.FloatField()
    distance=models.FloatField()
    testimado = models.CharField( max_length=10)
    precio=models.IntegerField()
    cancelc = models.IntegerField( null=True,blank=True)#0 no cancelado,1 cancelado cliente, 2 cancelado conductor
    tterminado=models.DateTimeField(verbose_name='pedido', auto_now=False, auto_now_add=False,null=True,blank=True)
    tpedido = models.DateTimeField(verbose_name='pedido', auto_now=False, auto_now_add=False)
    ttake = models.DateTimeField(verbose_name='tomado', auto_now=False, auto_now_add=False)
    




    class Meta:
        """Meta definition for Services."""

        verbose_name = 'Services'
        verbose_name_plural = 'Services'
    def __str__(self):
        return str(self.id)


class Price(models.Model):
    """Model definition for Price."""
    ppkm = models.FloatField(verbose_name='precio por kilometro')
    ppm = models.FloatField(verbose_name='precio por minuto')
    pm = models.FloatField(verbose_name='precio minimo')
    fechainit = models.DateField(verbose_name="fecha de implementacion", auto_now=True, auto_now_add=False)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Price."""

        verbose_name = 'Price'
        verbose_name_plural = 'Prices'

    def __str__(self):
        """Unicode representation of Price."""
        return str(self.fechainit)
        


