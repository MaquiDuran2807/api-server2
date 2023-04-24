


from django.urls import path
from .views import (ClientCarreras ,DriverServecesActiv, DriverTakeService,MyService,
                    CancelService,Prices,ResetallView,CarrerasNView,ViewServicesActive,
                    ApiNearClient,ApiDriverTakeServices,ApiCancel,ApiCancelClient)

urlpatterns = [
    path('',ClientCarreras.as_view() ),
    path('drivers',DriverServecesActiv.as_view() ),
    path('take',DriverTakeService.as_view() ),
    path('myservice',MyService.as_view() ),
    path('cancels',CancelService.as_view() ),
    path('price',Prices.as_view() ),
    path('reset',ResetallView.as_view() ),
    path('carrerasn',CarrerasNView.as_view() ),
    path('viewservices',ViewServicesActive.as_view() ),
    path('near',ApiNearClient.as_view()),
    path('takeapi',ApiDriverTakeServices.as_view()),
    path('cancelapi/<pk>',ApiCancel.as_view()),
    path('cancelclient',ApiCancelClient.as_view()),
    
]
