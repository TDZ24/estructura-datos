def dividir_por_restas(dividendo, divisor):
    if divisor == 0:
        return "Error: No se puede dividir por cero."
    
    cociente = 0
    signo = 1  # Para manejar el signo del resultado
    
    # Manejar casos donde el dividendo o el divisor son negativos
    if (dividendo < 0) ^ (divisor < 0):  # XOR para determinar el signo
        signo = -1
    
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    
    # Restar el divisor del dividendo hasta que el dividendo sea menor que el divisor
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    
    return cociente * signo

# Ejemplo de uso
dividendo = 20
divisor = 4
resultado = dividir_por_restas(dividendo, divisor)
print(f"El resultado de dividir {dividendo} entre {divisor} es: {resultado}")