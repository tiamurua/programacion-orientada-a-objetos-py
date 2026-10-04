from clase_matricula import Matricula

class GestorMatricula:
    __matriculas: list
    
    def __init__(self):
        self.__matriculas = []
        
    def crear_matricula(self, f, e, p):
        if e != None and p != None:
            nueva = Matricula(f, e, p)
            self.__matriculas.append(nueva)
            print("Matricula creada con exito.")
        else:
            print("ERROR: empleado o programa inexistente.")
            
    #Dado el Id del empleado, informe la duración de todos 
    # los programas de capacitación en los que está 
    # matriculado.
    def informar_duracion_matriculado(self, ie):
        cont = 0
        for matricula in self.__matriculas:
            if matricula.getEmpleado().getIDEmpleado() == ie:
                programa = matricula.getPrograma()
                cont += 1
                print(f"Programa: {programa.getNombre()} - Duracion: {programa.getDuracion()} dias.")
        
        if cont == 0:
            print("El empleado no esta inscripto en ningun programa de capacitacion.")
    
    #Dado el nombre de un programa de capacitación, 
    # muestre el/los empleados matriculados en el 
    # mismo.
    def mostrar_matriculados_programa(self, np):
        cont = 0
        for matricula in self.__matriculas:
            if matricula.getPrograma().getNombre().lower() == np.lower():
                empleado = matricula.getEmpleado()
                cont += 1
                print(f"Nombre completo del empleado: {empleado.getNomCompleto()}")
                
        if cont == 0:
            print(f"Ningun empleado se matriculo en {np}.")
            
    def informar_no_matriculados(self, ge):
        print("Empleado/s no matriculado/s en ningun programa de capacitacion: ")
        for empleado in ge.getListaEmpleados():
            em_id = empleado.getIDEmpleado()
            matriculado = False
            for matricula in self.__matriculas:
                if matricula.getEmpleado().getIDEmpleado() == em_id:
                    matriculado = True
            
            if not matriculado:
                print(f"Nombre Completo del empleado: {empleado.getNomCompleto()}")
    