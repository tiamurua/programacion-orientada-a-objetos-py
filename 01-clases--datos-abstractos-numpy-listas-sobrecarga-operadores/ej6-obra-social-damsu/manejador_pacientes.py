#2. Leer los datos de los Pacientes desde el archivo “Pacientes.csv” y cargarlos en un
# ManejadorPacientes implementado usando una lista de Python.
import csv
from clase_paciente import Paciente
from manejador_atencion import ManejadorAtenciones

class ManejadorPacientes:
    __pacientes: list
    
    def __init__(self):
        self.__pacientes = []
        
    def agregarPaciente(self, p):
        self.__pacientes.append(p)
        
    def cargaArchivo(self):
        archivo = open('pacientes.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dni = fila[0]
                nombre = fila[1]
                unidad = fila[2]
                unPaciente = Paciente(dni, nombre, unidad)
                self.agregarPaciente(unPaciente)
        archivo.close()
        
    def informePorDni(self, xDni):
        encontrado = False
        i = 0
        while i < len(self.__pacientes) and not encontrado:
            if self.__pacientes[i].getDNI() == xDni:
                print(f"Nombre: {self.__pacientes[i].getNombre()}")
                encontrado = True
            else:
                i += 1
                
        cont = 0
        manAte = ManejadorAtenciones.getArreglo()
        for atencion in manAte:
            if atencion.getDNI() == xDni:
                cont += 1
        
        print(f"Cantidad de atenciones recibidas: {cont}")
        
    #c. Listar nombre, apellido de los pacientes que no tuvieron ninguna atención
    def listarPacientesSinAtencion(self, ma):
        print("Pacientes que no tuvieron ningun tipo de atencion: ")
        for paciente in self.__pacientes:
            if not ma.buscarAtencion(paciente.getDNI()):
                print(f"{paciente.getNombre()}")
    
    #d. Listar los Pacientes, ordenados por Apellido, de menor a mayor por unidad.
    # Regla de negocio: para resolver este último punto, el analista le solicita que
    # sobrecargue el operador “<”.            
    def incisoD(self):
        self.__pacientes.sort()
        print("Pacientes (AyN - DNI - Unidad):")
        for paciente in self.__pacientes:
            print(paciente)
                
if __name__ == "__main__":
    mp = ManejadorPacientes()
    mp.cargaArchivo()
    ma = ManejadorAtenciones()
    ma.cargarArchivo()
    mp.incisoD()