class Departamento:
    __idDepto: int
    __nombre: str
    
    def __init__(self, numero, nombre):
        self.__idDepto = numero
        self.__nombre = nombre
        
    def getIdDepto(self):
        return self.__idDepto
    
    def getNomDepto(self):
        return self.__nombre

        
