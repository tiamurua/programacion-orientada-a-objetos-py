import csv
from departamento import Departamento
from accidente import Accidente

class ManejadorDepartamentos:
    __deptos: list
    
    def __init__(self):
        self.__deptos = []
        
    def agregarDpto(self, depto):
        self.__deptos.append(depto)
        
    def cargarD(self):
        archivo = open("Departamentos.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idDepa, nomDepa = fila
                unDepa = Departamento(idDepa, nomDepa)
                self.agregarDpto(unDepa)
            
        archivo.close()

    def getDepto(self, i):
        return self.__deptos[i]

    def getNumDepto(self, departamento):
        for i in range (19):
            if self.__deptos[i] == departamento:
                return i
            
    