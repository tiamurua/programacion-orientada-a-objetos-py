from gestor_biblioteca import GestorBiblioteca

def testeo():
    gestor_b = GestorBiblioteca()
    
    #Crear biblioteca/s
    corte = int(input("Ingrese 0 para dejar de agregar bibliotecas: "))
    while corte != 0:
        nombre_b = input("Ingrese nombre de la biblioteca: ")
        direccion_b = input("Ingrese direccion: ")
        tel_b = input("Ingrese telefono: ")
        
        gestor_b.agregar_biblioteca(nombre_b, direccion_b, tel_b)
        
        corte = int(input("Ingrese 0 para dejar de agregar bibliotecas: "))
    
    #1 Agregar libro
    nombre_biblioteca = input("Ingrese nombre de la Biblioteca para ingresar un libro en su coleccion: ")
    
    corte = int(input("Ingrese 0 para dejar de agregar libros: "))
    while corte != 0:
        nombre_l = input("Ingrese nombre del libro: ")
        autor_l = input("Ingrese autor: ")
        isbn_l = input("Ingrese ISBN del libro: ")
        genero_l = input("Ingrese genero del libro: ")
        
        gestor_b.agregar_libro(nombre_biblioteca, nombre_l, autor_l, isbn_l, genero_l)
        
        corte = int(input("Ingrese 0 para dejar de agregar libros: "))
        
    #2 Eliminar Libro
    nombre_b = input("Ingrese nombre de la biblioteca: ")
    nombre_l = input("Ingrese Nombre del libro que desea eliminar de la coleccion: ")
    gestor_b.eliminar_libro(nombre_b, nombre_l)
    
    #3 Para un Titulo de libro ingresado por teclado, 
    # mostrar nombre de la biblioteca en la que se encuentra, 
    # nombre del Autor y Género
    titulo_libro = input("Ingrese titulo del libro: ")
    gestor_b.esta_en_biblioteca(titulo_libro)
    
    #4 Listar Libros
    nombre_biblioteca = input("Ingrese nombre de la biblioteca")
    gestor_b.listar_libros(nombre_biblioteca)
    
if __name__ == '__main__':
    testeo()