class TarjetaSube:
    __saldo: int
    __numero: int
    
    def __init__(self, saldo, numero):
        self.__saldo = saldo
        self.__numero = numero
    
    def getNumero(self):
        return self.__numero
    
    def __str__(self):
        return f"Numero de tarjeta: {self.__numero}, Saldo: {self.__saldo}"
    
    #El método cargar_saldo(importe), debe verificar que el 
    # importe sea positivo.
    def cargar_saldo(self, importe):
        if importe > 0:
            self.__saldo += importe
            return True
        else:
            return False
    
    #El método Pagar_pasaje(Importe), debe verificar si hay 
    # saldo suficiente, en caso afirmativo llevar a cabo la 
    # operación e informar el nuevo saldo, y en caso negativo, 
    # devolver un valor negativo que se deberá chequear para 
    # saber si se pudo realizar el pago.        
    def pagar_pasaje(self, importe):
        if self.__saldo >= importe:
            self.__saldo -= importe
            return self.__saldo
        else:
            return -1
        
    def consultar_saldo(self):
        return self.__saldo
    