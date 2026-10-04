from gestor_planes import GestorPlanes
from clase_plan import Plan

def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Dada una posición de la lista: Mostrar por pantalla qué tipo de plan") 
    print("   se encuentra almacenado en dicha posición (usar la función isinstance()).")
    print("2. Leer por teclado una cobertura geográfica y contar y mostrar la")
    print("   cantidad de planes que corresponden a la misma.")
    print("3. Ingresar por teclado una cantidad de canales internacionales y")
    print("   mostrar el /los nombres de las compañías que ofrecen una cantidad mayor o igual a la ingresada.")
    print("4. Para todos los planes en la lista, mostrar: Tipo de plan, nombre de") 
    print("   la compañía, duración del plan, cobertura geográfica e importe final. Este ítem debe resolverlo en la clase base.")
    print("0. Salir")
    
if __name__ == '__main__':
    GestorP = GestorPlanes()
    GestorP.cargar_archivo()
    
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input(("--- Ingrese opcion ---> ")))
        
        if opcion == 1:
            GestorP.inciso_1()
            
        elif opcion == 2:
            GestorP.inciso_2()
            
        elif opcion == 3:
            GestorP.inciso_3()
            
        elif opcion == 4:
            Plan.inciso_4()
                  
        elif opcion == 0:
            print("Saliendo del programa...")
            
        else:
            print("Opcion invalida. Intente de nuevo.")
            
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))