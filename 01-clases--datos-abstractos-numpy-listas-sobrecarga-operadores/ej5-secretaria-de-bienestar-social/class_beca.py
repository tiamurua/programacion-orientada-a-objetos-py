class Beca:
    __idBeca: int
    __tipo: str
    __importe: int
    
    def __init__(self, idBeca, tipo, importe):
        self.__idBeca = idBeca
        self.__tipo = tipo
        self.__importe = importe
        
    def getIdBeca(self):
        return self.__idBeca
    
    def getTipo(self):
        return self.__tipo
    
    def getImporte(self):
        return self.__importe
    
    def __str__(self):
        return f"{self.__idBeca}, {self.__tipo}, ${self.__importe:.2f}"
    
    