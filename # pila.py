# pila.py

class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.tope = None

    # push: O(1)
    def push(self, dato):
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    # pop: O(1)
    def pop(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def esta_vacia(self):
        return self.tope is None

    def mostrar(self):
        actual = self.tope
        while actual:
            print(actual.dato)
            actual = actual.siguiente