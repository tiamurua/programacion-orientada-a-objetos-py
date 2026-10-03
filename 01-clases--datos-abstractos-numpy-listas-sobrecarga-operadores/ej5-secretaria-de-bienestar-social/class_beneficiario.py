class Beneficiario:
    __dni: int
    __nombre: str
    __apellido: str
    __carrera: str
    __facultad: str
    __anioCursa: int
    __promedio: int
    __idBecaAsignada: int
    
    def __init__(self, dni, nombre, apellido, carrera, facultad, anioCursa, promedio, idBecaAsignada):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera
        self.__facultad = facultad
        self.__anioCursa = anioCursa
        self.__promedio = promedio
        self.__idBecaAsignada = idBecaAsignada
        
    def getDNI(self):
        return self.__dni
    
    def getNombreCompleto(self):
        return self.__nombre, self.__apellido
    
    def getCarrera(self):
        return self.__carrera
    
    def getFacultad(self):
        return self.__facultad
    
    def getAnioCursa(self):
        return self.__anioCursa
    
    def getPromedio(self):
        return self.__promedio
    
    def getIdBecaAsignada(self):
        return self.__idBecaAsignada
    
    def __str__(self):
        return f"DNI: {self.__dni}, {self.__nombre}, {self.__apellido}, {self.__carrera}, {self.__facultad}, {self.__anioCursa}, {self.__promedio}, {self.__idBecaAsignada}"
    
    def __gt__(self, otro):
        return self.__facultad > otro.__facultad
    
    