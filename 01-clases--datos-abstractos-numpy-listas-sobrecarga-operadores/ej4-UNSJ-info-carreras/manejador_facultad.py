import csv
import numpy as np
from clase_facultad import Facultad
from manejador_carrera import ManejadorCarrera

class ManejadorFacultad:
    __facultades = np.array
    __cantidad = int
    
    
    def __init__(self, cantidad):
        self.__facultades = np.empty(cantidad, dtype=Facultad)
        self.__cantidad = 0
        
    def cargarFacultades(self):
        archivo = open("Facultades.csv", encoding = "utf-8")
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else: 
                codFacultad = int(fila[0])
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telContacto = fila[4]
                facu = Facultad(codFacultad, nombre, direccion, localidad, telContacto)
                self.__facultades[self.__cantidad] = facu
                self.__cantidad += 1
        archivo.close()
        
    def getArreglo(self):
        return self.__facultades
    
    def canCarreras(self, manCar):
        listaCarreras = manCar.getLista()
        
        for i in range(len(self.__facultades)):
            cont = 0
            for j in range(len(listaCarreras)):
                if listaCarreras[j].getCodFac() == self.__facultades[i].getCodFac():
                    cont += 1
            
            print(f"Facultad: {self.__facultades[i].getNombre()} Carreras: {cont}")
            
            
    
    