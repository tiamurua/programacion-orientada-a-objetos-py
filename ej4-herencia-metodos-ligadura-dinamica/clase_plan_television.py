from clase_plan import Plan

class PlanTelevision(Plan):
    __cantidad_canales_nacionales: int
    __cantidad_canales_internacionales: int
    
    def __init__(self, nombre_compania, duracion, cobertura, precio_base, cantidad_canales_nacionales, cantidad_canales_internacionales):
        super().__init__(nombre_compania, duracion, cobertura, precio_base)
        self.__cantidad_canales_nacionales = cantidad_canales_nacionales
        self.__cantidad_canales_internacionales = cantidad_canales_internacionales
        
    def getCanCanalesNac(self):
        return self.__cantidad_canales_nacionales
    
    def getCanCanalesInter(self):
        return self.__cantidad_canales_internacionales
    
    def __str__(self):
        return (super().__str__() + "\n"
                f"Cantidad de canales nacionales: {self.__cantidad_canales_nacionales}\n"
                f"Cantidad de canales internacionales: {self.__cantidad_canales_internacionales}\n")
    
    def importe_final(self):
        if self.getCanCanalesInter() > 10:
            imp_final = super().getPrecioBase() * 0.15 + super().getPrecioBase()
        else:
            imp_final = super().getPrecioBase()
        return imp_final
    
    def inciso_4(self):
        super().inciso_4()
        print(f"Cantidad de canales nacionales: {self.getCanCanalesNac()}")
        print(f"Cantidad de canales internacionales: {self.getCanCanalesInter()}")