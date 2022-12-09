

from django.urls import path
from .views import Clientes,ClientCreateView

urlpatterns = [
    path('',Clientes.as_view()),
    path('addclient',ClientCreateView.as_view()),

]
