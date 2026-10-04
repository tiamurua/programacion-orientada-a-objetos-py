from clase_libro import Libro

class Biblioteca:
    __nombre: str
    __direccion: str
    __telefono: str
    __lista_libros: list
    
    def __init__(self, nombre, direccion, telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__lista_libros = []
        
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getListaLibros(self):
        return self.__lista_libros
    
    def __str__(self):
        return f"Nombre: {self.getNombre()} - Direccion: {self.getDireccion()} - Telefono: {self.getTelefono()} - Libros: {self.getListaLibros()}"
        
    def buscar_libro_nombre(self, nom_li):
        i = 0
        encontrado = False
        libro = None
        while i < len(self.__lista_libros) and not encontrado:
            if self.__lista_libros[i].getTitulo().lower() == nom_li.lower():
                encontrado = True
                libro = self.__lista_libros[i]
            else:
                i += 1
        return libro
    
    def eliminar_libro(self, libro):
        try:
            if libro:
                if not isinstance(libro, Libro):
                    raise TypeError("El objeto 'libro' no es una instancia de la clase Libro.")
                self.__lista_libros.remove(libro) #Se quita de la lista
                del libro #se elimina referencia manualmente, activa __del__()
            else:
                print("Libro no encontrado.")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
