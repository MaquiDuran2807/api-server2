from django.shortcuts import render
from .models import Services
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from clients.models import Client,Calificacion
from django.core.cache import cache
from datetime import datetime
from django.db.models import Avg




# Create your views here.

class Carreras(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
        jd=json.loads(request.body)
        print(request.headers)
        
        serviciosgeneral=[]
        listapop=['id','identification','genero','token']
        jd=json.loads(request.body)
        print(jd)
        servicios=list(Client.objects.filter(token=jd['cliente_id']).values())
        calificacion=Calificacion.objects.filter(usuario=servicios[0]['id']).aggregate(Avg('calificaciones'))
        if calificacion['calificaciones__avg']==None:
            servicios[0]['calificacion']='sin calificacion'
        else:    
            servicios[0]['calificacion']=calificacion.get('calificaciones__avg')
        for i in listapop:
            servicios[0].pop(i)

        servicios[0]['coordenadas']=jd['coordenadas']

        ahora=datetime.now()
        servicios[0]['hora_peticion']=ahora
        carrerascache=cache.get('carreras')
        print('este es el get ',carrerascache)
        datos = {'message': "Success",'servicios':'peticion en proceso'}
        if carrerascache==None:
            print('era none')
            serviciosgeneral.append( servicios)
            cache.set('carreras',serviciosgeneral)
            return JsonResponse(datos)
        else:
            print('no era none')
    

            for x in carrerascache:
                serviciosgeneral.append(x)
                cache.set('carreras',serviciosgeneral,timeout=None)

            serviciosgeneral.append( servicios)
            print(serviciosgeneral)
            #Services.objects.create(cliente_id=jd['cliente_id'],conductor_id=jd['conductor_id'],lat=jd['lat'],lng=jd['lng'])
            cache.set('carreras',serviciosgeneral,timeout=None)
            
            print('esta es la concatenacion ')
            datos = {'message': "Success",'servicios':'peticion en proceso'}
            return JsonResponse(datos)
        
        


        
    def get(self,request):
        
        #cache.delete('carreras')
        carrerascache=cache.get('carreras')

        print('esto es lo que viene de cache',carrerascache)

        datos={'clients':carrerascache}
        
            
        return JsonResponse(datos)
