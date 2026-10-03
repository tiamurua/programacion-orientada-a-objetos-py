from accidente import Accidente
from manejador_departamento import ManejadorDepartamentos

def menu():
    print("\n------Menu de Opciones------")
    print("1 - Registrar accidente")
    print("2 - Mostrar accidentes de cada departamento en un mes")
    print("3 - Mostrar departamento con mas accidentes en un mes")
    print("4 - Mostrar total anual de un departamento")
    print("5 - Mostrar tabla completa de accidentes")
    print("0 - Salir")


if __name__ == '__main__':
    manejador_deptos = ManejadorDepartamentos()
    manejador_deptos.cargarD()
    
    manejador_accidentes = Accidente()
    manejador_accidentes.cerearTabla()
    
    opcion = -1
    while opcion != 0:
        menu()
        opcion = int(input("Ingrese una opcion:"))
        
        #a. Dado un numero de mes, mostrar para cada uno de los 
        # Departamentos: nombre del departamento y el total de 
        # accidentes ocurridos en el mes dado.
        if opcion == 1:
            numeroDepartamento = int(input("Ingrese el numero de departamento (1 - 19), 0 para finalizar la carga: "))
            
            while numeroDepartamento != 0:
                numeroMes = int(input("Ingrese un numeor de mes (1 - 12): "))
                canAccidentes = int(input("Ingrese cantidad de accidentes: "))
                
                manejador_accidentes.cargarTabla(numeroMes, numeroDepartamento, canAccidentes)
                print("Accidente cargado correctamente.")
                
                numeroDepartamento = int(input("Ingrese el numero de departamento (1 - 19), 0 para finalizar la carga: "))
            
        elif opcion == 2:
            numeroMes = int(input("Ingrese numero de mes (1 - 12): "))
            print("------ Accidentes por departamentos en el mes dado ------")
            
            for i in range(19):
                cantidad = manejador_accidentes.getTabla()[i][numeroMes - 1]
                nombre = manejador_deptos.getDepto(i).getNomDepto()
                print(f"{nombre}: {cantidad} accidentes")
            
        elif opcion == 3:
            nomMes = int(input("Ingrese el numero del mes: "))
            max = -1
            indice = -1
        
            for i in range(19):
                cantidad = manejador_accidentes.getTabla()[i][nomMes]
                if cantidad > max:
                    max = cantidad
                    indice = i
            
            if indice != -1:
                nomDepto = manejador_deptos.getDepto(indice).getNomDepto()
                print(f"Departamento con mas accidentes: {nomDepto} con {cantidad} accidentes.")
            
        elif opcion == 4:
            nomDepto = input("Ingrese nombre del departamento: ")
            indiceDepto = -1

            for i in range(19):
                if manejador_deptos.getDepto(i).getNomDepto().lower() == nomDepto.lower():
                    indiceDepto = i
                    
            if indiceDepto != -1:
                acum = sum(manejador_accidentes.getTabla()[indiceDepto])
                print(f"Total de accidentes en {nomDepto}: {acum}")
            else:
                print("Departamento no encontrado")
        
        elif opcion == 5:
            print("--- TABLA DE ACCIDENTES ---")
            # Mostrar encabezado
            print(f"{'Departamento':<15}", end = "") 
            for m in range(1, 13):
                print(f"{m:>6}", end = "")
            print(f"{'Total':>8}")
            
            #Inicializar un arreglo de totales por mes
            totales = [0] * 12
            
            #Recorrer departamentos
            for i in range(19):
                nombre = manejador_deptos.getDepto(i).getNomDepto()
                print(f"{nombre:<15}", end = "")
                
                for j in range (12):
                    cantidad = manejador_accidentes.getTabla()[i][j]
                    totales[j] += cantidad
                    print(f"{cantidad:>6}", end = "")
                    
            #Mostrar Fila TOTAL
            print(f"{'TOTAL':<15}", end = "")
            for m in range(12):
                print(f"{totales[m]:>6}", end = "")
            
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opcion invalida. Intente nuevamente.")
    