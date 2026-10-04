class Matricula:
    __fecha: str
    __empleado: object
    __programa: object
    
    def __init__(self, fecha, empleado, programa):
        self.__fecha = fecha
        self.__empleado = empleado
        self.__programa = programa
        
    def getFecha(self):
        return self.__fecha
    
    def getEmpleado(self):
        return self.__empleado
    
    def getPrograma(self):
        return self.__programa
    
    def __str__(self):
        return f"Fecha: {self.getFecha()} - Empleado: {self.getEmpleado()} - Programa: {self.getPrograma()}"
    
    def setEmpleado(self, empleado):
        self.__empleado = empleado
        
    def setPrograma(self, programa):
        self.__programa = programa
