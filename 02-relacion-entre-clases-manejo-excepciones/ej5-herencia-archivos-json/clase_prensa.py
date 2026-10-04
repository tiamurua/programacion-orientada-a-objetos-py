from clase_medio import Medio

class PrensaEscrita(Medio):
    __tipo_publicacion: str 
    __periodicidad: str
    
    def __init__(self, nombre, audiencia, tipo_publicacion, periodicidad):
        super().__init__(nombre, audiencia)
        self.__tipo_publicacion = tipo_publicacion
        self.__periodicidad = periodicidad
        
    def getTipoPublicidad(self):
        return self.__tipo_publicacion
    
    def getPeriodicidad(self):
        return self.__periodicidad
    
    def __str__(self):
        return super().__str__() + f"Tipo de publicacion: {self.getTipoPublicidad()}\nPeriodicidad: {self.getPeriodicidad()}"
    