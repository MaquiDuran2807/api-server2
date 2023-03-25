from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    """Model definition for Client."""

    generos=[('M','masculino'),
             ('F','femenino'),
             ('O','otro')
    ]

    token = models.CharField( max_length=300,db_index=True,blank=True)
    tokenNotifi=models.CharField( max_length=400,db_index=True,blank=True)
    identification = models.IntegerField(verbose_name='cedula')
    name = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    genero = models.CharField( max_length=2,choices=generos,default='femenino',blank=True,null=True)
    email = models.EmailField( max_length=254,db_index=True,unique=True)
    img = models.ImageField( upload_to='Client', height_field=None, width_field=None, max_length=None,blank=True)
    imgcc = models.ImageField(verbose_name='documento de identidad', upload_to='Client', height_field=None, width_field=None, max_length=None,blank=True)
    tel = models.IntegerField(verbose_name='numero celular')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    
    is_active = models.BooleanField(default=False)


    class Meta:
        """Meta definition for Client."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return str(self.id)+' '+self.name

class Referido(models.Model):
    """Model definition for Referidos."""
    lazos=[
        ('f','familia'),
        ('a','amigo'),
        ('c','conocido')
    ]
    # TODO: Define fields here
    # modelo de referidos
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    referidos  = models.ManyToManyField(Client,related_name='referidos',blank=True)
    

   
    lazo = models.CharField( max_length=10,choices=lazos,default='amigo')

    class Meta:
        """Meta definition for Referido."""

        verbose_name = 'Referido'
        verbose_name_plural = 'Referidos'

    def __str__(self):
        """Unicode representation of Referidos."""
        return self.referidos+' '+self.lazo

class Calificacion(models.Model):
    """Model definition for calificacion."""


    usuario = models.ForeignKey(Client, on_delete=models.CASCADE)
    calificaciones = models.IntegerField()
    comentario = models.CharField( max_length=150,null=True,blank=True)
   

    # TODO: Define fields here

    class Meta:
        """Meta definition for calificacion."""

        verbose_name = 'calificacion'
        verbose_name_plural = 'calificaciones'

    def __str__(self):
        """Unicode representation of calificacion."""
        return str(self.usuario)+' calificacion: '+str(self.calificaciones)

class Saldo(models.Model):
    """Model definition for saldo."""

    # TODO: Define fields here
    usuario = models.ForeignKey(Client, on_delete=models.CASCADE)
    saldo = models.IntegerField()
    frecarga = models.DateTimeField(verbose_name="fecha recarga", auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for saldo."""

        verbose_name = 'saldo_cliente'
        verbose_name_plural = 'saldos'

    def __str__(self):
        """Unicode representation of saldo."""
        return str(self.frecarga)





