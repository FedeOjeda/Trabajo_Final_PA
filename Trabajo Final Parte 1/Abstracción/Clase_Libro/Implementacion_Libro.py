from libreria import Libreria

# Implementación Libro  
libro = Libreria('Harry Potter', 'J.K.Rowlling', 3000)
libro.alamacenar_libros()
libro = Libreria('Peter Pan', 'Disney', 5000)
libro.alamacenar_libros()
libro = Libreria('Romeo y Julieta', 'Shakespeare', 1000)
libro.alamacenar_libros()
print(libro.precio_total())
print(libro.mostrar_lista())