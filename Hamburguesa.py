pila = []

while True:
    print("\n--- ARMAR HAMBURGUESA ---")
    print("1. Agregar ingrediente")
    print("2. Armar hamburguesa")
    print("3. Ver ingredientes")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        ingrediente = input("Ingrediente: ")
        pila.append(ingrediente)
        print(f"{ingrediente} agregado")

    elif opcion == "2":
        if pila:
            print("\nPreparando hamburguesa:")
            while pila:
                print(f"Agregando {pila.pop()}")
        else:
            print("No hay ingredientes")

    elif opcion == "3":
        print("Ingredientes actuales:", pila)

    elif opcion == "4":
        print("Fin del programa")
        break

    else:
        print("Opción inválida")
