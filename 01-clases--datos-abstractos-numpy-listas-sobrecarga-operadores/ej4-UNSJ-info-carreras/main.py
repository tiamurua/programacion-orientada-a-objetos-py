from manejador_carrera import ManejadorCarrera
from manejador_facultad import ManejadorFacultad

def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Cargar Carreras")
    print("2. Cargar Facultades")
    print("3. Mostrar nombre de la facultad en la que se dicta una carrera.")
    print("4. Mostrar cantidad de carreras por facultad.")
    print("5. Mostrar las carreras de una facultad.")
    print("0. Salir")
    
if __name__ == '__main__':
    manejadorC = ManejadorCarrera()
    manejadorF = ManejadorFacultad()
    
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))
        
        if opcion == 1:
            manejadorC.cargarCarreras()
        elif opcion == 2:
            manejadorF.cargarFacultades()
        elif opcion == 3:
            nCarrera = input("Ingrese el nombre de la carrera: ")
            manejadorC.buscarFacultad(nCarrera, manejadorF)
        elif opcion == 4:
            manejadorF.canCarreras(manejadorC)
        elif opcion == 5:
            nomFacultad = input("Ingrese el nombre de la facultad.")
            manejadorC.mostrarCarrerasDeFacultad(nomFacultad, manejadorF)            
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente de nuevo.")
            
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))
    