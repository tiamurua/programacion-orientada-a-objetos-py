from clase_pro_cap import ProgramaCapacitacion

class GestorProgramaCapacitacion:
    __programas: list
    
    def __init__(self):
        self.__programas = []
        
    def agregar_programa(self, n, c, d):
        self.__programas.append(ProgramaCapacitacion(n, c, d))
        
    def buscar_programa_codigo(self, cod):
        i = 1
        encontrado = False
        programa = None
        while i < len(self.__programas) and not encontrado:
            if self.__programas[i].getCodigo().lower() == cod.lower():
                encontrado = True
                programa = self.__programas[i]
            else:
                i += 1
        return programa
    
    