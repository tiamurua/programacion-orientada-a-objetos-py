from clase_biblioteca import Biblioteca
from clase_libro import Libro

class GestorBiblioteca:
    __bibliotecas: list
    
    def __init__(self):
        self.__bibliotecas = []
        
    def agregar_biblioteca(self, n, d, t):
        self.__bibliotecas.append(Biblioteca(n, d, t))
    
    def buscar_biblioteca_nombre(self, nom_bi):
        i = 0
        encontrado = False
        biblioteca = None
        while i < len(self.__bibliotecas) and not encontrado:
            if self.__bibliotecas[i].getNombre().lower() == nom_bi.lower():
                encontrado = True
                biblioteca = self.__bibliotecas[i]
            else:
                i += 1
        return biblioteca
    
    def agregar_libro(self, nb, n, a, i, g):
        try:
            biblioteca = self.buscar_biblioteca_nombre(nb)
            if biblioteca != None:
                libros = biblioteca.getListaLibros()
                libro = Libro(n, a, i, g)
                if not isinstance(libro, Libro):
                    raise TypeError("El objeto 'libro' no es una instancia de la clase Libro.")
                libros.append(libro)
        except TypeError as e:
            print("ERROR DE TIPO:", e)
    
    def eliminar_libro(self, nom_bi, nom_li):
        biblioteca = self.buscar_biblioteca_nombre(nom_bi)
        if biblioteca != None:
            libro = biblioteca.buscar_libro_nombre(nom_li)
            if libro != None:
                biblioteca.eliminar_libro(libro)
                
    def esta_en_biblioteca(self, nom_lib):
        try:
            for biblioteca in self.__bibliotecas:
                libro = biblioteca.buscar_libro_nombre(nom_lib)
                if libro != None:
                    if not isinstance(libro, Libro):
                        raise TypeError("El objeto 'libro' no es una instancia de la clase Libro.")
                    print(f"El libro se encuentra en: {biblioteca.getNombre()}")
                    print(f"Autor del libro: {libro.getAutor()}")
                    print(f"Genero del libro: {libro.getGenero()}")
                else:
                    print(f"El libro no se encuentra en la coleccion de {biblioteca.getNombre()}.")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
            
    def listar_libros(self, nom_bib):
        try:
            biblioteca = self.buscar_biblioteca_nombre(nom_bib)
            if biblioteca != None:
                if not isinstance(biblioteca, Biblioteca):
                    raise TypeError("El objeto 'biblioteca' no es instancia de la clase Biblioteca.")
                print("Libros en la coleccion:")
                for libro in biblioteca.getListaLibros():
                    print(f"Titulo: {libro.getTitulo()}")
            else:
                print("Biblioteca inexistente.")
        except TypeError as e:
            print("ERROR DE TIPO:", e)
