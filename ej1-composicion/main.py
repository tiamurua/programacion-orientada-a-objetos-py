from gestor_hotel import GestorHotel

def testeo():
    gestor_h = GestorHotel()
    
    gestor_h.agregarHotel()
    nombre_h = input("Ingrese nombre del hotel: ")
    
    #1 Agregar habitaciones al hotel
    gestor_h.agregar_habitacion(nombre_h)
    
    #2 Reservar una habitación
    gestor_h.reservar(nombre_h)
    
    #3 Liberar habitacion
    gestor_h.liberar(nombre_h)
    
    #4 Dado un tipo de habitación (sencilla, doble, suite), 
    # mostrar número y piso de las habitaciones de ese tipo.
    gestor_h.inciso_4(nombre_h)
    
    #5 Mostrar la cantidad de habitaciones libres por piso.
    gestor_h.inciso_5(nombre_h)
    
    #6 Para cada tipo de habitación mostrar el detalle asociado 
    # con el siguiente formato:
    gestor_h.inciso_6(nombre_h)
    
if __name__ == '__main__':
    testeo()