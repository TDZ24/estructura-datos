class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        """Inserta un nuevo valor en el árbol"""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        """Método auxiliar para insertar recursivamente"""
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)
    
    def preorden(self, nodo):
        """Recorrido Pre-Orden: Raíz, Izquierda, Derecha"""
        if nodo is not None:
            print(nodo.valor)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def por_niveles(self):
        """Recorrido por niveles (BFS)"""
        if self.raiz is None:
            print("El árbol está vacío")
            return
        
        cola = [self.raiz]

        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor, end=" ")
            
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def buscar(self, nodo, busqueda):
        """Busca un valor en el árbol"""
        if nodo is None:
            return "El valor no existe", False
        if nodo.valor == busqueda:
            return f"El valor {nodo.valor} existe", True
        if busqueda < nodo.valor:
            return self.buscar(nodo.izquierda, busqueda)
        else:
            return self.buscar(nodo.derecha, busqueda)


# Ejemplo de uso
arbol = ArbolBinario()
numeros = [20, 10, 30, 5, 15, 25, 35]

for num in numeros:
    arbol.insertar(num)

print("Recorrido Pre-Orden:")
arbol.preorden(arbol.raiz)

print("\nRecorrido por Niveles:")
arbol.por_niveles()

print("\n")

# Pruebas de búsqueda
resultado = arbol.buscar(arbol.raiz, 15)
print(resultado)  # ("El valor 15 existe", True)

resultado = arbol.buscar(arbol.raiz, 99)
print(resultado)  # ("El valor no existe", False)