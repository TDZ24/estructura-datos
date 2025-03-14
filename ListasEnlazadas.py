from typing import Optional

class Animal : 
    nombre: str
    edad: int
    tipoAnimal: str

def __init__(self, nombre: str, edad: int, tipoAnimal: str) -> None:
    self.nombre = nombre
    self.edad = edad
    self.tipoAnimal = tipoAnimal

def get_nombre(self) -> str:
    return self.nombre

def get_edad(self) -> int:
    return self.edad

def get_tipoAnimal(self) -> str:
    return self.tipoAnimal


def set_nombre(self, nombre: str) -> None:
    self.nombre = nombre

def set_edad(self, edad: int) -> None:
    self.edad = edad

def set_tipoAnimal(self, tipoAnimal: str) -> None:
    self.tipoAnimal = tipoAnimal

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional["Node"] = None

    def agregar(self, numero: int) -> None:
        nodo: Node = Node (numero)
        if self.cabeza is None:
            self.cabeza = nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nodo

