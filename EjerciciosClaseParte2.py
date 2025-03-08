# Clase Persona
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

# Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, titular, saldo, numero_de_cuenta):
        self.titular = titular
        self.saldo = saldo
        self.numero_de_cuenta = numero_de_cuenta

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad} unidades. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"Se retiraron {cantidad} unidades. Saldo actual: {self.saldo}")

    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

# Clase Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

    def calcular_circunferencia(self):
        return 2 * 3.1416 * self.radio

# Clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año_de_publicacion = año_de_publicacion

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_año_de_publicacion(self):
        return self.año_de_publicacion

    def establecer_año_de_publicacion(self, año):
        self.año_de_publicacion = año

    def mostrar_detalles(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año de Publicación: {self.año_de_publicacion}")

# Clase Canción
class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.titulo = titulo

    def obtener_artista(self):
        return self.artista

    def establecer_artista(self, artista):
        self.artista = artista

    def obtener_album(self):
        return self.album

    def establecer_album(self, album):
        self.album = album

    def obtener_duracion(self):
        return self.duracion

    def establecer_duracion(self, duracion):
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo '{self.titulo}' de {self.artista}...")

# Clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def obtener_cantidad_disponible(self):
        return self.cantidad_disponible

    def establecer_cantidad_disponible(self, cantidad):
        self.cantidad_disponible = cantidad

    def calcular_total(self, cantidad):
        if cantidad > self.cantidad_disponible:
            print("No hay suficiente stock.")
        else:
            return cantidad * self.precio

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def aprobado(self):
        promedio = self.calcular_promedio()
        if promedio >= 6.0:
            return True
        else:
            return False

# Ejemplos de uso
persona = Persona("Juan", 25, "Masculino")
persona.presentarse()

cuenta = CuentaBancaria(persona, 1000, "123456789")
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.consultar_saldo()

rectangulo = Rectangulo(5, 10)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

circulo = Circulo(7)
print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Circunferencia del círculo: {circulo.calcular_circunferencia()}")

libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
libro.mostrar_detalles()

cancion = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", "6:07")
cancion.reproducir()

producto = Producto("Laptop", 1200, 10)
print(f"Total a pagar por 3 laptops: {producto.calcular_total(3)}")

estudiante = Estudiante("Ana", 20, "Matemáticas")
estudiante.agregar_calificacion(8)
estudiante.agregar_calificacion(7)
estudiante.agregar_calificacion(6)
print(f"Promedio del estudiante: {estudiante.calcular_promedio()}")
print(f"¿Aprobó el curso? {'Sí' if estudiante.aprobado() else 'No'}")
