# 1. Crear las clases Paciente y Atenciones. Los datos de los archivos representan el estado
#  de los objetos pertenecientes a estas clases.
import csv

class Paciente:
    __dni: int
    __Nombre: str
    __Unidad: str
    
    def __init__(self, dni, Nombre, Unidad):
        self.__dni = dni
        self.__Nombre = Nombre
        self.__Unidad = Unidad
        
    def getDNI(self):
        return self.__dni
    
    def getNombre(self):
        return self.__Nombre
    
    def getUnidad(self):
        return self.__Unidad
    
    def __str__(self):
        return f"{self.__Nombre} - DNI: {self.__dni} - Unidad: {self.__Unidad}"
    
    def __lt__(self, otro):
        return (self.getUnidad(), self.getNombre()) < (otro.getUnidad(), otro.getNombre())