


from django.urls import path
from .views import ClientCarreras ,DriverServecesActiv, DriverTakeService,MyService,CancelService,Prices

urlpatterns = [
    path('',ClientCarreras.as_view() ),
    path('drivers',DriverServecesActiv.as_view() ),
    path('take',DriverTakeService.as_view() ),
    path('myservice',MyService.as_view() ),
    path('cancels',CancelService.as_view() ),
    path('price',Prices.as_view() ),
]
