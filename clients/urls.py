

from django.urls import path
from .views import (Clientes,ClientCreateView,ClientesInfo,ClientesCalification,
                    ClientesNotification,ClientDriverCreateView,ClientList)

# nombre de la app
app_name = 'clients'

urlpatterns = [
    path('<int:id>',Clientes.as_view()),
    path('addclient',ClientCreateView.as_view(),name='addclient'),
    path('addclientdriver',ClientDriverCreateView.as_view(),name='addclientdriver'),
    path('clientinfo',ClientesInfo.as_view()),
    path('clientcalification',ClientesCalification.as_view()),
    path('clientnotifica',ClientesNotification.as_view()),
    path('clientlist',ClientList.as_view()),
]
