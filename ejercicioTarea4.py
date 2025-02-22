def multiplicar_por_sumas(a, b):
    resultado = 0
    for _ in range(abs(b)):  # Usamos abs() para manejar números negativos
        resultado += a
    return resultado if b >= 0 else -resultado  # Ajustamos el signo del resultado

# Ejemplo de uso
numero1 = 5
numero2 = 4
resultado = multiplicar_por_sumas(numero1, numero2)
print(f"El resultado de multiplicar {numero1} por {numero2} es: {resultado}")