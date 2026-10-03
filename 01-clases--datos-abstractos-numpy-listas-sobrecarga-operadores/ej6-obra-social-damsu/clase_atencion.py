# 1. Crear las clases Paciente y Atenciones. Los datos de los archivos representan el estado
#  de los objetos pertenecientes a estas clases.

import csv

class Atencion:
    __Dni: int
    __fecha: str
    __importe: int
    
    def __init__(self, Dni, fecha, importe):
        self.__Dni = Dni
        self.__fecha = fecha
        self.__importe = importe
        
    def getDNI(self):
        return self.__Dni
    
    def getFecha(self):
        return self.__fecha
    
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"DNI: {self.__Dni} - Fecha: {self.__fecha} - Importe: {self.__importe}"