# Simulamos una lista de vuelos disponibles

class Vuelos:
    def buscar_vuelos(self, fecha, destino):
        # Acá nos conectariamos a las APIs de las aerolineas para filtrar 
        # los vuelos disponibles
        vuelos = [
            {"aerolinea": "Aerolineas Argentinas", "hora": "08:00 AM"},
            {"aerolinea": "LATAM Airlines", "hora": "02:00 PM"},
            {"aerolinea": "Iberia", "hora": "07:30 PM"}
        ]
        
        # Devolvemos una lista de vuelos disponibles
        resultado = f"Vuelos disponibles a {destino} el {fecha}:\n"
        for vuelo in vuelos:
            resultado += f"- {vuelo['aerolinea']} a las {vuelo['hora']}\n"
        
        return resultado

