from manejador_beneficiario import ManejadorBeneficiario
from manejador_beca import ManejadorBeca
import csv


def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Cargar Beneficiarios")
    print("2. Cargar Becas")
    print("3. Informar los beneficiarios e importe total que debe disponer la Secretaría para el pago de una Beca.")
    print("4. Leer por teclado un dni, informar si el beneficiario tiene más de una beca,mostrando nombre y apellido.")
    print("5. Mostrar las carreras de una facultad.")
    print("0. Salir")
    
if __name__ == '__main__':
    manejadorBec = ManejadorBeca()
    manejadorBen = ManejadorBeneficiario()
    
    
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))
        
        if opcion == 1:
            manejadorBen.agregarBeneficiario()
        elif opcion == 2:
            manejadorBec.agregarBeca()
        elif opcion == 3:
            tBeca = input("Ingrese un tipo de Beca: ")
            manejadorC.buscarFacultad(nCarrera, manejadorF)
        elif opcion == 4:
            #Leer por teclado un dni, informar si el beneficiario tiene más de una beca,
            # mostrando nombre y apellido
            xDNI = int(input("Ingrese numero de DNI: "))
            informarBecas(xDNI, manejadorBec)
            manejadorF.canCarreras(manejadorC)
        elif opcion == 5:
            nomFacultad = input("Ingrese el nombre de la facultad.")
            manejadorC.mostrarCarrerasDeFacultad(nomFacultad, manejadorF)            
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente de nuevo.")
            
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))