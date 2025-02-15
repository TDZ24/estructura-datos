persona = {}
continuar: bool = True

def agregarValor (clave:str, valor:str) :
    persona.update({clave: valor})

def eliminar (clave:str, valor: str):
    persona.pop()
 
while continuar:
    accion = int(input('que quieres hacer: 1. Agregar / 2. Eliminar / 3. Salir'))

    if accion == 1:
            print('agrega la clave')
            clave: str = input()
            print('agregar valor')
            valor: str = input()
            


