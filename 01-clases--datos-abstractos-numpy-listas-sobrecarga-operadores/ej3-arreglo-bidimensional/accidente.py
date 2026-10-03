from manejador_departamento import ManejadorDepartamentos

class Accidente:
    __tabla: list
    
    def __init__(self):
        self.__tabla = []
        
    def cerearTabla(self):
        fila = 19
        columna = 12
        
        for i in range(fila):
            fila_aux = []
            for j in range(columna):
                fila_aux.append(0)
            self.__tabla.append(fila_aux)
     
    def cargarTabla(self, mes, depto, cant):
        self.__tabla[depto-1][mes-1] += cant
        
    def getTabla(self):
        return self.__tabla