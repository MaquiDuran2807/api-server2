from django.core.cache import cache
from geopy.distance import geodesic


class ObjectsCarreras:
    
    def __init__(self) -> None:
        self.id=0
        self.name=""
        self.name=""
        self.lastname=""
        self.tokenNotifi=""
        self.img = ""
        self.tel = 0
        self.calificacion = 0.0
        self.viaje = {}
        self.coordenadas ={}
        self.destino = {}
        self.hora_peticion = ""
        self.distancias = 20.0
    
    
def crearCarreras():
    list_cache=[]
    cacheCarreras = cache.get('carreras')
    print(cacheCarreras)
    if cacheCarreras==None:
        return list_cache
    
    contador=0
    for x in cacheCarreras:
        contador=contador+1
        
        carrera=ObjectsCarreras()
        print(type(x),type(ObjectsCarreras))
        if type(x) == type(carrera):
            list_cache.append(x)
        
        else:
            print(x,"numero: ",contador,"id: ",x[0]['id'])
            carrera.id=x[0]['id']
            carrera.name=x[0]['name']
            carrera.lastname=x[0]['lastname']
            carrera.tokenNotifi=x[0]['tokenNotifi']
            carrera.img=x[0]['img']
            carrera.tel=x[0]['tel']
            carrera.calificacion=x[0]['calificacion']
            carrera.viaje=x[0]['viaje']
            carrera.coordenadas=x[0]['coordenadas']
            carrera.hora_peticion=x[0]['hora_peticion']
            list_cache.append(carrera)
    return list_cache

def nearClient(latitud,longitud):
    cercanas=[]
    dos_cercanas=[]
    listaCarreras=crearCarreras()
    posicion_driver= (latitud,longitud)
    for x in listaCarreras:
        print(x.name)
        posicion_client=(x.coordenadas["recogida"]['lat'],x.coordenadas["recogida"]['lng'])
        distancia=geodesic(posicion_driver,posicion_client).km
        if distancia<=1:
            print("esta cerca, distancia: ",distancia,"km")
            print(x.name)
            x.distancias=distancia
            print(x.distancias)
            cercanas.append(x)
        
    
            
    return cercanas
        
def TakeService(hora_servicio,id_cliente):
    carrera_tomada=[]
    carreras_activas=[]
    carreras = crearCarreras()
    for x in carreras:
        print(x.hora_peticion,x.id,hora_servicio,id_cliente)
        if x.hora_peticion == hora_servicio and x.id == id_cliente:
            
            carrera_tomada=x
            print("carrera tomada: ==============================",carrera_tomada.name)
        else:
            carreras_activas.append(x)
            
    cache.set('carreras',carreras_activas,timeout=None)
    print("======================carreras activas: ",carreras_activas,"carrera tomada:===== ",carrera_tomada)
    return carrera_tomada
        