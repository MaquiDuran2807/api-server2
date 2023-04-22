from rest_framework import serializers
from .models import Services


class SerializadorCarreras(serializers.Serializer):
    
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    lastname=serializers.CharField(max_length=100)
    tokenNotifi=serializers.CharField(max_length=100)
    img = serializers.CharField(max_length=100)
    tel = serializers.IntegerField()
    calificacion = serializers.FloatField()
    viaje = serializers.JSONField()
    coordenadas =serializers.JSONField()
    hora_peticion = serializers.DateTimeField()
    distancias = serializers.FloatField(required=False)
    id_carrera = serializers.IntegerField(required=False)
    car=serializers.JSONField(required=False)

class SerializadorCancel(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields = ('cancelc',)
    
class SerializadorNear(serializers.Serializer):
    
    latitud = serializers.FloatField()
    longitud = serializers.FloatField()
    
class SerializadorTakeServeces(serializers.Serializer):
    id_driver=serializers.IntegerField()
    hora_peticion=serializers.CharField()
    
    