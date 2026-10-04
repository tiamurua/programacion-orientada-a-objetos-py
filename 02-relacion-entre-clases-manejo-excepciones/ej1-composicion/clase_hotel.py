from typing import Any
from clase_habitacion import Habitacion

class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __lista_habitaciones: list
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_habitaciones = []
        
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getListaHabitaciones(self):
        return self.__lista_habitaciones
    
    def __str__(self):
        return f"Nombre: {self.getNombre()} - Direccion: {self.getDireccion()} - Telefono: {self.getDireccion()} - Habitaciones: {self.getListaHabitaciones()}"
    
    def agregar_habitacion(self, numero, piso, tipo, precio_por_noche, disponibilidad):
        una_habitacion = Habitacion(numero, piso, tipo, precio_por_noche, disponibilidad)
        self.__lista_habitaciones.append(una_habitacion)
        
    def buscar_habitacion_numero(self, num):
        i = 0
        encontrada = False
        habitacion = None
        while i < len(self.__lista_habitaciones) and not encontrada:
            if self.__lista_habitaciones[i].getNumero() == num:
                encontrada = True
                habitacion = self.__lista_habitaciones[i]
            else:
                i += 1
                
        return habitacion
