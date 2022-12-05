


from django.urls import path
from .views import Carreras

urlpatterns = [
    path('',Carreras.as_view() ),
]
