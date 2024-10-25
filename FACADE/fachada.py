# Fachada 

from vuelo import Vuelos
from hotel import Hoteles

class FachadaViaje:
    def __init__(self):
        self.disponibilidad_vuelos = Vuelos()
        self.disponibilidad_hoteles = Hoteles()
    
    def buscar_viaje(self, fecha, destino):
        vuelos = self.disponibilidad_vuelos.buscar_vuelos(fecha, destino)
        hoteles = self.disponibilidad_hoteles.buscar_hoteles(fecha, destino)
        return f"{vuelos}\n{hoteles}"

