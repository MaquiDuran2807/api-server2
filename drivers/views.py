

# Create your views here.
from django.shortcuts import render
from .models import Driver,terminos,AutoDriver
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View
from django.views.generic.edit import FormView
from .forms import DriverForm
from clients.models import Client
from cars.models import Auto
#impotar reverse lazy
from django.urls import reverse_lazy
#importar httpresponse
from django.http import HttpResponse


# Create your views here.

class Conductores(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        clientes=list(Driver.objects.values())
        print(clientes)
        datos={'clients':clientes}
        print(clientes)
        return JsonResponse(datos)

class DriverCreateView(FormView):
    template_name = "add_driver.html"
    form_class=DriverForm
    success_url = '/'

    def post (self, request, *args, **kwargs):
        print("===================================post============================")
        print(request.POST)
        print(request.FILES)
        email=request.POST["verificar_email"]
        licencia=request.POST["licencia"]
        placa=request.POST["placa"]
        marca=request.POST["marca"]
        modelo=request.POST["modelo"]
        color=request.POST["color"]
        referencia=request.POST["referencia"]
        es_propietario=request.POST["es_propietario"]
        if es_propietario=="si":
            es_propietario=True
        else:
            es_propietario=False
        termino=request.POST["terminos"]
        termino=True
        imagen=request.FILES
        imagen_licencia=imagen["imagen_licencia"]
        imagen_vehiculo=imagen["imagen_vehiculo"]
        imagen_cedula=imagen["imagen_cedula"]
        imagen_antecedentes=imagen["imagen_antecedentes"]
        imagen_soat=imagen["imagen_soat"]
        imagen_tarjetapropiedad=imagen["imagen_tarjetapropiedad"]
        cliente=Client.objects.get(email=email)
        cliente.imgcc=imagen_cedula
        cliente.save()
        carro=Auto.objects.create(propietario=cliente,marca=marca,modelo=modelo,color=color,referencia=referencia,es_propio=es_propietario,imgsoat=imagen_soat,imgauto=imagen_vehiculo,imgtarjetapropi=imagen_tarjetapropiedad,numero_placa=placa)
        existDriver=Driver.objects.filter(persona=cliente).exists()
        if existDriver:
            conductor=Driver.objects.get(persona=cliente)
            conductor.licencia=licencia
            conductor.imglicencia=imagen_licencia
            conductor.imgantecedentes=imagen_antecedentes
            conductor.save()
            carros=AutoDriver.objects.get(conductor=conductor)
            carros.autos.add(carro)
            return render(request,"registred_driver.html",{'registro':'actualizado'})
        else:
            conductor=Driver.objects.create(persona=cliente,licencia=licencia,imglicencia=imagen_licencia,imgantecedentes=imagen_antecedentes)
            carros=AutoDriver.objects.create(conductor=conductor)
            carros.autos.add(carro)
            termino1=terminos.objects.create(persona=cliente,terminos=termino)
            return render(request,"registred_driver.html",{'registro':'registrado','conductor':cliente.name,'is_driver':True})
        #return super(DriverCreateView,self).post(request, *args, **kwargs)
    

    def form_valid(self, form):
        print("===================================form is valid============================")
        #form.save()
        return super(DriverCreateView,self).form_valid(form)












# agregar un conductor
"""class addDriver(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        ad=(request.POST)
        correo=ad["correo"]
        token1=ad["token"]
        iden=ad["identification"]
        print(correo)
        imgen=request.FILES
        imgen=imgen["imagen"]
        print(imgen)
        Client.objects.create(token=token1,identification=iden,name=ad["name"],lastname=ad["lastname"],genero=ad["genero"],email=ad["correo"],img=imgen,tel=ad["telefono"])#agregar un cliente
        imglicencia=request.FILES
        imglicencia=imglicencia["imglicencia"]
        imgantecedentes=request.FILES
        imgantecedentes=imgantecedentes["imgantecedentes"]
        carro= Auto.objects.get(numero_placa=ad["placa"])
        if carro:
            Driver.objects.create(persona=Client.objects.get(email=correo),licencia=ad["licencia"],imglicencia=imglicencia,imgantecedentes=imgantecedentes,auto=carro)
            datos={"cliente":"tegistrado"}
            return JsonResponse(datos)
        else:
            datos={"auto":"no existe"}
            return JsonResponse(datos)"""
       
        
     
