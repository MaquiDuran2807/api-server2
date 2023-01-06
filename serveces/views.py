from django.shortcuts import render
from .models import Services,Price
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from clients.models import Client,Calificacion
from django.core.cache import cache
from datetime import datetime 
from django.db.models import Avg,Max
from geopy.distance import geodesic




# Create your views here.

class ClientCarreras(View):
    """vista para recibir las peticiones post de las carreras de los Clientes"""

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
        jd=json.loads(request.body)#decoifica el mensaje que envian como json via http
        print(jd)
        serviciosgeneral=[]#se acumulan los datos en una lista de diccionarios con la informacion de las carreras para luego guardarlas en cache
        listapop=['identification','genero','token','email','imgcc']# lista de llaves para eliminar del diccionario lo que no necesitamosque pase
        servicios=list(Client.objects.filter(token=jd['cliente_id']).values())#consulta los datos del cliente 
        calificacion=Calificacion.objects.filter(usuario=servicios[0]['id']).aggregate(Avg('calificaciones'))#consulta la calificacion del cliente
        if calificacion['calificaciones__avg']==None:
            servicios[0]['calificacion']=0
        else:    
            servicios[0]['calificacion']=calificacion.get('calificaciones__avg')
        for i in listapop:
            servicios[0].pop(i)
        servicios[0]['coordenadas']=jd['coordenadas']
        servicios[0]['viaje']=jd['viaje']
        servicios[0]['socketid']=jd['socketid']
        ahora=datetime.now()
        ahora=str(ahora)
        servicios[0]['hora_peticion']=ahora
        carrerascache=cache.get('carreras')
        datos = {'message': "Success",'servicios':'peticion en proceso','consultar': ahora+str(servicios[0]['id']),"horaPeticion":ahora}
        if carrerascache==None:
            serviciosgeneral.append( servicios)
            cache.set('carreras',serviciosgeneral)
            return JsonResponse(datos)
        else:
            for x in carrerascache:
                serviciosgeneral.append(x)

            serviciosgeneral.append( servicios)
            cache.set('carreras',serviciosgeneral,timeout=None)
            datos = {'message': "Success",'servicios':'peticion en proceso','consultar': ahora+str(servicios[0]['id']),"horaPeticion":ahora}
            return JsonResponse(datos)
        
        
        
    def get(self,request):
        'metodo para mostrar las carreras '
        tomadas=[]
        
        #cache.delete('carreras')
        carrerascache=cache.get('carreras')
        print('esto es lo que viene de cache',carrerascache)
        conductoresca=cache.keys('carrerastake*')
        print(conductoresca)
        for w in conductoresca:
            cachetomadas=cache.get(w)
            tomadas.append(cachetomadas)

        datos={'clients':carrerascache,'cache_carrerastomadas':tomadas}  
        return JsonResponse(datos)

class DriverServecesActiv(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request):
        inrange=[]
        ds=json.loads(request.body)
        cache_carreras=cache.get('carreras')
        for x in cache_carreras:
            disdriver=(ds["ubicacion"]["lat"],ds["ubicacion"]["lng"])
            disclient=(x[0]["coordenadas"]["recogida"]["lat"],x[0]["coordenadas"]["recogida"]["lng"])
            distance=geodesic(disdriver,disclient).km
            if distance<=1:
                x[0]["distancia_cliente"]=distance*1000
                inrange.append(x)

        datos={"estado":inrange}
        
        return JsonResponse(datos)

class DriverTakeService(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def post(self, request):
        acumcarreras=[]
        take=False
        dt=json.loads(request.body) 
        conduc=list(Client.objects.filter(token=dt["token"]).values())#consulta que usuario exista falta validar
        cliente=Client.objects.get(pk=dt['id'])
        calificacion=Calificacion.objects.filter(usuario=conduc[0]['id']).aggregate(Avg('calificaciones'))#consulta la calificacion del cliente
        
        if calificacion['calificaciones__avg']==None:
            conduc[0]['calificacion']=0.0
        else:    
            conduc[0]['calificacion']=calificacion.get('calificaciones__avg')
        
        
        cache_carreras=cache.get('carreras')
        print(cache_carreras)
        for x in cache_carreras:
            print(f'el valor de {str(x[0]["hora_peticion"])} el valor de {dt["hora_peticion"]} ')
            if x[0]["id"]==dt['id'] and str(x[0]["hora_peticion"])==dt["hora_peticion"]:
                dista=x[0]["viaje"]["distancia"]
                dista=str(dista)
                dista=dista.replace('km',"")
                dista=float(dista)

                print(dista)
                print('este es x: ',x)
                horapeticion= str(x[0]["hora_peticion"])
                horatake=str(datetime.now())
                print('estas son las horas pasadas por strstripe',horapeticion,horatake)
                print("este es el id del conductor: ",conduc[0]['id'],type(conduc[0]['id']) ," y este el del cliente",dt['id'],type(dt['id']),cliente.pk)

                Services.objects.create(client_id=cliente.pk, conductor_id=conduc[0]['id'], latori=x[0]["coordenadas"]["recogida"]['lat'], lngori=x[0]["coordenadas"]["recogida"]['lng'], latdes=x[0]["coordenadas"]["destino"]['lat'], lngdes=x[0]["coordenadas"]["destino"]['lng'], distance=dista, testimado=x[0]["viaje"]["testimado"], precio=x[0]["viaje"]["precio"], tpedido = horapeticion, ttake= horatake)
                take=True
                
                 
            else:
                acumcarreras.append(x)
        
        if take==True:
            cache.set("carreras",acumcarreras,timeout=None)
            idriv= 'carrerastake'+str(x[0]["hora_peticion"])+str(dt['id'])
            cache.set(idriv,conduc)
            datos={"peticion":"tomada, buen viaje","llave":idriv,"hora_pedido":horapeticion}
        else:
            datos={"peticion":"el viaje ya ha sido tomado"}

        return JsonResponse(datos)
    

class MyService(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def post(self, request):
        ms = json.loads(request.body)
        valid=False
        
        idriv= 'carrerastake'+str(ms["hora_peticion"])+str(ms['id'])
        kcachedrive=cache.get(idriv)
        print('este es idriv ',idriv)
        print('kcachedriv',kcachedrive)

        
        if kcachedrive:
            valid=True
        if valid==True:
            datos={"mywego":kcachedrive,"llave":idriv,"tiempopedido":ms["hora_peticion"]}
            return JsonResponse(datos)
        else:

            datos={"mywego":"esperando"}
            return JsonResponse(datos)


class CancelService(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def post(self, request):
        cs = json.loads(request.body)
        rol=0
        llave=cs["llave"]
        carrera=cache.get(llave)
        if carrera==None:
            print("llego vacio la carrera")
            return JsonResponse({"no hay datos":"no data"})

        else:
            cache.delete(cs["llave"])
            cancels=Services.objects.filter(tpedido=cs["hora_pedido"]).update(cancelc=cs["rol"])
            datos={"carrera":"carrera ancelada","dcancelada":cancels}

            return JsonResponse(datos)

class Prices(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def get(self,request):
        
        precio=str(Price.objects.all().last())
        precioh=list(Price.objects.filter(fechainit=precio).values())
        
        datos={"precios":precioh}
        return JsonResponse(datos)

class ResetallView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def get(self,request):
        cache.delete('carreras')
        carrera23=cache.get('carreras')
        return JsonResponse({"datos borrados":carrera23})
        







 
