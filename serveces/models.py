from django.db import models
from clients.models import Client
from drivers.models import Driver

# Create your models here.



# Create your models here.
class Services(models.Model):
    """Model definition for Services."""

    # TODO: Define fields here
    client = models.ForeignKey(Client, on_delete=models.CASCADE,db_constraint=False)
    conductor = models.ForeignKey(Client, on_delete=models.CASCADE,db_constraint=False,related_name='conductor')
    latori = models.FloatField()
    lngori = models.FloatField()
    latdes = models.FloatField()
    lngdes = models.FloatField()
    distance=models.FloatField()
    testimado = models.CharField( max_length=10)
    precio=models.IntegerField()
    cancelc = models.IntegerField( null=True,blank=True)# 1 cancelado conductor, 2 cancelado cliente,
    tterminado=models.DateTimeField(verbose_name='terminado', auto_now=False, auto_now_add=False,null=True,blank=True)
    tpedido = models.DateTimeField(verbose_name='pedido', auto_now=False, auto_now_add=False)
    ttake = models.DateTimeField(verbose_name='tomado', auto_now=False, auto_now_add=False)

    




    class Meta:
        """Meta definition for Services."""

        verbose_name = 'Services'
        verbose_name_plural = 'Services'
    


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


class  CarrerasNoTomadas(models.Model):
    """Model definition for NoTTake."""
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE,db_constraint=False)
    hora_no_tomada = models.DateTimeField(verbose_name='hora no tomada', auto_now=False, auto_now_add=False)
    distancia = models.FloatField()
    precio = models.IntegerField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    direccion_origen = models.CharField(max_length=100)
    direccion_destino = models.CharField(max_length=100)
    
    class meta :
        verbose_name = 'carrera no tomada'
        verbose_name_plural = 'carreras no tomadas'
        
    def __str__(self):
        """Unicode representation of NoTTake."""
        return str(self.cliente)+' '+str(self.hora_no_tomada)


