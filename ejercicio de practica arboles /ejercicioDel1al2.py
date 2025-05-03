class NodoArbol:
    def __init__(self, valor: int):
        self.valor: int = valor
        self.izquierda: 'NodoArbol' = None
        self.derecha: 'NodoArbol' = None

class ArbolBinario:
    def __init__(self):
        self.raiz: 'NodoArbol' = None

    def insertar(self, valor: int) -> None:
        """Inserta un nuevo valor en el árbol manteniendo la propiedad de árbol binario"""
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual: 'NodoArbol', valor: int) -> None:
        """Método auxiliar recursivo para insertar un nuevo nodo"""
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
    
    def preorden(self, nodo: 'NodoArbol') -> None:
        """Recorre el árbol en orden: raíz, izquierda, derecha"""
        if nodo is not None:
            print(nodo.valor)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def por_niveles(self) -> None:
        """Recorre el árbol nivel por nivel (BFS)"""
        if self.raiz is None:
            print("El árbol está vacío")
            return
        
        cola = [self.raiz]  # type: list[NodoArbol]

        while cola:
            nodo_actual = cola.pop(0)
            print(nodo_actual.valor, end=" ")
            
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)

    def buscar(self, nodo: 'NodoArbol', busqueda: int) -> tuple[str, bool]:
        """Busca un valor en el árbol y retorna un mensaje y un booleano"""
        if nodo is None:
            return "El valor no existe", False
        if nodo.valor == busqueda:
            return f"El valor {nodo.valor} existe", True
        if busqueda < nodo.valor:
            return self.buscar(nodo.izquierda, busqueda)
        else:
            return self.buscar(nodo.derecha, busqueda)


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    valores = [20, 10, 30, 5, 15, 25, 35]
    
    for num in valores:
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