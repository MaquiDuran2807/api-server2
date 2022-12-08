

from django.urls import path
from .views import Conductores
urlpatterns = [
   path('',Conductores.as_view() ),
]
