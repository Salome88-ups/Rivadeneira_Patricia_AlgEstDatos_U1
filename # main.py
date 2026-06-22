# main.py

from pila import Pila
from cola import Cola
from lista import ListaClientes

pila = Pila()
cola = Cola()
lista = ListaClientes()

def menu():
    print("\n--- SISTEMA CARUPS ---")
    print("1. Registrar cliente")
    print("2. Ver clientes")
    print("3. Buscar cliente")
    print("4. Agregar turno")
    print("5. Atender turno")
    print("6. Historial deshacer acción")
    print("7. Ver cola")
    print("0. Salir")

while True:
    menu()
    op = input("Opción: ")

    if op == "1":
        dni = input("DNI: ")
        nombre = input("Nombre: ")
        lista.agregar(dni, nombre)
        pila.push("Registrar cliente")
        print("Cliente registrado.")

    elif op == "2":
        lista.mostrar()

    elif op == "3":
        nombre = input("Nombre a buscar: ")
        cliente = lista.buscar(nombre)
        print(cliente.dni, cliente.nombre) if cliente else print("No encontrado")

    elif op == "4":
        dni = input("DNI turno: ")
        nombre = input("Nombre: ")
        cola.enqueue((dni, nombre))
        pila.push("Registrar turno")
        print("Turno agregado.")

    elif op == "5":
        turno = cola.dequeue()
        print("Atendiendo:", turno)
        pila.push("Atender turno")

    elif op == "6":
        accion = pila.pop()
        print("Se deshizo:", accion)

    elif op == "7":
        cola.mostrar()

    elif op == "0":
        break