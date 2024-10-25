# Simulamos una lista de hoteles disponibles

class Hoteles:
    def buscar_hoteles(self, fecha, destino):
        # Buscamos hoteles disponibles segun el destino y fecha que pasamos
        hoteles = [
            {"nombre": "Hotel Intercontinental", "estrellas": 5},
            {"nombre": "Hotel NH", "estrellas": 4},
            {"nombre": "Hotel Bristol", "estrellas": 3}
        ]
        
        # Devolvemos la lista de los hoteles disponibles y la cantidad de estrellas
        resultado = f"Hoteles disponibles en {destino} el {fecha}:\n"
        for hotel in hoteles:
            resultado += f"- {hotel['nombre']} ({hotel['estrellas']} estrellas)\n"
        
        return resultado
