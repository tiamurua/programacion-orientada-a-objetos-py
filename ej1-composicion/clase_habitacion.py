class Habitacion:
    __numero: int
    __piso: int
    __tipo: str
    __precio_por_noche: float
    __disponibilidad: bool
    
    def __init__(self, numero, piso, tipo, precio_por_noche, disponibilidad):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio_por_noche = precio_por_noche
        self.__disponibilidad = disponibilidad
        
    def getNumero(self):
        return self.__numero
    
    def getPiso(self):
        return self.__piso
    
    def getTipo(self):
        return self.__tipo
    
    def getPrecioPorNoche(self):
        return self.__precio_por_noche
    
    def getDisponibilidad(self):
        return self.__disponibilidad
    
    def __str__(self):
        return f"Numero: {self.getNumero()} - Piso: {self.getPiso()} - Tipo: {self.getTipo()} - Precio por noche: {self.getPrecioPorNoche()} - Disponibilidad: {self.getDisponibilidad()}"
    
    def setDisponibilidad(self, d):
        self.__disponibilidad = d
