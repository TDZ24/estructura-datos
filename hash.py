class Persona:
    def __init__(self, nombre, telefono, direccion):
        if not nombre or not telefono or not direccion:
            raise ValueError("Todos los campos son obligatorios")
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError("El teléfono debe ser un número de 10 dígitos")
        
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
    
    def __str__(self):
        return f"{self.nombre}, {self.telefono}, {self.direccion}"
    
    def get_key(self):
        return self.telefono


def hash(clave, tamaño_tabla):
    return sum(ord(c) for c in str(clave)) % tamaño_tabla


class TablaHash:
    def __init__(self, tamaño=10):
        self.tabla = [None] * tamaño
    
    def insertar(self, persona):
        if not isinstance(persona, Persona):
            print("Error: El objeto no es una persona válida")
            return False
        
        if self.buscar(persona.get_key()) is not None:
            print("Error: El número de teléfono ya está registrado")
            return False
        
        if None not in self.tabla:
            print("Tabla llena")
            return False

        posicion = hash(persona.get_key(), len(self.tabla))
        while self.tabla[posicion] is not None:
            posicion = (posicion + 1) % len(self.tabla)

        self.tabla[posicion] = persona
        return True
    
    def buscar(self, clave):
        posicion = hash(clave, len(self.tabla))
        while self.tabla[posicion]:
            if self.tabla[posicion].get_key() == clave:
                return self.tabla[posicion]
            posicion = (posicion + 1) % len(self.tabla)
        return None
    
    def eliminar(self, clave):
        posicion = hash(clave, len(self.tabla))
        while self.tabla[posicion]:
            if self.tabla[posicion].get_key() == clave:
                self.tabla[posicion] = None
                return True
            posicion = (posicion + 1) % len(self.tabla)
        return False
    
    def listar(self):
        return [p for p in self.tabla if p is not None]

# Ejemplo
def probar_directorio():
    directorio = TablaHash(10)
    personas = [
        Persona("Thomas Pérez", "3001234567", "Calle 1 # 2-3"),
        Persona("María López", "3007654321", "Avenida 4 # 5-6"),
        Persona("Carlos Gómez", "3009876543", "Carrera 7 # 8-9"),
        Persona("Ana Martínez", "3001122334", "Calle 10 # 11-12"),
        Persona("Pedro Rodríguez", "3005566778", "Avenida 13 # 14-15")
    ]
    
    # Insertar personas con validación
    for p in personas:
        if directorio.insertar(p):
            print(f"{p.nombre} ha sido agregado correctamente.")
        else:
            print(f"Error al agregar {p.nombre}.")

    # Buscar persona
    print(directorio.buscar("3007654321"))
    
    # Listar personas
    for persona in directorio.listar():
        print(persona)
    
    # Eliminar persona
    directorio.eliminar("3001234567")
    print(directorio.buscar("3001234567"))  # Debería ser None

probar_directorio()
