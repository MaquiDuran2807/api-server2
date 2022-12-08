

# Create your views here.
from django.shortcuts import render
from .models import Client
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View

# Create your views here.

class Clientes(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        clientes=list(Client.objects.values())
        print(clientes)
        datos={'clients':clientes}
        print(clientes)
        return JsonResponse(datos)

    def post(self,request):
        cl=json.loads(request.body)
        correo=cl["correo"]
        token=cl["token"]
        cliente=Client.objects.filter(email=correo)
        cliente.token=token
        cliente=list(cliente.values())
        datos={"cliente":cliente}
        return JsonResponse(datos)





