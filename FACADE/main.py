from fachada import FachadaViaje

if __name__ == "__main__":
    fachada_viaje = FachadaViaje()
    
    # El cliente solo interactúa con la fachada, le pasa la fecha y el destino
    resultado = fachada_viaje.buscar_viaje("2024-10-10", "Buenos Aires")
    print(resultado)
