

from django.urls import path
from .views import Clientes

urlpatterns = [
    path('',Clientes.as_view()),
]
