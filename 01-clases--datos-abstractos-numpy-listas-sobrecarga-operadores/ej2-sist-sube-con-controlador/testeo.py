from clase_tarjeta_sube import TarjetaSube

def test():
    for i in range(3):
        saldo = int(input("Ingrese saldo de la tarjeta: "))
        numero = int(input("Ingrese numero de la tarjeta: "))
        tarjeta = TarjetaSube(saldo, numero)
        
        vPasaje = int(input("Ingrese el valor del pasaje: "))
        pagado = tarjeta.pagar_pasaje(vPasaje)
        if pagado >= 0:
            print(f"Pasaje pagado exitosamente. Saldo actual: ${pagado}")
        else:
            print("Saldo insuficiente, no es posible pagar el pasaje.")
            
        iCarga = int(input("Ingrese el importe a cargar: "))
        bandera = tarjeta.cargar_saldo(iCarga)
        if bandera:
            print(f"Importe cargado exitosamente. Saldo actual: ${tarjeta.consultar_saldo()}")
        else:
            print("ERROR, el importe debe ser positivo.")
        