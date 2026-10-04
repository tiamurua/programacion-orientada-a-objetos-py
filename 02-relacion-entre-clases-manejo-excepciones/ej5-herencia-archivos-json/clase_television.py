from clase_medio import Medio

class Television(Medio):
    __cantidad_canales: int 
    __programas: list
    
    def __init__(self, nombre, audiencia, cantidad_canales):
        super().__init__(nombre, audiencia)
        self.__cantidad_canales = cantidad_canales
        self.__programas = []
    
    def getCantCanales(self):
        return self.__cantidad_canales

    def __str__(self):
        return super().__str__() + f"\nCantidad de canales: {self.getCantCanales()}\nProgramas: {self.__programas}"

