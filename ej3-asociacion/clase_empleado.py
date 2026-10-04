class Empleado:
    __nombre_y_apellido: str
    __id_empleado: int
    __puesto: str
    
    def __init__(self, nombre_y_apellido, id_empleado, puesto):
        self.__nombre_y_apellido = nombre_y_apellido
        self.__id_empleado = id_empleado
        self.__puesto = puesto
        
    def getNomCompleto(self):
        return self.__nombre_y_apellido
    
    def getIDEmpleado(self):
        return self.__id_empleado
    
    def getPuesto(self):
        return self.__puesto
    
    def __str__(self):
        return f"Nombre y apellido: {self.getNomCompleto()} - ID Empleado: {self.getIDEmpleado()} - Puesto: {self.getPuesto()}"
    
    