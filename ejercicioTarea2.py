n = 11

def fibonacci_recursivo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = fibonacci_recursivo(n - 1)

    siguiente = serie[-1] + serie[-2]
    serie.append(siguiente)
    
    return serie

print(f"Los primeros {n} números de la serie Fibonacci son: {fibonacci_recursivo(n)}")