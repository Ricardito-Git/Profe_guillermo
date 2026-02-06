from collections import deque

cola = deque()

while True:
    print("\n--- CAJA DEL RESTAURANTE ---")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Ver cola")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        cola.append(nombre)
        print(f"{nombre} agregado a la cola")

    elif opcion == "2":
        if cola:
            print(f"Atendiendo a {cola.popleft()}")
        else:
            print("No hay clientes en espera")

    elif opcion == "3":
        print("Clientes en cola:", list(cola))

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
