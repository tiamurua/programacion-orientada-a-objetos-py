from gestor_empleados import GestorEmpleados
from gestor_matricula import GestorMatricula
from gestor_pro_cap import GestorProgramaCapacitacion

def testeo():
    gestor_e = GestorEmpleados()
    gestor_m = GestorMatricula()
    gestor_p = GestorProgramaCapacitacion()
    
    #Crear empleado
    '''
    nombre = input("Ingrese nombre del empleado: ")
    id = int(input("Ingrese ID del empleado: "))
    puesto = input("Ingrese puesto del empleado: ")
    
    gestor_e.agregar_empleado(nombre, id, puesto)
    '''
    gestor_e.agregar_empleado("Laura Gómez", 1, "Analista de Datos")
    gestor_e.agregar_empleado("Carlos Pérez", 2, "Desarrollador Backend")
    gestor_e.agregar_empleado("Sofía Ramírez", 3, "Especialista en RRHH")
    gestor_e.agregar_empleado("Martín Ruiz", 4, "Diseñador UX")
    
    
    #Crear programa de capacitacion
    '''
    nombre = input("Ingresar nombre del programa: ")
    codigo = input("Ingrese codigo del programa: ")
    duracion = int(input("Ingrese duracion del pprograma: "))
    
    gestor_p.agregar_programa(nombre, codigo, duracion)
    '''
    gestor_p.agregar_programa("Liderazgo Empresarial", "P001", 30)
    gestor_p.agregar_programa("Seguridad Informática", "P002", 45)
    gestor_p.agregar_programa("Gestión de Proyectos", "P003", 60)
    
    
    #Crear matricula
    fecha = input("Ingrese fecha: ")
    id_empleado = int(input("Ingrese ID del empleado para la matricula: "))
    codigo_programa = input("Ingrese codigo del programa para la matricula: ")
    
    empleado = gestor_e.buscar_empleado_id(id_empleado)
    programa = gestor_p.buscar_programa_codigo(codigo_programa)
    
    gestor_m.crear_matricula(fecha, empleado, programa)
    
    #Dado el Id del empleado, informe la duración de todos 
    # los programas de capacitación en los que está 
    # matriculado.
    id_empleado = int(input("Ingrese ID de un empleado: "))
    gestor_m.informar_duracion_matriculado(id_empleado)
    
    #Dado el nombre de un programa de capacitación, 
    # muestre el/los empleados matriculados en el 
    # mismo.
    nombre_programa = input("Ingrese nombre de un programa de capacitacion: ")
    gestor_m.mostrar_matriculados_programa(nombre_programa)
    
    #Informar aquellos Empleados que no han sido 
    # matriculados en ningún programa de 
    # capacitación.
    gestor_m.informar_no_matriculados(gestor_e)
    
if __name__ == '__main__':
    testeo()