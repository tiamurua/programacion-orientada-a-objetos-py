# 3. Leer los datos de las atenciones desde del archivo “Atenciones.csv” y cargarlos en un
#  ManejadorAtenciones usando un arreglonumpy.
from clase_atencion import Atencion
import csv
import numpy as np

class ManejadorAtenciones:
    __cantidad_atenciones: int
    __dimension_arreglo: int
    __incremento = 5
    __atenciones: None

    def __init__(self, dimension = 5, incremento=5):
        self.__atenciones = np.empty(dimension, dtype=Atencion)
        self.__cantidad_atenciones = 0
        self.__dimension_arreglo = dimension

    def agregarAtencion(self, unaAtencion):
        if self.__cantidad_atenciones == self.__dimension_arreglo:
            self.__dimension_arreglo += self.__incremento
            self.__atenciones.resize(self.__dimension_arreglo)
            self.__atenciones[self.__cantidad_atenciones] = unaAtencion
            self.__cantidad += 1
            
    def cargarArchivo(self):
        archivo = open('atenciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dni = int(fila[0])
                fecha = fila[1]
                importe = int(fila[2])
                xAtencion = Atencion(dni, fecha, importe)
                self.agregarAtencion(xAtencion)
        archivo.close()
        
    def getArreglo(self):
        return self.__atenciones
    
    #a. Leer por teclado una fecha, e informar las atenciones realizadas en dicha fecha y el
    # importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha.
    def informe_por_fecha(self, xfecha):
        cont = 0
        acum = 0
        for i in range(self.__cantidad_atenciones):
            if self.__atenciones[i].getFecha() == xfecha:
                cont += 1
                acum += self.__atenciones[i].getImporte()

        if cont > 0:
            print(f"Cantidad de atenciones realizadas el {xfecha}: {cont}")
            print(f"Importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha: {acum}")
        else:
            print("No se encontraron atenciones en la fecha ingresada.")
        
if __name__ == "__main__":
    a = ManejadorAtenciones()
    a.cargarArchivo()
    a.informe_por_fecha("01/04/2025")