class Carrera:
    __codCarrera: int
    __nombre: str
    __fInicio: str
    __duracion: int
    __tituloQueOtorga: str
    __codFacultad: int
    
    def __init__(self, codCarrera, nombre, fInicio, duracion, tituloQueOtorga, codFacultad):
        self.__codCarrera = codCarrera
        self.__nombre = nombre
        self.__fInicio = fInicio
        self.__duracion = duracion
        self.__tituloQueOtorga = tituloQueOtorga
        self.__codFacultad = codFacultad
    
    def getCodFac(self):
        return self.__codFacultad
    
    def getNom(self):
        return self.__nombre
    
    def getDuracion(self):
        return self.__duracion
    
    def __lt__(self, otra):
        return self.__nombre.lower() < otra.getNom().lower()
    