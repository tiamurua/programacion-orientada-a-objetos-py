from class_beca import Beca
from manejador_beneficiario import ManejadorBeneficiario
import csv

class ManejadorBeca:
    __becas: list
    
    def __init__(self):
        self.__becas = []
        
    def agregarBeca(self, archivo):
        archivo = open('becas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idBeca = int(fila[1])
                tipo = fila[2]
                importe = fila[3]
                unaBeca = Beca(idBeca, tipo, importe)
                self.__becas.append(unaBeca)
        archivo.close()
        
    def getLista(self):
        return self.__becas
    
    