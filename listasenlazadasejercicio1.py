class Animal:
    def __init__(self, nombre, edad, tipo):
        """Constructor de la clase Animal"""
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
    
    def __str__(self):
        """Retorna una representación en texto del animal"""
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"
    
    def es_igual(self, otro_animal):
        """Compara si dos animales son iguales por nombre y tipo"""
        return self.nombre == otro_animal.nombre and self.tipo == otro_animal.tipo


class Nodo:
    def __init__(self, animal):
        """Nodo para la lista enlazada"""
        self.animal = animal
        self.siguiente = None


class Zoologico:
    def __init__(self):
        """Inicializa la lista enlazada vacía"""
        self.cabeza = None
    
    def agregar_animal(self, animal):
        """Agrega un animal al zoológico si no existe ya"""
        # Verificar si el animal ya está en la lista
        if self.buscar_animal(animal.nombre, animal.tipo):
            print(f"¡ATENCIÓN! El animal {animal.nombre} de tipo {animal.tipo} ya está registrado en el zoológico.")
            return False
        
        # Crear un nuevo nodo
        nuevo_nodo = Nodo(animal)
        
        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            print(f"Animal {animal.nombre} agregado como primer registro.")
            return True
        
        # Añadir al final de la lista
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        
        actual.siguiente = nuevo_nodo
        print(f"Animal {animal.nombre} de tipo {animal.tipo} agregado correctamente.")
        return True
    
    def buscar_animal(self, nombre, tipo):
        """Busca un animal por nombre y tipo"""
        actual = self.cabeza
        
        while actual:
            if actual.animal.nombre == nombre and actual.animal.tipo == tipo:
                return True
            actual = actual.siguiente
        
        return False
    
    def mostrar_animales_iterativo(self):
        """Muestra todos los animales usando un método iterativo"""
        print("\n=== LISTA DE ANIMALES (Método Iterativo) ===")
        
        if self.cabeza is None:
            print("El zoológico no tiene animales registrados.")
            return
        
        actual = self.cabeza
        contador = 1
        
        while actual:
            print(f"Animal #{contador}: {actual.animal}")
            contador += 1
            actual = actual.siguiente
        
        print(f"Total de animales: {contador-1}")
    
    def mostrar_animales_recursivo(self):
        """Inicia la muestra recursiva de animales"""
        print("\n=== LISTA DE ANIMALES (Método Recursivo) ===")
        
        if self.cabeza is None:
            print("El zoológico no tiene animales registrados.")
            return
        
        self._mostrar_recursivo(self.cabeza, 1)
    
    def _mostrar_recursivo(self, nodo, contador):
        """Función auxiliar recursiva para mostrar animales"""
        # Caso base: fin de la lista
        if nodo is None:
            print(f"Total de animales: {contador-1}")
            return
        
        # Mostrar el animal actual
        print(f"Animal #{contador}: {nodo.animal}")
        
        # Llamada recursiva con el siguiente nodo
        self._mostrar_recursivo(nodo.siguiente, contador + 1)


# Programa principal para demostrar el funcionamiento
def main():
    # Crear el zoológico
    mi_zoo = Zoologico()
    
    # Menú simple para interactuar con el sistema
    while True:
        print("\n--- SISTEMA DE CONTROL DE ANIMALES DEL ZOOLÓGICO ---")
        print("1. Agregar un animal")
        print("2. Mostrar animales (iterativo)")
        print("3. Mostrar animales (recursivo)")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            nombre = input("Nombre del animal: ")
            while True:
                try:
                    edad = int(input("Edad del animal: "))
                    if edad < 0:
                        print("La edad debe ser un número positivo.")
                    else:
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido para la edad.")
            
            tipo = input("Tipo de animal (León, Elefante, etc.): ")
            
            nuevo_animal = Animal(nombre, edad, tipo)
            mi_zoo.agregar_animal(nuevo_animal)
            
        elif opcion == "2":
            mi_zoo.mostrar_animales_iterativo()
            
        elif opcion == "3":
            mi_zoo.mostrar_animales_recursivo()
            
        elif opcion == "4":
            print("¡Gracias por usar el sistema de control del zoológico!")
            break
            
        else:
            print("Opción no válida. Por favor intente de nuevo.")


# Si se ejecuta este archivo directamente
if __name__ == "__main__":
    # Para probar rápidamente con ejemplos predefinidos, descomenta estas líneas:
    zoo_prueba = Zoologico()
    
    # Agregar algunos animales
    zoo_prueba.agregar_animal(Animal("Simba", 4, "León"))
    zoo_prueba.agregar_animal(Animal("Dumbo", 3, "Elefante"))
    zoo_prueba.agregar_animal(Animal("Pepita", 2, "Águila"))
    
    # Intentar agregar un animal repetido
    print("\n-- Intentando agregar un animal repetido --")
    zoo_prueba.agregar_animal(Animal("Simba", 5, "León"))
    
    # Mostrar con ambos métodos
    zoo_prueba.mostrar_animales_iterativo()
    zoo_prueba.mostrar_animales_recursivo()
    
    # Descomentar para usar el menú interactivo:
    # main()