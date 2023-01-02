

# Create your views here.
from django.shortcuts import render
from .models import Client,Saldo,Calificacion
from drivers.models import Driver 
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum,Avg,Count
from django.views import View
from django.views.generic import CreateView
from .forms import ClientForm
from serveces.models import Services
from datetime import datetime 


# Create your views here.

class Clientes(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id):
        listpop=["id","token","identification","genero","email","imgcc","tel"]
        clientes=list(Client.objects.filter(pk=id).values())
        for i in listpop:
            clientes[0].pop(i)
        calificacion=Calificacion.objects.filter(usuario=id).aggregate(Avg('calificaciones'))#consulta la calificacion del cliente
        calificacion2=Calificacion.objects.filter(usuario=id).aggregate(Count('calificaciones'))
        if calificacion['calificaciones__avg']==None:
            clientes[0]['calificacion']=0
            clientes[0]['viajes']=0

        else:    
            clientes[0]['calificacion']=calificacion.get('calificaciones__avg')
            clientes[0]['viajes']=calificacion2.get('calificaciones__count')
            saldo1=Saldo.objects.filter(usuario=id).aggregate(Sum("saldo"))
        clientes[0]["saldo"]=saldo1.get('saldo__sum')
        isDriver=Driver.objects.filter(persona=id).exists()
        print(clientes)
        datos={'clients':clientes,"conductor":isDriver}
        print(clientes)
        return JsonResponse(datos)

    def post(self,request,id):
        cl=(request.POST)
        correo=cl["correo"]
        token1=cl["token"]
        iden=cl["identification"]
        print(correo)
        imgen=request.FILES
        imgen=imgen["imagen"]
        print(imgen)
        Client.objects.create(token=token1,identification=iden,name=cl["name"],lastname=cl["lastname"],genero=cl["genero"],email=cl["correo"],img=imgen,tel=cl["telefono"])
        datos={"cliente":"tegistrado"}
        print('cliente no existe')
        
        return JsonResponse(datos)

        

class ClientCreateView(CreateView):
    model = Client
    template_name = "add_clients.html"
    form_class=ClientForm


class ClientesInfo(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        ci=json.loads(request.body)
        listpop=["token","identification","genero","email","imgcc","tel"]
        clientes=list(Client.objects.filter(email=ci["correo"]).values())
        idcli=clientes[0]["id"]
        for i in listpop:
            clientes[0].pop(i)
        calificacion=Calificacion.objects.filter(usuario=idcli).aggregate(Avg('calificaciones'))#consulta la calificacion del cliente
        calificacion2=Calificacion.objects.filter(usuario=idcli).aggregate(Count('calificaciones'))
        saldo1=Saldo.objects.filter(usuario=idcli).aggregate(Sum("saldo"))
        if calificacion['calificaciones__avg']==None:
            clientes[0]['calificacion']=0.0
            clientes[0]['viajes']=0

        else:    
            clientes[0]['calificacion']=calificacion.get('calificaciones__avg')
            clientes[0]['viajes']=calificacion2.get('calificaciones__count')
        
        if saldo1['saldo__sum']==None:
            clientes[0]["saldo"]=0
        else:
            clientes[0]["saldo"]=saldo1.get('saldo__sum')
        isDriver=Driver.objects.filter(persona=idcli).exists()
        print(clientes)
        datos={'clients':clientes,"conductor":isDriver}
        print(clientes)
        return JsonResponse(datos)

    

class ClientesCalification(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        cc=json.loads(request.body)
        ahora=datetime.now()
        if cc["rol"]=="condutor":
            Calificacion.objects.create(usuario=Client.objects.get(pk=cc["id"]),calificaciones=cc["calificacion"],comentario=cc["comentario"])
            servicio=Services.objects.filter(tpedido=cc["hora"]).update(tterminado=ahora)
            print(servicio)
            Saldo.objects.create(usuario=Client.objects.get(pk=cc["mi_id"]),saldo=cc["precio"],frecarga=ahora)
        else:
            Calificacion.objects.create(usuario=Client.objects.get(pk=cc["id"]),calificaciones=cc["calificacion"],comentario=cc["comentario"])
            if cc["pago"]=="efectivo":
                return JsonResponse({"succes":"succes"})
            else:
                Saldo.objects.create(usuario=Client.objects.get(pk=cc["mi_id"]),saldo=-cc["precio"],frecarga=ahora)    
        return JsonResponse({"calificacion":"calificado"})

class ClientesNotification(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        cn=json.loads(request.body)
        tok=Client.objects.get(pk=cn["id"])
        tok.tokenNotifi=cn["tokenN"]
        tok.save()
        return JsonResponse({'token':'se agrego el token'})



"""class AddClientes(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        ac=json.loads(request.body)
        Client.objects.create(token= ,identification= ,name= ,lastname= ,genero= ,email= ,)
"""





