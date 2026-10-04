class ProgramaCapacitacion:
    __nombre: str
    __codigo: str
    __duracion: int
    
    def __init__(self, nombre, codigo, duracion):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__duracion = duracion
        
    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getDuracion(self):
        return self.__duracion
    
    def __str__(self):
        return f"Nombre: {self.getNombre()} - Codigo: {self.getCodigo()} - Duracion: {self.getDuracion()}"
    
    