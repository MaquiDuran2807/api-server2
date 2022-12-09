

from django.urls import path
from .views import Conductores,DriverCreateView
urlpatterns = [
   path('',Conductores.as_view() ),
   path('adddriver',DriverCreateView.as_view()),
]
