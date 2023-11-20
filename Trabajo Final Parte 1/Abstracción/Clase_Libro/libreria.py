from libro import Libro

# Clase Librería
class Libreria(Libro):
    lista_libros = []
   
    def alamacenar_libros(self):
        self.libro = (self.autor,self.titulo,self.precio)
        self.lista_libros.append(self.libro)
        return self.lista_libros
    
    def mostrar_lista(self):
        return self.lista_libros
    
    def precio_total(self):
        total = 0
        for self.libro in self.lista_libros:
               total += self.libro[-1]
        return f'El precio total de todos los libros es ${total} pesos.'