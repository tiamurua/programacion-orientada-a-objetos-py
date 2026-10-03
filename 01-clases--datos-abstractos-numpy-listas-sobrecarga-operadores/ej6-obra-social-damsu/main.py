'''El programa debe:






'''
from manejador_atencion import ManejadorAtenciones
from manejador_pacientes import ManejadorPacientes

# 4. A través de un menú de opciones, llevar a cabo las siguientes funcionalidades:
def menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1. Atenciones realizadas e importe total que debe disponer la UNSJ para el pago de la obra social, de una fecha especifica.")
    print("2. Buscar un DNI e informar Nombre y cantidad de atenciones recibidas.")
    print("3. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención")
    print("4. ")
    print("5. ")
    print("0. Salir")
    
if __name__ == '__main__':
    manejadorA = ManejadorAtenciones()
    manejadorP = ManejadorPacientes()
    
    manejadorA.cargarArchivo()
    manejadorP.cargaArchivo()
    
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input(("--- Ingrese numero de opcion ---> ")))
        
        if opcion == 1:
            #a. Leer por teclado una fecha, e informar las atenciones realizadas en dicha fecha y el
            # importe total que debe disponer la UNSJ para el pago a la obra social en esa fecha.
            fecha = input("Ingrese una fecha: ")
            manejadorA.informe_por_fecha(fecha)
            
        elif opcion == 2:
            #b. Leer por teclado un dni, e informar Nombre y apellido, y cantidad de atenciones
            # que tuvo.
            dni = int(input("Ingrese DNI: "))
            manejadorP.informePorDni(dni)
            
        elif opcion == 3:
            #c. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención
            manejadorP.listarPacientesSinAtencion(manejadorA)
                
        elif opcion == 4:
            #d. Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
            # Regla de negocio: para resolver este último punto, el analista le solicita que
            # sobrecargue el operador “<”.
            manejadorP.listaOrdenada(manejadorA)
        elif opcion == 5:
            #Listar nombre, apellido y promedio de los estudiantes, que poseyendo un promedio mayor que 8, no poseen beca de ayuda económica.  
            manejadorBen.listarAlumnosNoBeneficiarios()
                     
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente de nuevo.")'''