

from django.urls import path
from .views import Conductores,DriverCreateView

# nombre de la app
app_name = 'drivers'


urlpatterns = [
   path('',Conductores.as_view() ),
   path('adddriver',DriverCreateView.as_view(),name='adddriver'),
]
