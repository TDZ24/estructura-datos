## POO
# Clase -> class
# Metodo -> def
# Atributos -> Variable dentro de la clase
# Herencia -> Heredar atributos o caracteristicas de la clase padre 
# Metods / atributos privados -> solo se usas desde la misma clase o clase hija
# apuntadores -> self


# vehiculo -> Clase
# -------------------------
# Color
# Modelo--------> atributos
# Cilindraje
# numeroRueda

# encender
# acelerar
# frenar----------> metodos
# apagar


class Vehiculo : 
    color: str
    marca: str
    modelo: int
    cilindraje: int
    numeroRuedas: int
    combustible: int
    tipo: str

    #Metodo constructor o deconstructor
    def __init__(self, marca:str, combustible:int, tipo:str ) -> None:
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
    
    def __str__(self) -> str:
        return f"La marca del vehiculo es {self.marca}, es un/a {self.tipo} y su combustible es de {self.combustible}"

    def encender(self):
        if self.combustible <= 10: 
            print ("tiene que ponerle gasolina")
        elif self.combustible:
            print("tiene combustible de sobra")
        return

    def acelerar(self):
        while self.combustible > 10:
            self.combustible -= 5
            print(f"Ahora el combustible es {self.combustible}")
        if self.combustible <= 10:
            print("El combustible está bajo")
    

    def frenar(self ):
        pass

    def apagar(self ):
        pass

class Moto(Vehiculo):
    pass

class Carro(Vehiculo):
    pass
    
vehiculo1 = Vehiculo('Lamborghini', 40, 'Carro')
print(vehiculo1)
vehiculo1.encender()
vehiculo1.acelerar()

moto1 = Moto('Kawasaki', 20, 'Moto')
print(moto1)
moto1.encender()
moto1.acelerar()

carro1 = Carro('Chevrolet', 50, 'Carro')
print(carro1)
carro1.encender()
carro1.acelerar()