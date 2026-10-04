from clase_plan_telefonia import PlanTelefonia
from clase_plan_television import PlanTelevision
import csv

class GestorPlanes:
    __planes: list
    
    def __init__(self):
        self.__planes = []
        
    def agregarPlan(self, unPlan):
        self.__planes.append(unPlan)
    
        
    def cargar_archivo(self):
        with open("ej_4/planes.csv", "r", encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            
            next(reader)
            
            for fila in reader:
                tipo = fila[0].upper()
                nombre = fila[1]
                duracion = int(fila[2])
                cobertura = fila[3]
                precio = float(fila[4])
                
                if tipo == 'M':
                    tipo_llamadas = fila[5]
                    minutos = int(fila[6])
                    plan = PlanTelefonia(nombre, duracion, cobertura, precio, tipo_llamadas, minutos)
                    self.agregarPlan(plan)
                    print("Plan cargado exitosamente")
                
                elif tipo == 'T':
                    canales_nac = int(fila[5])
                    canales_inter = int(fila[6])
                    plan = PlanTelevision(nombre, duracion, cobertura, precio, canales_nac, canales_inter)
                    self.agregarPlan(plan)
                    print("Plan cargado exitosamente")
                
                else:
                    print(f"Tipo de plan desconocido: {tipo}")
            archivo.close()
            
    def inciso_1(self):
        #Dada una posición de la lista: Mostrar por pantalla qué tipo de plan 
        # se encuentra almacenado en dicha posición (usar la función isinstance()).
        posicion = int(input("Ingrese un numero de posicion: "))
        if 0 <= posicion < len(self.__planes):
            if isinstance(self.__planes[posicion], PlanTelefonia):
                print(f"Tipo de plan almacenado en la posicion: {posicion}")
                print(self.__planes[posicion])
            elif isinstance(self.__planes[posicion], PlanTelevision):
                print(f"Tipo de plan almacenado en la posicion: {posicion}")
                print(self.__planes[posicion])
        else:
            print("Posicion no valida.")
            
    def inciso_2(self):
        #Leer por teclado una cobertura geográfica y contar y mostrar la
        # cantidad de planes que corresponden a la misma.
        cobertura = input("Ingrese una cobertura geografica: ")
        cont = 0
        for plan in self.__planes:
            if plan.getCobertura().lower() == cobertura.lower():
                cont += 1
        print(f"Cantidad de planes que tienen esta cobertura: {cont} planes.")
        
    def inciso_3(self):
        #Ingresar por teclado una cantidad de canales internacionales y 
        # mostrar el /los nombres de las compañías que ofrecen una cantidad mayor o igual a la ingresada.
        cantidad = int(input("Ingrese una cantidad de canales internacionales: "))
        print(f"Nombre de compañia/s que ofrecen una cantidad de canales internacionales mayor o igual a {cantidad}")
        c = 0
        for plan in self.__planes:
            if isinstance(plan, PlanTelevision):
                if plan.getCanCanalesInter() >= cantidad:
                    print(f"- {plan.getNomCompania()}")
                    c += 1
        
        if c == 0:
            print(f"Ninguna compañia ofrece una cantidad de canales internacionales mayor o igual a {cantidad}")
            
