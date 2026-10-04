from clase_empleado import Empleado

class GestorEmpleados:
    __empleados: list
    
    def __init__(self):
        self.__empleados = []
        
    def agregar_empleado(self, n, i, p):
        self.__empleados.append(Empleado(n, i, p))
        
    def buscar_empleado_id(self, id):
        i = 0
        encontrado = False
        empleado = None
        while i < len(self.__empleados) and not encontrado:
            if self.__empleados[i].getIDEmpleado() == id:
                encontrado = True
                empleado = self.__empleados[i]
            else:
                i += 1
        return empleado
    
    def getListaEmpleados(self):
        return self.__empleados
    
    