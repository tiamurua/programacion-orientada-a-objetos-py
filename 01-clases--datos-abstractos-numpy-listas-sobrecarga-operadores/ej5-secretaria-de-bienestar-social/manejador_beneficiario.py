from manejador_beca import ManejadorBeca
from class_beneficiario import Beneficiario
import csv

class ManejadorBeneficiario:
    __beneficiarios: list
    
    def __init__(self):
        self.__beneficiarios = []
        
    def agregarBeneficiario(self, archivo):
        archivo = open('beneficiarios.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                dni = int(fila[1])
                nombre = fila[2]
                apellido = fila[3]
                carrera = fila[4]
                facultad = fila[5]
                anioCursa = int(fila[6])
                promedio = int(fila[7])
                idBecaAsignada = int(fila[8])
                unBeneficiario = Beneficiario(dni, nombre, apellido, carrera, facultad, anioCursa, promedio, idBecaAsignada, unBeneficiario)
                self.__beneficiarios.append(unBeneficiario)
        archivo.close()
        
    def getLista(self):
        return self.__beneficiarios
    
    def informarSobreTipoBeca(self, tipo_beca):
        ids_beca = []
        importe_total = 0.0
        becas = ManejadorBeca.getLista()

        # Recolectar todos los idBeca del tipo especificado
        for beca in becas:
            if beca.getTipo().lower() == tipo_beca.lower():
                ids_beca.append(beca.getIdBeca())

        if len(ids_beca) == 0:
            print("No se encontraron becas del tipo especificado.")
            return

        print(f"\nBeneficiarios con beca del tipo '{tipo_beca.upper()}':")

        for beneficiario in self.__beneficiarios:
            if beneficiario.getIdBecaAsignada() in ids_beca:
                print(f"- {beneficiario.getNombre()} {beneficiario.getApellido()} (DNI: {beneficiario.getDNI()})")
                # Buscar el importe correspondiente a ese idBeca
                for beca in self.__becas:
                    if beca.getIdBeca() == beneficiario.getIdBecaAsignada():
                        importe_total += float(beca.getImporte())

        print(f"\nImporte total a disponer por la Secretaría: ${importe_total:.2f}")

    def informar_mas_de_una_beca(self, xdni):
        cont = 0
        beneficiario = None
        for beneficiario in self.__beneficiarios:
            if beneficiario.getDNI() == xdni:
                cont += 1
        if cont > 1:
            encontrado = False
            i = 0
            while not encontrado and i < len(self.__beneficiarios):
                if self.__beneficiarios[i].getDNI() == xdni:
                    beneficiario = self.__beneficiarios[i]
                else:
                    i += 1
            return beneficiario
            
    def listarOrdenadosPorFacultad(self):
        lista_ordenada = sorted(self.__beneficiarios, reverse = True) # usa __gt__
        print("\n--- Beneficiarios ordenados por Facultad (descendente) ---")
        for beneficiario in lista_ordenada:
            print(f"Facultad: {beneficiario.getFacultad()} - {beneficiario.getNombreCompleto()} (DNI: {beneficiario.getDNI()})")
            
    def listarAlumnosNoBeneficiarios(self, manejador_becas):
        encontrado = False
        i = 0
        while i < len(manejador_becas.getLista()) and not encontrado:
            if manejador_becas.getTipo().upper() == 'A':
                encontrado = True
                indiceBeca = manejador_becas.getIdBeca()
            else:
                i += 1
            
        print("Alumnos con promedio mayor a 8 pero que no poseen beca de ayuda económica.")        
        for beneficiario in self.__beneficiarios:
            if beneficiario.getPromedio() > 8:
                if beneficiario.getIdBecaAsignada() != indiceBeca:
                    print(f"{beneficiario.getNombreCompleto()} - Promedio: {beneficiario.getPromedio()}")
                    
                    