import csv
import numpy as np
from class_carrera import Carrera
from manejador_facultad import ManejadorFacultad

class ManejadorCarrera:
    __carreras = np.array
    __cantidad = int
    
    
    def __init__(self, cantidad):
        self.__carreras = np.empty(cantidad, dtype=Carrera)
        self.__cantidad = 0
        
    def cargarCarreras(self):
        archivo = open("Carreras.csv", encoding = "utf-8")
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else: 
                codCarrera = int(fila[0])
                nombre = fila[1]
                fInicio = fila[2]
                duracion = int(fila[3])
                titulo = fila[4]
                codFacu = int(fila[5])
                carrera = Carrera(codCarrera, nombre, fInicio, duracion, titulo, codFacu)
                self.__carreras[self.__cantidad] = carrera
                self.__cantidad += 1
        archivo.close()
        
    def buscarFacultad(self, nc, manFac):
        i = 0
        encontrado = False
        while i < self.__cantidad and not encontrado:
            if self.__carreras[i].getNombre().lower() == nc.lower():
                codF = self.__carreras[i].getCodFac()
                encontrado = True
            else:
                i += 1
                
        if encontrado:
            j = 0
            while i < len(manFac.getArreglo()):
                if manFac.getArreglo()[j].getCodFac() == codF:
                    print(f"La carrera {nc} se dicta en la facultad: {manFac.getArreglo()[j].getNombre()}")
                    return
                else:
                    j += 1
            print("Facultad no encontrada.")
        else:
            print("Carrera no encontrada.")
    
    def getLista(self):
        return self.__carreras
    
    def mostrarCarrerasDeFacultad(self, nf, manFac):
        codFac = None
        i = 0
        encontrado = False
        while i < len(manFac.getArreglo()) and not encontrado:
            if manFac.getArreglo()[i].getNombre().lower() == nf.lower():
                codFac = manFac.getArreglo()[i].getCodFac()
                encontrado = True
            else:
                i += 1
                
        if encontrado:
            carrerasFiltradas = []
            for carrera in self.__carreras:
                if carrera.getCodFac() == codFac:
                    carrerasFiltradas.append(carrera)
                    
            if len(carrerasFiltradas) != 0:
                carrerasFiltradas.sort()
                print(f"Carreras que se dictan en {nf}:")
                for carrera in carrerasFiltradas:
                    print(f"Carrera: {carrera.getNombre()} Duracion: {carrera.getDuracion()}")
            else:
                print(f"No se registraron carreras en {nf}")
        else:
            print("Facultad no encontrada")
            
        
        