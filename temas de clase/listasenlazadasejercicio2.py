import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento, completada=False):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = completada
        self.siguiente = None
    
    def __str__(self):
        return f"Descripción: {self.descripcion}\nPrioridad: {self.prioridad}\nFecha de vencimiento: {self.fecha_vencimiento.strftime('%d/%m/%Y')}\nEstado: {'Completada' if self.completada else 'Pendiente'}"

class ListaTareas:
    def __init__(self):
        self.cabeza = None
    
    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        """Agrega una nueva tarea a la lista y la ordena por prioridad y fecha"""
        nueva_tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
        
        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nueva_tarea
            return True
        
        # Si la nueva tarea tiene mayor prioridad que la cabeza
        if nueva_tarea.prioridad < self.cabeza.prioridad or \
           (nueva_tarea.prioridad == self.cabeza.prioridad and nueva_tarea.fecha_vencimiento < self.cabeza.fecha_vencimiento):
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
            return True
        
        # Buscar la posición correcta para insertar
        actual = self.cabeza
        while actual.siguiente is not None and \
              (actual.siguiente.prioridad < nueva_tarea.prioridad or \
              (actual.siguiente.prioridad == nueva_tarea.prioridad and actual.siguiente.fecha_vencimiento <= nueva_tarea.fecha_vencimiento)):
            actual = actual.siguiente
        
        nueva_tarea.siguiente = actual.siguiente
        actual.siguiente = nueva_tarea
        return True
    
    def eliminar_tarea(self, descripcion=None, posicion=None):
        """Elimina una tarea por descripción o posición"""
        if self.cabeza is None:
            return False
        
        # Eliminar por descripción
        if descripcion is not None:
            if self.cabeza.descripcion == descripcion:
                self.cabeza = self.cabeza.siguiente
                return True
            
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.siguiente.descripcion == descripcion:
                    actual.siguiente = actual.siguiente.siguiente
                    return True
                actual = actual.siguiente
            
            return False
        
        # Eliminar por posición
        elif posicion is not None:
            if posicion < 0:
                return False
            
            if posicion == 0:
                self.cabeza = self.cabeza.siguiente
                return True
            
            actual = self.cabeza
            contador = 0
            
            while actual is not None and contador < posicion - 1:
                actual = actual.siguiente
                contador += 1
            
            if actual is None or actual.siguiente is None:
                return False
            
            actual.siguiente = actual.siguiente.siguiente
            return True
        
        return False
    
    def mostrar_tareas(self):
        """Muestra todas las tareas ordenadas por prioridad y fecha"""
        if self.cabeza is None:
            print("No hay tareas pendientes.")
            return
        
        print("\n===== LISTA DE TAREAS =====")
        actual = self.cabeza
        posicion = 1
        
        while actual is not None:
            print(f"\n--- Tarea {posicion} ---")
            print(actual)
            actual = actual.siguiente
            posicion += 1
    
    def buscar_tarea(self, descripcion):
        """Busca una tarea por descripción"""
        actual = self.cabeza
        posicion = 1
        
        while actual is not None:
            if actual.descripcion == descripcion:
                print(f"\n--- Tarea encontrada (Posición {posicion}) ---")
                print(actual)
                return actual
            actual = actual.siguiente
            posicion += 1
        
        print(f"No se encontró ninguna tarea con la descripción: '{descripcion}'")
        return None
    
    def marcar_completada(self, descripcion):
        """Marca una tarea como completada y la elimina de la lista"""
        return self.eliminar_tarea(descripcion=descripcion)

def parsear_fecha(fecha_str):
    """Convierte una cadena de fecha en formato dd/mm/aaaa a un objeto datetime"""
    try:
        return datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
    except ValueError:
        return None

def menu_principal():
    lista_tareas = ListaTareas()
    
    while True:
        print("\n===== SISTEMA DE GESTIÓN DE TAREAS =====")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Buscar tarea")
        print("5. Marcar tarea como completada")
        print("0. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            
            prioridad = 0
            while prioridad < 1 or prioridad > 3:
                try:
                    prioridad = int(input("Prioridad (1: Alta, 2: Media, 3: Baja): "))
                    if prioridad < 1 or prioridad > 3:
                        print("La prioridad debe ser un número entre 1 y 3.")
                except ValueError:
                    print("La prioridad debe ser un número entre 1 y 3.")
            
            fecha_valida = False
            while not fecha_valida:
                fecha_str = input("Fecha de vencimiento (dd/mm/aaaa): ")
                fecha = parsear_fecha(fecha_str)
                if fecha is not None:
                    fecha_valida = True
                else:
                    print("Formato de fecha inválido. Use dd/mm/aaaa.")
            
            lista_tareas.agregar_tarea(descripcion, prioridad, fecha)
            print(f"Tarea '{descripcion}' agregada correctamente.")
        
        elif opcion == "2":
            print("\n1. Eliminar por descripción")
            print("2. Eliminar por posición")
            subopcion = input("Seleccione una opción: ")
            
            if subopcion == "1":
                descripcion = input("Descripción de la tarea a eliminar: ")
                if lista_tareas.eliminar_tarea(descripcion=descripcion):
                    print(f"Tarea '{descripcion}' eliminada correctamente.")
                else:
                    print(f"No se encontró ninguna tarea con la descripción: '{descripcion}'")
            
            elif subopcion == "2":
                try:
                    posicion = int(input("Posición de la tarea a eliminar: ")) - 1  # Ajuste para base 0
                    if lista_tareas.eliminar_tarea(posicion=posicion):
                        print(f"Tarea en posición {posicion + 1} eliminada correctamente.")
                    else:
                        print(f"No se encontró ninguna tarea en la posición: {posicion + 1}")
                except ValueError:
                    print("La posición debe ser un número.")
        
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        
        elif opcion == "4":
            descripcion = input("Descripción de la tarea a buscar: ")
            lista_tareas.buscar_tarea(descripcion)
        
        elif opcion == "5":
            descripcion = input("Descripción de la tarea completada: ")
            if lista_tareas.marcar_completada(descripcion):
                print(f"Tarea '{descripcion}' marcada como completada y eliminada de la lista.")
            else:
                print(f"No se encontró ninguna tarea con la descripción: '{descripcion}'")
        
        elif opcion == "0":
            print("¡Gracias por usar el Sistema de Gestión de Tareas!")
            break
        
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()