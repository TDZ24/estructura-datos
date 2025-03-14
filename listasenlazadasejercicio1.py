class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_tipo(self):
        return self.tipo

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_tipo(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"


# Clase Nodo para la lista enlazada
class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None


# Clase ListaEnlazada para manejar el registro de animales
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        nuevo_nodo = Nodo(animal)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_animales(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente


# Crear algunos animales
animal1 = Animal("Simba", 5, "León")
animal2 = Animal("Baloo", 10, "Oso")
animal3 = Animal("Raja", 7, "Tigre")

# Crear la lista enlazada y agregar los animales
lista_animales = ListaEnlazada()
lista_animales.agregar_animal(animal1)
lista_animales.agregar_animal(animal2)
lista_animales.agregar_animal(animal3)

# Mostrar todos los animales en el zoológico
print("Animales en el zoológico:")
lista_animales.mostrar_animales()