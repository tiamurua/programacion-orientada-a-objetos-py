from clase_prensa import PrensaEscrita
from clase_radio import Radio
from clase_television import Television
import json

class GestorMedios:
    __medios: list
    
    def __init__(self):
        self.__medios = []
        
    def cargar_archivo(self):
        try:
            with open("ejercicio_5/medios.json", "r", encoding='utf-8') as archivo:
                datos = json.load(archivo)
            
                for medio in datos:
                    tipo = medio["tipo"].lower()
                    
                    if tipo == "television":
                        nombre = medio["nombre"]
                        audiencia = medio["audiencia"]
                        cantidad_canales = medio[""]