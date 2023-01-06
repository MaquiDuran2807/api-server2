
from django.urls import path
from .views import HomeView

# nombre de la app
app_name = 'home'

urlpatterns = [
   path('',HomeView.as_view(),name='home' ),
  
]
