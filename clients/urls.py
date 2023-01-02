

from django.urls import path
from .views import Clientes,ClientCreateView,ClientesInfo,ClientesCalification,ClientesNotification

urlpatterns = [
    path('<int:id>',Clientes.as_view()),
    path('addclient',ClientCreateView.as_view()),
    path('clientinfo',ClientesInfo.as_view()),
    path('clientcalification',ClientesCalification.as_view()),
    path('clientnotifica',ClientesNotification.as_view()),
]
