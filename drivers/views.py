

# Create your views here.
from django.shortcuts import render
from .models import Driver
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views import View

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
