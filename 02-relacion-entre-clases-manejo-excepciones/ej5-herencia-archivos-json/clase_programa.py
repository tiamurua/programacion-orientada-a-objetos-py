class Programa:
    __nombre: str 
    __horario_inicio: str 
    __horario_fin: str
    
    def __init__(self, nombre, horario_inicio, horario_fin):
        self.__nombre = nombre
        self.__horario_inicio = horario_inicio
        self.__horario_fin = horario_fin
        
    def getNombre(self):
        return self.__nombre
    
    def getHorarioInicio(self):
        return self.__horario_inicio
    
    def getHorarioFin(self):
        return self.__horario_fin
    
    def __str__(self):
        return f"Nombre del programa: {self.getNombre()}\nHorario de inicio: {self.getHorarioInicio()}\n{self.getHorarioFin()}"
    
    