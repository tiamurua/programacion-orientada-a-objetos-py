from clase_medio import Medio

class Radio(Medio):
    __nombre_emisora: str 
    __frecuencia_transmision: str 
    __programacion: list
    
    def __init__(self, nombre, audiencia, nombre_emisora, frecuencia_transmision):
        super().__init__(nombre, audiencia)
        self.__nombre_emisora = nombre_emisora
        self.__frecuencia_transmision = frecuencia_transmision
        self.__programacion = []
        
    def getNomEmisora(self):
        return self.__nombre_emisora
    
    def getFrecuenciaTrans(self):
        return self.__frecuencia_transmision
    
    def __str__(self):
        return super().__str__() + f"\nNombre de la emisora: {self.getNomEmisora()}\nFrecuencia de transmision: {self.getFrecuenciaTrans()}\nProgramacion: {self.__programacion}"
    
    