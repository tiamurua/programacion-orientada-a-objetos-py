from clase_tarjeta_sube import TarjetaSube

class Controlador:
    __tarjetas = list
    
    def __init__(self, lista):
        self.__tarjetas = []
        
    def agregarTarjetas(self, unaTarjeta):
        if isinstance(unaTarjeta, TarjetaSube):
            self.__tarjetas.append(unaTarjeta)
        else:
            print("ERROR, el objeto debe ser una tarjeta sube.")
        
    def tarjetasSaldoNegativo(self):
        contador = 0
        for tarjeta in self.__tarjetas:
            if TarjetaSube.consultar_saldo < 0:
                print(f"La siguiente tarjeta tiene saldo negativo: {TarjetaSube.getNumero}")
            else: contador += 1
            
            if contador == 0:
                print("No hay tarjetas con saldo negativo")
                
    def buscarTarjeta(self, numero):
        i = 0
        encontrado = False
        while i < len(self.__tarjetas) and not encontrado:
            if self.__tarjetas[i].getNumero() == numero:
                print(f"Saldo de la tarjeta: ${self.__tarjetas[i].consultar_saldo()}.")
                encontrado = True
            else:
                i += 1
        if not encontrado:
            print(f"La tarjeta sube: {numero} no se encuentra en la lista.")
            