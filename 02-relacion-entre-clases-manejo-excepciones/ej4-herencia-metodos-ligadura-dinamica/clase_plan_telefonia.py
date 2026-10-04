from clase_plan import Plan

class PlanTelefonia(Plan):
    __tipo_llamadas: str 
    __cantidad_minutos: int
    
    def __init__(self, nombre_compania, duracion, cobertura, precio_base, tipo_llamadas, cantidad_minutos):
        super().__init__(nombre_compania, duracion, cobertura, precio_base)
        self.__tipo_llamadas = tipo_llamadas
        self.__cantidad_minutos = cantidad_minutos
        
    def getTipoLlamadas(self):
        return self.__tipo_llamadas
    
    def getCanMinutos(self):
        return self.__cantidad_minutos
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Tipo de llamada: {self.__tipo_llamadas}\n"
                f"Cantidad de minutos: {self.__cantidad_minutos}")
    
    def importe_final(self):
        if self.getTipoLlamadas().lower == "internacional":
            imp_final = super().getPrecioBase() * 0.2 + super().getPrecioBase()
            
        elif self.getTipoLlamadas().lower() == "local":
            imp_final = super().getPrecioBase() - (super().getPrecioBase() * 0.075)
        else:
            imp_final = super().getPrecioBase()
        return imp_final
    
    def inciso_4(self):
        super().inciso_4()
        print(f"Tipo de llamadas: {self.getTipoLlamadas()}")
        print(f"Cantidad de minutos: {self.getCanMinutos()}")
    