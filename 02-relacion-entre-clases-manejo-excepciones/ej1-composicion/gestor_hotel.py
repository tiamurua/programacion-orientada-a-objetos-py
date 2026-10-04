from clase_hotel import Hotel
from clase_habitacion import Habitacion

class GestorHotel:
    __hoteles: list
    
    def __init__(self):
        self.__hoteles = []
        
    def agregarHotel(self):
        nombre = input("Ingrese nombre del hotel: ")
        direccion = input("Ingrese direccion: ")
        telefono = input("Ingrese telefono: ")
        un_hotel = Hotel(nombre, direccion, telefono)
        self.__hoteles.append(un_hotel)
        
    def buscar_hotel_nombre(self, nh):
        i = 0
        encontrado = False
        hotel = None
        while i < len(self.__hoteles) and not encontrado:
            if self.__hoteles[i].getNombre().lower() == nh.lower():
                encontrado = True
                hotel = self.__hoteles[i]
            else:
                i += 1
        return hotel
            
    def agregar_habitacion(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'hotel' no es una instancia de la clase Hotel.")
                numero = int(input("Ingrese numero de habitacion: "))
                piso = int(input("Ingrese numero de piso: "))
                tipo_habitacion = input("Ingrese tipo de habitacion: ")
                precio_x_noche = float(input("Ingrese precio por noche: "))
                disponibilidad = input("Ingrese disponibilidad (s/n): ").lower() == 's'
                
                hotel.agregar_habitacion(numero, piso, tipo_habitacion, precio_x_noche, disponibilidad)
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def reservar(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'hotel' no es una instancia de la clase Hotel.")
                
                numero = int(input("Ingresar numero de departamento: "))
                habitacion = hotel.buscar_habitacion_numero(numero)
                if habitacion != None:
                    if not isinstance(habitacion, Habitacion):
                        raise TypeError("El objeto 'habitacion' no es una instancia de la clase Habitacion.")
                
                    if habitacion.getDisponibilidad():
                        habitacion.setDisponibilidad(False)
                    else:
                        print("La habitacion ya se encuentra ocupada.")
                else:
                    print("Habitacion no existente.")
        except ValueError:
            print("ERROR: numero debe ser un dato numerico valido.")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def liberar(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'hotel' no es una instancia de la clase Hotel.")
                numero = int(input("Ingresar numero de departamento: "))
                habitacion = hotel.buscar_habitacion_numero(numero)
                if habitacion != None:
                    if not isinstance(habitacion, Habitacion):
                        raise TypeError("El objeto 'habitacion' no es una instancia de la clase Habitacion.")
            
                    if not habitacion.getDisponibilidad():
                        habitacion.setDisponibilidad(True)
                    else:
                        print("La habitacion ya se encuentra libre.")
                else:
                    print("Habitacion no existente.")
        except ValueError:
            print("ERROR: numero debe ser un dato numerico valido.")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def inciso_4(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'hotel' no es una instancia de la clase Hotel.")
                tipo_habitacion = input("Ingrese un tipo de habitacion (sencilla, doble, suite): ")
                cont = 0
                
                for habitacion in hotel.getListaHabitaciones():
                    if habitacion.getTipo().lower() == tipo_habitacion.lower():
                        print(f"Numero de habitacion: {habitacion.getNumero()}")
                        print(f"Piso: {habitacion.getPiso()}")
                        cont += 1
                        
                if cont == 0:
                    print(f"No hay habitaciones del tipo {tipo_habitacion}")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def inciso_5(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'nom_h' no es una instancia de la clase Hotel.")
                habitaciones = hotel.getListaHabitaciones()
                i = 0
                while i < len(habitaciones):
                    piso_actual = habitaciones[i].getPiso()
                    
                    #Verifico si ya analice este piso
                    j = 0
                    ya_visto = False
                    while j < i and not ya_visto:
                        if habitaciones[j].getPiso() == piso_actual:
                            ya_visto = True
                        j += 1
                    
                    if not ya_visto:
                        #Cuento las habitaciones libres en este piso
                        contador_libres = 0
                        k = 0
                        for habitacion in habitaciones:
                            if habitacion.getPiso() == piso_actual and habitacion.getDisponibilidad():
                                contador_libres += 1
                        print(f"Piso: {piso_actual}: {contador_libres} habitacion/es libre/s")
                    
                    i += 1
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def inciso_6(self, nom_h):
        try:
            hotel = self.buscar_hotel_nombre(nom_h)
            if hotel != None:
                if not isinstance(hotel, Hotel):
                    raise TypeError("El objeto 'hotel' no es una instancia de la clase Hotel.")
                
                i = 0
                habitaciones = hotel.getListaHabitaciones()
                while i < len(habitaciones):
                    tipo_actual = habitaciones[i].getTipo()
                    
                    j = 0
                    ya_mostrado = False
                    while j < i and not ya_mostrado:
                        if habitaciones[j].getTipo().lower() == tipo_actual.lower():
                            ya_mostrado = True
                        j += 1
                        
                    if not ya_mostrado:
                        print(f"\nTipo de habitacion: {tipo_actual}")
                        print(f"{'Numero':<10}{'Piso':<10}{'Precio por noche':<20}{'Disponibilidad':<15}")
                        print("-" * 55)
                        
                        for habitacion in habitaciones:
                            if habitacion.getTipo().lower() == tipo_actual.lower():
                                numero = habitacion.getNumero()
                                piso = habitacion.getPiso()
                                precio = habitacion.getPrecioPorNoche()
                                if habitacion.getDisponibilidad():
                                    disponibilidad = "Libre"
                                else:
                                    disponibilidad = "Ocupada"
                                print(f"{str(numero):<10}{str(piso):<10}${str(precio):<19}{disponibilidad:<15}")
                    
                    i += 1
        except TypeError as e:
            print("ERROR DE TIPO:", e)