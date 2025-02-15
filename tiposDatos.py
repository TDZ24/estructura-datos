numeros = list ()
continuar: bool = True

def agregar (numero : int) -> None:
    numeros.append(numero)

def eliminar (numero : int) -> None:
    numeros.pop()


while continuar:
    print("Selecione una opcion")
    print("1. Agregar un número")
    print("2. Eliminar la ultima posicion")
    print("3. Salir")
        
    opcion = int(input())

    if opcion == 3:
        continuar = False

    