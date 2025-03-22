numeros = list()

def agregar(numero: int):
    numeros.append(numero)
    print(f"Número {numero} agregado a la lista.")
    return numeros

def eliminar(numero: int):
    if numero in numeros:
        numeros.pop()
        print(f"Número {numero} eliminado de la lista.")
    else:
        print(f"El número {numero} no está en la lista.")
    return numeros

def bucle_ciclo():
    while True:
        print("\nLista actual:", numeros)
        print("1. Agregar un número")
        print("2. Eliminar un número")
        print("3. Salir")
        
        opcion = input("Seleccione una operación (1/2/3): ")
        
        if opcion == "1":
            try:
                numero = int(input("Ingrese un número para agregar: "))
                agregar(numero)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            try:
                numero = int(input("Ingrese un número para eliminar: "))
                eliminar(numero)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Ejecutar el bucle
bucle_ciclo()


numeros = {}

def agregar(nombre: str, numero: int):
    numeros[nombre] = numero
    print(f"Número {numero} agregado con la clave '{nombre}'.")
    return numeros

def eliminar(nombre: str):
    if nombre in numeros:
        numero_eliminado = numeros.pop(nombre)
        print(f"Número {numero_eliminado} con clave '{nombre}' eliminado del diccionario.")
    else:
        print(f"La clave '{nombre}' no está en el diccionario.")
    return numeros

def bucle_ciclo():
    while True:
        print("\nDiccionario actual:", numeros)
        print("1. Agregar un número")
        print("2. Eliminar un número")
        print("3. Salir")
        
        opcion = input("Seleccione una operación (1/2/3): ")
        
        if opcion == "1":
            try:
                nombre = input("Ingrese un nombre para la clave: ")
                numero = int(input("Ingrese un número para agregar: "))
                agregar(nombre, numero)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la clave para eliminar: ")
            eliminar(nombre)
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

# Ejecutar el bucle
bucle_ciclo()