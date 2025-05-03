# 1. Clases Empleado, Gerente, Desarrollador

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre} está supervisando al equipo en el departamento de {self.departamento}.")
        self.supervisarAEquipo()

    def supervisarAEquipo(self):
        print(f"{self.nombre} está supervisando a los siguientes empleados: {', '.join(self.equipo)}.")

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion} en el departamento de {self.departamento}.")
        self.escribirCodigo()

    def escribirCodigo(self):
        print(f"{self.nombre} está desarrollando una nueva funcionalidad.")

# 2. Clases FiguraGeometrica, Triangulo, Cuadrado

class FiguraGeometrica:
    def calcularArea(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado

# 3. Clases Electrodomestico, Lavadora, Refrigerador

class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergetico):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico

    def encender(self):
        print(f"El electrodoméstico {self.marca} {self.modelo} está encendido.")

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, capacidad):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def encender(self):
        super().encender()
        self.iniciarCicloDeLavado()

    def iniciarCicloDeLavado(self):
        print(f"La lavadora {self.marca} {self.modelo} está iniciando un ciclo de lavado con capacidad de {self.capacidad} kg.")

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        super().encender()
        self.regularTemperatura()

    def regularTemperatura(self):
        print(f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura. ¿Tiene congelador? {self.tieneCongelador}.")

# 4. Clases Usuario, Administrador, Cliente

class Usuario:
    def __init__(self, nombreDeUsuario, contraseña):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña

    def iniciarSesion(self):
        print(f"El usuario {self.nombreDeUsuario} ha iniciado sesión.")

class Administrador(Usuario):
    def __init__(self, nombreDeUsuario, contraseña):
        super().__init__(nombreDeUsuario, contraseña)

    def gestionarUsuarios(self):
        print(f"El administrador {self.nombreDeUsuario} está gestionando usuarios.")

class Cliente(Usuario):
    def __init__(self, nombreDeUsuario, contraseña):
        super().__init__(nombreDeUsuario, contraseña)

    def realizarCompra(self):
        print(f"El cliente {self.nombreDeUsuario} está realizando una compra.")

# Ejemplos de uso

# Empleados
empleado1 = Empleado("Juan", 30000, "Ventas")
empleado1.trabajar()

gerente1 = Gerente("Ana", 50000, "Desarrollo", ["Carlos", "Maria"])
gerente1.trabajar()

desarrollador1 = Desarrollador("Luis", 40000, "TI", "Python")
desarrollador1.trabajar()

# Figuras Geometricas
triangulo1 = Triangulo(10, 5)
print(f"Área del triángulo: {triangulo1.calcularArea()}")

cuadrado1 = Cuadrado(7)
print(f"Área del cuadrado: {cuadrado1.calcularArea()}")

# Electrodomésticos
lavadora1 = Lavadora("Samsung", "WM123", 1200, 8)
lavadora1.encender()

refrigerador1 = Refrigerador("LG", "RF456", 1500, True)
refrigerador1.encender()

# Usuarios
usuario1 = Usuario("user123", "password123")
usuario1.iniciarSesion()

admin1 = Administrador("admin", "admin123")
admin1.iniciarSesion()
admin1.gestionarUsuarios()

cliente1 = Cliente("cliente1", "cliente123")
cliente1.iniciarSesion()
cliente1.realizarCompra()