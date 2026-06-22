# cola.py

class NodoCola:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None


class Cola:
    def __init__(self):
        self.head = None
        self.tail = None

    # enqueue: O(1)
    def enqueue(self, cliente):
        nuevo = NodoCola(cliente)
        if self.tail is None:
            self.head = self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo

    # dequeue: O(1)
    def dequeue(self):
        if self.head is None:
            return None
        cliente = self.head.cliente
        self.head = self.head.siguiente
        if self.head is None:
            self.tail = None
        return cliente

    def esta_vacia(self):
        return self.head is None

    def mostrar(self):
        actual = self.head
        while actual:
            print(actual.cliente)
            actual = actual.siguiente
            # Cola de turnos CarUPS
