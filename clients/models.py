from django.db import models

# Create your models here.

class Client(models.Model):
    """Model definition for Client."""

    generos=[('M','masculino'),
             ('F','femenino'),
             ('O','otro')
    ]

    # TODO: Define fields here

    token = models.CharField( max_length=300,db_index=True,blank=True)
    identification = models.IntegerField(verbose_name='cedula')
    name = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    genero = models.CharField( max_length=2,choices=generos,default='femenino')
    email = models.EmailField( max_length=254,db_index=True,unique=True)
    img = models.ImageField( upload_to='Client', height_field=None, width_field=None, max_length=None)
    imgcc = models.ImageField(verbose_name='documento de identidad', upload_to='Client', height_field=None, width_field=None, max_length=None,blank=True)
    tel = models.IntegerField(verbose_name='numero celular')
    


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
        ('familiar','f'),
        ('amigo','a'),
        ('conocido','c')
    ]


    # TODO: Define fields here
    referidos = models.ForeignKey(Client, on_delete=models.CASCADE)
    lazo = models.CharField( max_length=50,choices=lazos,default='amigo')

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




