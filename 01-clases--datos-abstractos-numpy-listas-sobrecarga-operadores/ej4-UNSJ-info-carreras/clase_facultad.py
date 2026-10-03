class Facultad:
    __codFacultad: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telContacto: int
    
    def __init__(self, codFacultad, nombre, direccion, localidad, telContacto):
        self.__codFacultad = codFacultad
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telContacto = telContacto
        
    def getCodFac(self):
        return self.__codFacultad
    
    def getNombre(self):
        return self.__nombre
    
    def getNombre(self):
        return self.__nombre
    
    