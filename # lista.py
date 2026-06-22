# lista.py

class NodoCliente:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.siguiente = None


class ListaClientes:
    def __init__(self):
        self.cabeza = None

    # agregar: O(n) (porque se recorre hasta el final)
    def agregar(self, dni, nombre):
        nuevo = NodoCliente(dni, nombre)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # buscar: O(n)
    def buscar(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente
        return None

    # mostrar: O(n)
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"DNI: {actual.dni} - Nombre: {actual.nombre}")
            actual = actual.siguiente