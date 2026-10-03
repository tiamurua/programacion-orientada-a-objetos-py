from manejador_beca import ManejadorBeca
from manejador_beneficiario import ManejadorBeneficiario

def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Cargar Beneficiarios y Becas")
    print("2. Informar los beneficiarios e importe total que debe disponer la Secretaría para el pago de una Beca.")
    print("3. Leer por teclado un dni, informar si el beneficiario tiene más de una beca,mostrando nombre y apellido.")
    print("4. Beneficiarios ordenados de mayor a menor (por Facultad)")
    print("5. Nombre, apellido y promedio de los estudiantes, que poseyendo un promedio mayor que 8, no poseen beca de ayuda económica.")
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
            manejadorBec.agregarBeca()
            
        elif opcion == 2:
            tBeca = input("Ingrese un tipo de Beca: ")
            manejadorBen.informarSobreTipoBeca(tBeca)
                
        elif opcion == 3:
            #Leer por teclado un dni, informar si el beneficiario tiene más de una beca, mostrando nombre y apellido.
            DNI = int(input("Ingrese DNI: "))
            beneficiario = manejadorBen.informar_mas_de_una_beca(DNI)
            if beneficiario is not None:
                print(f"\n{beneficiario.getNombre()} {beneficiario.getApellido()} tiene mas de una beca.")
            else:
                print(f"\nNo se encontró beneficiario con múltiples becas con el DNI {DNI}.")
                
        elif opcion == 4:
            #Listar los beneficiarios, ordenados de mayor a menor por Facultad.
            manejadorBen.listarOrdenadosPorFacultad()
            
        elif opcion == 5:
            #Listar nombre, apellido y promedio de los estudiantes, que poseyendo un promedio mayor que 8, no poseen beca de ayuda económica.  
            manejadorBen.listarAlumnosNoBeneficiarios()
                     
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente de nuevo.")