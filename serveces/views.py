from django.shortcuts import render
from .models import Services,Price,CarrerasNoTomadas
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from clients.models import Client,Calificacion,Saldo
from django.core.cache import cache
from datetime import datetime, timedelta
import datetime as dt
from django.db.models import Avg
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.views import APIView,status
from rest_framework.response import Response
from .serializers import SerializadorCarreras,SerializadorNear,SerializadorTakeServeces,SerializadorCancel
from . objects import crearCarreras, nearClient, TakeService
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
        listapop=['identification','genero','token','email','imgcc','is_active']# lista de llaves para eliminar del diccionario lo que no necesitamosque pase
        servicios=list(Client.objects.filter(token=jd["cliente_id"]).values())#consulta los datos del cliente 
        print(servicios)
        if servicios==[]:
            print(servicios)
            return JsonResponse ({'message': "Error",'servicios':'no existe el cliente'})
        calificacion=Calificacion.objects.filter(usuario=servicios[0]['id']).aggregate(Avg('calificaciones'))#consulta la calificacion del cliente
        if calificacion['calificaciones__avg']==None:
            servicios[0]['calificacion']=0
        else:    
            servicios[0]['calificacion']=calificacion.get('calificaciones__avg')
        for i in listapop:
            servicios[0].pop(i)
        servicios[0]['coordenadas']=jd['coordenadas']
        servicios[0]['viaje']=jd['viaje']
        #servicios[0]['socketid']=jd['socketid']
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



class ViewServicesActive(ListAPIView):
    """vista para mostrar los servicios activos"""
    serializer_class=SerializadorCarreras 
    
    
    def get_queryset(self):
        queryset =  crearCarreras()
        usuario=self.request.user
        print(f"este es el usuario  {usuario}")
        print(queryset)
        return queryset
    
class ApiNearClient(APIView):
    
    """ Buscar clientes mas cercanos a mi posicion"""
    
    def post(self,request,format=True):
        # tomar la ubicacion del conductor del metodo post
        lat=self.request.data['lat']
        lng=self.request.data['lng']
        carreras= nearClient(lat,lng)
        serializer=SerializadorCarreras(carreras,many=True)
        return Response(serializer.data)

class ApiDriverTakeServices(CreateAPIView):
    """ vista para tomar las carreras de los clientes"""
    serializer_class= SerializadorTakeServeces
    
    
    def create(self,request,*args,**kwargs):
        """metodo para tomar las carreras de los clientes"""
        # tomar el id del conductor y la hora de la peticion de la carrera del metodo post
        
        id_de_driver = self.request.data['id_driver']
        hora_de_peticion = self.request.data['hora_peticion']
        id_cliente=self.request.data['id_cliente']
        horatake=(datetime.now().astimezone())
        saldo=Saldo.objects.filter(usuario_id=id_de_driver).latest('frecarga')
        diredencia_dias=(horatake-saldo.frecarga)
        print(diredencia_dias.days,"este es el numero de dias",timedelta(days=30).days,"este es el numero de dias")
        if -(diredencia_dias.days)>=timedelta(days=30).days:
            print("entro al if")
            saldo=Saldo.objects.create(usuario_id=id_de_driver, saldo=0,frecarga=horatake)
            print(saldo,"este es el saldo")
            return Response({"carrera":"no tiene saldo"})
        print(hora_de_peticion)
        carrera=TakeService(hora_de_peticion,id_cliente)
        print(carrera,"esta es la carrera")
        if carrera==[]:
            return Response({"carrera":"ya ha sido tomada"})
        # guardar en base de datos el servivicio
        dista=carrera.viaje["distancia"]
        dista=str(dista)
        dista=dista.replace('km',"")
        dista=float(dista)
        horatake=(datetime.now().astimezone())
        saldo=Saldo.objects.filter(usuario_id=id_de_driver).latest('frecarga')
        diredencia_dias=(horatake-saldo.frecarga)
        horatake=str(horatake)
        servicio=Services.objects.create(client_id=carrera.id, conductor_id=id_de_driver, latori=carrera.coordenadas["recogida"]['lat'], lngori=carrera.coordenadas["recogida"]['lng'], latdes=carrera.coordenadas["destino"]['lat'], lngdes=carrera.coordenadas["destino"]['lng'], distance=dista, testimado=carrera.viaje["testimado"], precio=carrera.viaje["precio"], tpedido = hora_de_peticion, ttake= horatake)
        serializer=SerializadorCarreras(carrera)
        serializer.data["id_carrera"]=servicio.id
        
        
        print(serializer.data,"este es el saldo ", saldo,"esta es la diferencia de dias",diredencia_dias.days,"este es el tipo de dato",type(diredencia_dias))
        if diredencia_dias.days>=30:
            print("entro al if")
            saldo=Saldo.objects.create(usuario_id=id_de_driver, saldo=0)
            print(saldo,"este es el saldo")
        return Response({"id_carrera":servicio.id,"carrera":serializer.data})
    
class ApiCancel(UpdateAPIView):
    """ vista para cancelar las carreras de los clientes"""
    
    queryset=Services.objects.all()
    serializer_class=SerializadorCancel
    



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
        print(conduc[0]['id'],"este es el id del conductor=======================")
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
            datos={"peticion":"tomada, buen viaje","hora_pedido":horapeticion}
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
        



# vista para ver las carreras almacenadas en cache y organizar las carreras no tomadas en mas de 5 minutos y guardarlas en la base de datos

class CarrerasNView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def get(self,request):
        carreras=cache.get('carreras')
        acum=[]
        for x in carreras:
            if x[0]["hora_peticion"]!=None:
                hora=datetime.strptime(x[0]["hora_peticion"],"%Y-%m-%d %H:%M:%S.%f")
                hora =hora.replace(year=hora.year,month=hora.month,day=hora.day)
                print(type(hora))
                # hora mas 5 minutos
                hora_mas_5=hora+dt.timedelta(minutes=5)
                print("hora mas 5 minutos",hora_mas_5,"type",type(hora_mas_5))
                horaactual=datetime.now()
                # eliminar año dia mes para restar datetimes
                horaactual=horaactual.replace(year=horaactual.year,month=horaactual.month,day=horaactual.day)
                print(hora)
                print(horaactual,"type",type(horaactual))
                diferencia_horas=horaactual-hora
                x[0]["diferencia_horas"]=diferencia_horas
                print("hora actual es mayor a hora mas 5 minutos",horaactual>hora_mas_5)
                if horaactual>hora_mas_5:
                    acum.append(x)
                    carreras.remove(x)
                    print("se elimino")
                else:
                    print("no se elimino")
            else:
                print("no se elimino")
        print("este es acum",acum)
        for x in acum:
            print(x)
            dista=x[0]["viaje"]["distancia"]
            dista=str(dista)
            dista=dista.replace('km',"")
            dista=float(dista)
            precio = x [0]["viaje"]["precio"]
            cliente= Client.objects.get(id=x[0]["id"])
            CarrerasNoTomadas.objects.create(cliente=cliente,hora_no_tomada=x[0]["hora_peticion"],distancia=dista,latitud=x[0]["coordenadas"]["recogida"]["lat"],longitud=x[0]["coordenadas"]["recogida"]["lng"],direccion_origen=x[0]["coordenadas"]["recogida"]["direccion"],direccion_destino=x[0]["coordenadas"]["destino"]["direccion"] , precio=precio)
        cache.set("carreras",carreras,timeout=None)
        return JsonResponse({"carreras":carreras,"acum":acum,"diferencia de horas":diferencia_horas})



# vista para recibir peticion post de la app cuando la carrera no fue tomada y guardarla en la base de datos 

class CarrerasNoTomadasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        


    def post(self,request):
        cno=json.loads(request.body)
        dista=cno["viaje"]["distancia"]
        dista=str(dista)
        dista=dista.replace('km',"")
        dista=float(dista)
        precio = cno ["viaje"]["precio"]
        cliente= Client.objects.get(id=cno["id"])
        CarrerasNoTomadas.objects.create(cliente=cliente,hora_no_tomada=cno["hora_peticion"],distancia=dista,latitud=cno["coordenadas"]["recogida"]["lat"],longitud=cno["coordenadas"]["recogida"]["lng"],direccion_origen=cno["coordenadas"]["recogida"]["direccion"],direccion_destino=cno["coordenadas"]["destino"]["direccion"] , precio=precio)
        return JsonResponse({"carrera no tomada":"carrera no tomada"})
