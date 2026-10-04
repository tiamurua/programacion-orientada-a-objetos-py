class Plan:
    __nombre_compania: str 
    __duracion: int 
    __cobertura: str 
    __precio_base: int
    
    def __init__(self, nombre_compania, duracion, cobertura, precio_base):
        self.__nombre_compania = nombre_compania
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__precio_base = precio_base
        
    def getNomCompania(self):
        return self.__nombre_compania
    
    def getDuracion(self):
        return self.__duracion
    
    def getCobertura(self):
        return self.__cobertura
    
    def getPrecioBase(self):
        return self.__precio_base
    
    def __str__(self):
        cadena = f"Nombre de la compañia: {self.__nombre_compania}\nDuracion: {self.__duracion}\nCobertura: {self.__cobertura}\nPrecio de base: {self.__precio_base}"
        return cadena
    
    def inciso_4(self):
        #Para todos los planes en la lista, mostrar: Tipo de plan, 
        # nombre de la compañía, duración del plan, cobertura geográfica e importe final. Este ítem debe resolverlo en la clase base.
        print(f"Compañia: {self.getNomCompania()}")
        print(f"Duracion del plan: {self.getDuracion()}")
        print(f"Cobertura geografica: {self.getCobertura()}")
        print(f"Importe final: ${self.getPrecioBase():.2f}")