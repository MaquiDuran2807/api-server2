from django.db import models
# importar timestamp
from django.utils import timezone
# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=70)
    subtitle = models.CharField(max_length=70)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home')

    def __str__(self):
        return self.title
    
class Explore(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=70)
    texto = models.CharField(max_length=30)
    item1 = models.CharField(max_length=50)
    item2 = models.CharField(max_length=50)
    item3 = models.CharField(max_length=50)
    item4 = models.CharField(max_length=50)
    item5 = models.CharField(max_length=50)
    itemtitle1 = models.CharField(max_length=50)
    itemdescription1 = models.TextField()
    description = models.TextField()
    itentitle2 = models.CharField(max_length=50)
    itemdescription2 = models.TextField()
    itemtitle3 = models.CharField(max_length=50)
    itemdescription3 = models.TextField()
    image1 = models.ImageField(upload_to='explore')
    image2 = models.ImageField(upload_to='explore')


    def __str__(self):
        return self.title
    
class Services(models.Model):
    subtitle = models.TextField()
    itemtitle1 = models.CharField(max_length=50)
    itemdescription1 = models.TextField()
    itemtitle2 = models.CharField(max_length=50)
    itemdescription2 = models.TextField()
    itemtitle3 = models.CharField(max_length=50)
    itemdescription3 = models.TextField()
    itemtitle4 = models.CharField(max_length=50)
    itemdescription4 = models.TextField()
    itemtitle5 = models.CharField(max_length=50)
    itemdescription5 = models.TextField()
    itemtitle6 = models.CharField(max_length=50)
    itemdescription6 = models.TextField()

    def __str__(self):
        return self.subtitle


class FaqModel(models.Model):
    titlef = models.CharField(max_length=100)
    subtitlef = models.CharField(max_length=150)
    itemtitle1f = models.CharField(max_length=150)
    itemdescription1f = models.TextField()
    itemtitle2f = models.CharField(max_length=150)
    itemdescription2f = models.TextField()
    itemtitle3f = models.CharField(max_length=150)
    itemdescription3f = models.TextField()
    itemtitle4f = models.CharField(max_length=150)
    itemdescription4f = models.TextField()
    itemtitle5f = models.CharField(max_length=150)
    itemdescription5f = models.TextField()
    itemtitle6f = models.CharField(max_length=150)
    itemdescription6f = models.TextField()

    def __str__(self):
        return self.titlef

class Contact(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=70)
    tel= models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='contact')
    url = models.URLField()


    def __str__(self):
        return self.title

class copyRight(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=70)
    description = models.TextField()
    url_designed = models.URLField(blank=True, null=True)
    url_image = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.title


class ContactForm (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class SocialMedia (models.Model):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.facebook