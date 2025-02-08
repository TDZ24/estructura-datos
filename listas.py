temperatura = []

for n in range(0, 5):
    t = int(input("Registre la temperatura: "))
    temperatura.append(t)

promedio = sum (temperatura) / len(temperatura) 

if promedio < 20:
    print("Se necesita un arreglo, la temperatura promedio es baja.")
elif 20 <= promedio <= 30:
    print("La temperatura es óptima.")
else:
    print("Se necesita un arreglo, la temperatura promedio es alta.")
