def fibonacci(n):
    if n <= 0:
        return "Por favor, ingresa un número mayor que 0."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Inicializar la serie con los dos primeros números
    serie = [0, 1]
    
    # Generar los siguientes números de la serie
    for i in range(2, n):
        siguiente = serie[-1] + serie[-2]  # Suma de los dos últimos números
        serie.append(siguiente)
    
    return serie

# Ejemplo de uso
n = 10  # Cambia este valor para generar más o menos números
print(f"Los primeros {n} números de la serie Fibonacci son: {fibonacci(n)}")